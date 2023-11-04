from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Item(Base):
    __tablename__ = "items"

    Item_id = Column(String, primary_key=True, index=True)
    Item_link = Column(String)


class Orders(Base):
    __tablename__ = "orders"

    Order_id = Column(String, primary_key=True, index=True)
    Ali_order_id = Column(String, primary_key=True, nullable=True)
    Item_id = Column(String, ForeignKey("items.Item_id"))
    Tracking_number = Column(String, unique=True, nullable=True)
    Order_earning = Column(String)
    Buyer_name = Column(String)
    Address = Column(String)
    Contact_number = Column(String)    


class Disputes(Base):
    __tablename__ = "Disputes"

    dispute_ebay_id = Column(String, primary_key=True, index=True)
    loss = Column(String)
