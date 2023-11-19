from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Item(Base):
    __tablename__ = "items"
    Item_id = Column(String, primary_key=True, index=True)
    Item_link = Column(String)


class Orders(Base):
    __tablename__ = "orders"
    Order_id = Column(String, primary_key=True, index=True)
    Date = Column(String)
    Ali_order_id = Column(String)
    Order_earning = Column(Integer)
    Buyer_name = Column(String)
    Contact_number = Column(String)
    Tracking_number = Column(String)   


class Disputes(Base):
    __tablename__ = "disputes"
    dispute_order_id = Column(String, primary_key=True, index=True)
    loss = Column(Integer)

