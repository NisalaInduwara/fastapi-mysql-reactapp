from pydantic import BaseModel

class ItemCreate(BaseModel):
    Item_id: str
    Item_link: str


class OrderCreated(BaseModel):
    Order_id: str
    Date: str
    Ali_order_id: str
    Order_earning: int
    Buyer_name: str
    Contact_number: str

class DisputeCreate(BaseModel):
    Order_id: str
    loss: int