from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base, SessionLocal, engine
from sqlalchemy.exc import IntegrityError
import schemas
import crud_items
from fastapi.middleware.cors import CORSMiddleware


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