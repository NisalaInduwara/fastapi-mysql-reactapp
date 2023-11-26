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
async def get_items_count(db: Session = Depends(get_db)):
    total_count = crud_items.get_items_count(db)
    return {"total_count": total_count['total_count']}

@app.put("/update_item_link/")
async def update_item(Item_id: str, new_link: str, db: Session = Depends(get_db)):
    updated_item = crud_items.update_link(db, Item_id, new_link)
    return updated_item

@app.delete("/delete_item/")
async def delete_item(Item_id: str, db: Session = Depends(get_db)):
    deleted_item = crud_items.delete_item(db, Item_id)
    return deleted_item

# order tables methods
@app.post("/add_orders/")
async def add_order(Order_id: str, Date: str, Ali_order_id: str, Order_earning: int, 
                    Item_cost: int, Buyer_name: str, Contact_number: str, 
                    Tracking_number: str, next_tracking_number: Optional[str]=None, 
                    return_case: Optional[bool]=False, loss: Optional[int]=None, 
                    db: Session = Depends(get_db)):
    
    added_order = crud_orders.add_order(db, Order_id, Date, Ali_order_id, Order_earning,
                                        Item_cost, Buyer_name, Contact_number, Tracking_number,
                                        next_tracking_number, return_case, loss)
    return added_order

@app.get('/get_order_data/')
async def get_order_data(Order_id: Optional[str]=None, 
                  Tracking_number: Optional[str]=None, Ali_order_id: Optional[str]=None,
                  db: Session = Depends(get_db)):
    order_data = crud_orders.get_order_data(db, Order_id, Tracking_number, Ali_order_id)
    return order_data
    
@app.get("/track_order/")
async def track_order(Order_id: str, db: Session = Depends(get_db)):
    return crud_orders.track_order(db, Order_id)

@app.delete("/delete_order/")
async def delete_order(Order_id: str, db: Session = Depends(get_db)):
    return crud_orders.delete_order(db, Order_id)

@app.get("/get_contact_details/")
async def get_contact_details(Date: str, db: Session = Depends(get_db)):
    return crud_orders.get_contact_details(db, Date)

@app.put("/add_next_tracking_number/")
async def add_next_tracking_number(next_tracking_number: str, Order_id: Optional[str]=None, 
                             Tracking_number: Optional[str]=None, db: Session = Depends(get_db)):
    return crud_orders.add_next_tracking_number(db, next_tracking_number, Order_id, Tracking_number)

@app.put("/open_return_case")
async def open_return_case(Order_id: str, loss: int, return_case: bool, db: Session = Depends(get_db)):
    return crud_orders.open_return_case(db, Order_id, loss, return_case)

@app.put("/resolve_return/")
async def resolve_return(Order_id: str, return_case: bool, recovery_amount: int, 
                         db: Session = Depends(get_db)):
    return crud_orders.resolve_return_case(db, Order_id, return_case, recovery_amount)

@app.get("/get_counts/")
async def get_counts(db: Session = Depends(get_db)):
    return crud_orders.get_counts(db)


    
    

