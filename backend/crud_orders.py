from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import models


def add_order(db: Session, Order_id: str, 
              Date: str, Ali_order_id: str, 
              Order_earning: str,
              Buyer_name: str, Contact_number: str,
              Tracking_number: str):
    try:
        db_item = models.Orders(Order_id=Order_id, 
                                Date=Date, 
                                Ali_order_id=Ali_order_id,
                                Order_earning=Order_earning, 
                                Buyer_name=Buyer_name, 
                                Contact_number=Contact_number,
                                Tracking_number=Tracking_number)
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
