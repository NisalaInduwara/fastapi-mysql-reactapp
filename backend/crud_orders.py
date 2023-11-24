from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import models
from typing import Optional


def add_order(db: Session, Order_id: str, 
              Date: str, Ali_order_id: str, 
              Order_earning: int,
              Item_cost: int,
              Buyer_name: str, Contact_number: str,
              Tracking_number: str,
              next_tracking_number: Optional[str]=None,
              return_case: Optional[bool]=False,
              loss: Optional[int]=None):
    try:
        Order_earning = Order_earning - Item_cost
        db_item = models.Orders(Order_id=Order_id, 
                                Date=Date, 
                                Ali_order_id=Ali_order_id,
                                Order_earning=Order_earning, 
                                Buyer_name=Buyer_name, 
                                Contact_number=Contact_number,
                                Tracking_number=Tracking_number,
                                next_tracking_number=next_tracking_number,
                                return_case=return_case,
                                loss=loss)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    except IntegrityError as e:
        db.rollback()
        raise Exception(f"Order adding failed: IntegrityError - Duplicate Order ID {str(e)}")
    
    except Exception as e:
        db.rollback()
        raise Exception(f"Order adding failed: An error occurred {str(e)}")


def get_oder_data(db: Session, Order_id: Optional[str]=None, 
                  Tracking_number: Optional[str]=None, Ali_order_id: Optional[str]=None):
    try:
        if Order_id != None:
            order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        elif Tracking_number != None:
            order = db.query(models.Orders).filter(models.Orders.Tracking_number==Tracking_number or 
                                                   models.Orders.next_tracking_number==Tracking_number).first()
        elif Ali_order_id != None:
            order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        else:
            raise HTTPException(status_code=422, detail="Invalid Input")
        
        if order:
            return {"Order_id": order.Order_id,
                    "Date": order.Date,
                    "Ali_order_id": order.Ali_order_id,
                    "Order_earning": order.Order_earning,
                    "Buyer_name": order.Buyer_name,
                    "Contact_number": order.Contact_number,
                    "Tracking_number": order.Tracking_number,
                    "next_tracking_number": order.next_tracking_number,
                    "return_case": order.return_case,
                    "loss": order.loss}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error fetching order details: {str(e)}")


def track_order(db: Session, Order_id: str):

    try:
        order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        if order:
            tracking_number = order.Tracking_number
            next_tracking_number = order.next_tracking_number
            if next_tracking_number:
                return {'tracking_number': next_tracking_number}
            else:
                return {'tracking_number': tracking_number}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error fetching tracking number: {str(e)}")


def delete_order(db: Session, Order_id: str):

    try: 
        order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        if order:
            db.delete(order)
            db.commit()
            return {'Order_di': order.Order_id, 'Tracking_number': order.Tracking_number}
        else:
            raise HTTPException(status_code=404, detail="Order not found")
        
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting items: {str(e)}")
    
    
def get_contact_details(db: Session, Date: str):

    try:
        contact_data = db.query(models.Orders.Order_id, models.Orders.Buyer_name, 
                                models.Orders.Contact_number).filter(models.Orders.Date==Date)
        if contact_data:
            return contact_data
        else:
            raise HTTPException(status_code=404, detail="No contact data found")
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting items: {str(e)}")
    

def add_next_tracking_number(db: Session, next_tracking_number: str, Order_id: Optional[str]=None, 
                             Tracking_number: Optional[str]=None):

    try:
        if Order_id != None:
            order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        elif Tracking_number != None:
            order = db.query(models.Orders).filter(models.Orders.Tracking_number == Tracking_number).first()
        else:
            raise HTTPException(status_code=422, detail="Invalid Input")
        
        if order:
            order.next_tracking_number = next_tracking_number
            db.commit()
            db.refresh(order)
            return {"Id": order.Order_id, "next_tracking_number" : order.next_tracking_number}
        else:
            raise HTTPException(status_code=404, detail="No order data found")
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding next tracking number: {str(e)}")
    

def open_return_case(db: Session, Order_id: str, loss: int, return_case: bool):

    try:
        order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        if order:
            order.return_case = return_case
            order.loss = loss
            db.commit()
            db.refresh(order)
            return {"Id": order.Item_id, "loss" : order.loss}
        else:
            raise HTTPException(status_code=404, detail="No order data found")
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error opening return cases: {str(e)}")
    

def resolve_return_case(db: Session, Order_id: str, return_case: bool, recovery_amount: int):

    try:
        order = db.query(models.Orders).filter(models.Orders.Order_id == Order_id).first()
        loss = order.loss
        


    

def get_counts(db: Session):
    
    try:
        total_order_count = db.query(func.count(models.Orders.Order_id)).scalar()
        total_return_cases = db.query(func.count(models.Orders.return_case == True)).scalar()
        total_income = db.query(func.sum(models.Orders.Order_earning)).scalar()
        total_loss = db.query(func.sum(models.Orders.loss)).scalar()
        return {"total_order_count": total_order_count, "total_return_cases": total_return_cases, 
                "total_income": total_income, "total_loss": total_loss}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error total number of orders: {str(e)}")
    
    

        