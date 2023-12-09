from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Item(Base):
    __tablename__ = "Items_Table"
    Item_id = Column(String, primary_key=True, index=True)
    Item_link = Column(String)


class PreOrders(Base):
    __tablename__ = "PreOrders_Table"
    Order_id = Column(String, primary_key=True, index=True)
    Order_Date = Column(String)
    Order_earning = Column(Integer)
    Buyer_name = Column(String)
    Contact_number = Column(String)
    variation = Column(String, nullable=True)


class PostOrders(Base):
    __tablename__ = "PostOrders_Table"
    Order_id = Column(String, primary_key=True, index=True)
    Ali_order_id = Column(String)
    Tracking_number = Column(String)
    next_tracking_number = Column(String, nullable=True)
    item_cost = Column(Integer)


class Returns(Base):
    __tablename__ = "Returns_Table"
    Order_id = Column(String, primary_key=True, index=True)
    loss = Column(Integer)
    is_resolved = Column(Boolean)


