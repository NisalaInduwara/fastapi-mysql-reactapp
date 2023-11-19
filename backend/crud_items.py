from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
import models


def create_item(db: Session, Item_id: str, Item_link: str):
    try:
        db_item = models.Item(Item_id=Item_id, Item_link=Item_link)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    except IntegrityError as e:
        db.rollback()
        raise Exception(f"Item creation failed: IntegrityError - Duplicate Item_id {str(e)}")
    
    except Exception as e:
        db.rollback()
        raise Exception(f"Item creation failed: An error occurred {str(e)}")
    

def get_item_link_by_id(db: Session, Item_id: str):
    try:
        item = db.query(models.Item).filter(models.Item.Item_id == Item_id).first()
        if item: 
            return item.Item_link
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating item: {str(e)}")
    

def update_link(db: Session, Item_id: str, new_link:str):
    try:
        item = db.query(models.Item).filter(models.Item.Item_id == Item_id).first()
        if item:
            item.Item_link = new_link
            db.commit()
            db.refresh(item)
            return {"Id": item.Item_id, "Updated_link" : item.Item_link}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating item: {str(e)}")
    
    
def delete_item(db: Session, Item_id: str):
    try:
        item = db.query(models.Item).filter(models.Item.Item_id == Item_id).first()
        if item:
            db.delete(item)
            db.commit()
            return {"Id": item.Item_id, "Link": item.Item_link}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting items: {str(e)}")


def get_items_count(db: Session):
    try:
        total_count = db.query(func.count(models.Item.Item_id)).scalar()
        return {"total_count": total_count}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error retrieving items: {str(e)}")

