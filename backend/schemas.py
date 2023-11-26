from pydantic import BaseModel


class ItemCreate(BaseModel):
    Item_id: str
    Item_link: str

class PreOrderCreate(BaseModel):
    Order_id: str
    Order_Date: str
    Order_earning: int
    Buyer_name: str
    Contact_number: str
    variation: str

class PostOrderCreate(BaseModel):
    Order_id: str
    Ali_order_id: str
    Tracking_number: str
    next_tracking_number: str

class ReturnCreate(BaseModel):
    Order_id: str
    loss: int
    is_resolved: bool


