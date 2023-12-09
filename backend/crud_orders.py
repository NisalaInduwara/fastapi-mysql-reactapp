from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import models
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from sqlalchemy import func

chrome_driver_path = 'webdriver\chromedriver.exe'
chrome_service = Service(executable_path=chrome_driver_path)
tracking_details_path = 'https://parcelsapp.com/en/tracking/'


def add_pre_order(db: Session, Order_id: str, Order_Date: str, Order_earning: int,
              Buyer_name: str, Contact_number: str, variation: Optional[str]=None):
    try:
        pre_order = models.PreOrders(Order_id=Order_id, Order_Date=Order_Date, Order_earning=Order_earning, 
                                     Buyer_name=Buyer_name, Contact_number=Contact_number, variation=variation)
        db.add(pre_order)
        db.commit()
        db.refresh(pre_order)
        return {'Order_id': pre_order.Order_id}
     
    except Exception as e:
        db.rollback()
        raise Exception(f"Pre Order adding failed: An error occurred {str(e)}")
    

def add_post_order(db: Session, Order_id: str, Ali_order_id: str, Tracking_number: int, 
                   next_tracking_number: str, item_cost: int):
    try:
        post_order = models.PostOrders(Order_id=Order_id, Ali_order_id=Ali_order_id, Tracking_number=Tracking_number, 
                                next_tracking_number=next_tracking_number, item_cost=item_cost)
        db.add(post_order)
        db.commit()
        db.refresh(post_order)
        return {'Order_id': post_order.Order_id}
     
    except Exception as e:
        db.rollback()
        raise Exception(f"Post Order adding failed: An error occurred {str(e)}")
    

def make_return_case(db: Session, Order_id: str, loss: int, is_resolved: bool):
    try:
        return_case = models.Returns(Order_id=Order_id, loss=loss, is_resolved=is_resolved)
        db.add(return_case)
        db.commit()
        db.refresh(return_case)
        return {'Order_id': return_case.Order_id}
    
    except Exception as e:
        db.rollback()
        raise Exception(f"Return making failed: An error occurred {str(e)}")
    

def get_preorder_data(db: Session, Order_id: str):

    try:
        order = db.query(models.PreOrders).filter(models.PreOrders.Order_id == Order_id).first()
        if order:
             return {"Order_id": order.Order_id, "Date": order.Order_Date, "Order_earning": order.Order_earning, 
                     "Buyer_name": order.Buyer_name, "Contact_number": order.Contact_number, "variation": order.variation}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error fetching order details: {str(e)}")
    
    
def get_postorder_data(db: Session, Order_id: Optional[str]=None, Ali_order_id: Optional[str]=None, 
                       Tracking_number: Optional[str]=None):

    try:
        post_order = db.query(models.PostOrders).filter(
            models.PostOrders.Order_id == Order_id or
            models.PostOrders.Ali_order_id == Ali_order_id or
            models.PostOrders.Tracking_number==Tracking_number or 
            models.PostOrders.next_tracking_number==Tracking_number).first()
        if post_order:
            {"Ali_order_id": post_order.Ali_order_id, "Tracking_number": post_order.Tracking_number,
             "next_tracking_number": post_order.next_tracking_number}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error fetching order details: {str(e)}")


def get_tracking_link(db: Session, Order_id: str):
    try:
        order = db.query(models.PostOrders).filter(models.PostOrders.Order_id == Order_id).first()
        if order:
            tracking_number = order.Tracking_number
            next_tracking_number = order.next_tracking_number
            if next_tracking_number:
                return {'tracking_link': f'{tracking_details_path}{next_tracking_number}'}
            else:
                return {'tracking_link': f'{tracking_details_path}{tracking_number}'}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error fetching tracking number: {str(e)}")


