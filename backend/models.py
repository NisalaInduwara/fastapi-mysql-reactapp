from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Item(Base):
    __tablename__ = "items"
    Item_id = Column(String, primary_key=True, index=True)
    Item_link = Column(String)


class PreOrders(Base):
    __tablename__ = "pre_orders"
    Order_id = Column(String, primary_key=True, index=True)
    Order_Date = Column(String)
    Order_earning = Column(Integer)
    Buyer_name = Column(String)
    Contact_number = Column(String)
    variation = Column(String, nullable=True)


class PostOrders(Base):
    __tablename__ = "post_orders"
    Order_id = Column(String, primary_key=True, index=True)
    Ali_order_id = Column(String)
    Tracking_number = Column(String)
    next_tracking_number = Column(String, nullable=True)


class Returns(Base):
    __tablename__ = "make_returns"
    Order_id = Column(String, primary_key=True, index=True)
    loss = Column(Integer)
    is_resolved = Column(Boolean)


