from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base, SessionLocal, engine
from sqlalchemy.exc import IntegrityError
import schemas
import crud_items
import crud_orders
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional


Base.metadata.create_all(bind=engine)
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# item table methods
@app.post("/add_item/")
async def add_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    item = crud_items.create_item(db, Item_id=item.Item_id, Item_link=item.Item_link)
    return {"ID": item.Item_id, "Link": item.Item_link}


@app.get("/get_item_link/")
async def get_item(Item_id: str, db: Session = Depends(get_db)):
    link = crud_items.get_item_link_by_id(db, Item_id=Item_id)
    return {"Link": link}

@app.get("/items/")
async def get_items(db: Session = Depends(get_db)):
    return crud_items.get_items(db)

@app.put("/update_item_link/")
async def update_item(Item_id: str, new_link: str, db: Session = Depends(get_db)):
    updated_item = crud_items.update_link(db, Item_id, new_link)
    return updated_item

@app.delete("/delete_item/")
async def delete_item(Item_id: str, db: Session = Depends(get_db)):
    deleted_item = crud_items.delete_item(db, Item_id)
    return deleted_item

# order tables methods
@app.post("/add_pre_orders/")
async def add_order(order: schemas.PreOrderCreate, db: Session = Depends(get_db)):
    try:
        added_order = crud_orders.add_pre_order(db, order.Order_id, order.Order_Date, order.Order_earning,
                                            order.Buyer_name, order.Contact_number, order.variation)
        return added_order
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    

@app.post("/add_post_orders/")
async def add_order(order: schemas.PostOrderCreate, db: Session = Depends(get_db)):
    try:
        added_order = crud_orders.add_post_order(db, order.Order_id, order.Ali_order_id, order.Tracking_number,
                                            order.next_tracking_number, order.item_cost)
        return added_order
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@app.post("/make_return/")
async def make_return(order: schemas.ReturnCreate, db: Session = Depends(get_db)):
    try:
        added_order = crud_orders.make_return_case(db, order.Order_id, order.loss, order.is_resolved)
        return added_order
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    

@app.get('/get_preorder_data/')
async def get_preorder_data(Order_id: str, db: Session = Depends(get_db)):
    order_data = crud_orders.get_preorder_data(db, Order_id)
    return order_data


@app.get('/get_postorder_data/')
async def get_postorder_data(Order_id: str, Ali_order_id: str, 
                            Tracking_number: str, db: Session = Depends(get_db)):
    order_data = crud_orders.get_preorder_data(db, Order_id, Ali_order_id, Tracking_number)
    return order_data

    
@app.get("/get_tracking_link/")
async def track_order(Order_id: str, db: Session = Depends(get_db)):
    return crud_orders.get_tracking_link(db, Order_id)


@app.delete("/delete_order/")
async def delete_order(Order_id: str, db: Session = Depends(get_db)):
    return crud_orders.delete_order(db, Order_id)


@app.get("/get_contact_details/")
async def get_contact_details(Order_Date: str, db: Session = Depends(get_db)):
    return crud_orders.get_contact_details(db, Order_Date)


@app.put("/add_next_tracking_number/")
async def add_next_tracking_number(next_tracking_number: str, Tracking_number: Optional[str]=None, db: Session = Depends(get_db)):
    return crud_orders.add_next_tracking_number(db, next_tracking_number, Tracking_number)


@app.put("/resolve_return/")
async def resolve_return(Order_id: str, ali_refund: int, db: Session = Depends(get_db)):
    return crud_orders.resolve_return_case(db, Order_id, ali_refund)

@app.get("/get_counts/")
async def get_counts(db: Session = Depends(get_db)):
    return crud_orders.get_counts(db)


    
    

