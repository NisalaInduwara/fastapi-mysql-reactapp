from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException

import models


# CRUD functions for items table
def create_item(db: Session, Item_id: str, Item_link: str):
    try:
        db_item = models.Item(Item_id=Item_id, Item_link=Item_link)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError as e:
        db.rollback()
        raise Exception("Item creation failed: IntegrityError - Duplicate Item_id")
    except Exception as e:
        db.rollback()
        raise Exception("Item creation failed: An error occurred")
    

def get_item_link_by_id(db: Session, Item_id: str):
    try:
        item = db.query(models.Item).filter(models.Item.Item_id == Item_id).first()
        return item.Item_link
    except:
        db.rollback()
        raise HTTPException(status_code=404, detail="Item not found")
    

def update_link(db: Session, Item_id: str, new_link:str):
    try:
        item = db.query(models.Item).filter(models.Item.Item_id == Item_id).first()
        item.Item_link = new_link
        db.commit()
        db.refresh(item)
        return {"Id": item.Item_id, "Updated_link" : item.Item_link}
    except:
        db.rollback()
        raise HTTPException(status_code=404, detail="Item not found")
    
    
def delete_item(db: Session, Item_id: str):
    try:
        item = db.query(models.Item).filter(models.Item.Item_id == Item_id).first()
        db.delete(item)
        db.commit()
        return {"Id": item.Item_id, "Link": item.Item_link}
    except:
        db.rollback()
        raise HTTPException(status_code=404, detail="Item not found")



# CRUD functions for order
def create_item(db: Session, Item_id: str, Item_link: str):
    try:
        db_item = models.Item(Item_id=Item_id, Item_link=Item_link)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError as e:
        db.rollback()
        raise Exception("Item creation failed: IntegrityError - Duplicate Item_id")
    except Exception as e:
        db.rollback()
        raise Exception("Item creation failed: An error occurred")