def delete_order(db: Session, Order_id: str):

    return_message = ''
    try: 
        pre_order = db.query(models.PreOrders).filter(models.PreOrders.Order_id == Order_id).first()
        post_order = db.query(models.PostOrders).filter(models.PostOrders.Order_id == Order_id).first()
        return_case = db.query(models.Returns).filter(models.Returns.Order_id == Order_id).first()
        if pre_order:
            db.delete(pre_order)
            return_message = 'PRE_ORDER_DELETED'
        if post_order:
            db.delete(post_order)
            return_message = f'{return_message}|POST_ORDER_DELETED'
        if return_case:
            db.delete(return_case)
            return_message = f'{return_message}|RETURN_DATA_DELETED'
        db.commit()
        return {'message': return_message}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting Pre order item: {str(e)}")
            
    
def get_contact_details(db: Session, Order_Date: str):
    try:
        contact_data = db.execute(
            select(models.PreOrders.Order_id, models.PreOrders.Buyer_name, models.PreOrders.Contact_number)
            .where(models.PreOrders.Order_Date==Order_Date)
            .order_by(models.PreOrders.Order_id)).fetchall()
        contact_list = [{"Order_id": row[0], "Buyer_Name": row[1], "Contact_number": row[2]} for row in contact_data]
        return contact_list
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error getting contact details: {str(e)}")

    
def add_next_tracking_number(db: Session, next_tracking_number: str, Tracking_number: str):
    try:
        order = db.query(models.PostOrders).filter(models.PostOrders.Tracking_number==Tracking_number).first()
        if order:
            order.next_tracking_number = next_tracking_number
            db.commit()
            db.refresh(order)
            return {"Tracking_number": order.Tracking_number, "next_tracking_number" : order.next_tracking_number}
        else:
            raise HTTPException(status_code=404, detail="No order data found")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding next tracking number: {str(e)}")


def resolve_return_case(db: Session, Order_id: str, ali_refund: int):
    try:
        order = db.query(models.Returns).filter(models.Returns.Order_id == Order_id).first()
        if order:
            loss = order.loss - ali_refund
            order.loss = loss
            order.is_resolved = True
            db.commit()
            db.refresh(order)
            return {'ID': order.Order_id, 'loss': order.loss}
        else:
            raise HTTPException(status_code=404, detail="No order data found")
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error closing return cases: {str(e)}")


def get_counts(db: Session):
    
    try:
        if db.query(func.count(models.PreOrders.Order_id)).scalar() != None:
            total_order_count = db.query(func.count(models.PreOrders.Order_id)).scalar()
        else:
            total_order_count = 0
        
        if db.query(func.count(models.PostOrders.Order_id)).scalar() != None:
            total_shipped_count = db.query(func.count(models.PostOrders.Order_id)).scalar()
        else:
            total_shipped_count = 0
            
        if total_shipped_count == None:
            total_shipped_count = 0
        orders_to_be_ship = total_order_count - total_shipped_count
        total_return_cases = db.query(func.count(models.Returns.is_resolved == False)).scalar()
        total_income = db.query(func.sum(models.PreOrders.Order_earning)).scalar()
        total_cost = db.query(func.sum(models.PostOrders.item_cost)).scalar()
        total_loss = db.query(func.sum(models.Returns.loss)).scalar()
        if total_cost == None:
            total_cost = 0
        if total_loss == None:
            total_loss = 0
        
        total_profit = total_income - (total_cost + total_loss)
        return {"total_order_count": total_order_count, "total_return_cases": total_return_cases, 
                "total_income": total_income, "total_loss": total_loss, "total_loss": total_loss,
                "total_profit": total_profit, "tobe_ship": orders_to_be_ship}
    except Exception as e:
        db.rollback()
        return {"total_order_count": 0, "total_return_cases": 0, "total_income": 0, "total_loss": 0, "total_loss": 0,
                "total_profit": 0, "tobe_ship": 0}
    


def get_await_shipments(db: Session):

    try:
        query = (select([models.PreOrders])
        .outerjoin(models.PostOrders, models.PreOrders.Order_id  == models.PostOrders.Order_id)
        .where(models.PostOrders.Order_id.is_(None))
        )
        await_shipments = db.query(query).all()
        return await_shipments
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error getting await shipments: {str(e)}")
    
    

        