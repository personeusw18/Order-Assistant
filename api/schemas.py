from typing import List
from pydantic import BaseModel

class MenuItemBase(BaseModel):
    id: int
    price: float
    name: str
    desc: str

    class Config:
        orm_mode = True

class RestaurantBase(BaseModel):
    id: int
    name: str
    img: str

    class Config:
        orm_mode = True

class Restaurant(RestaurantBase):
    menu_items: List[MenuItemBase] = []

    class Config:
        orm_mode = True

class OrderAudio(BaseModel):
    restaurant_id: int
    audio: bytes

class OrderText(BaseModel):
    restaurant_id: int
    text: str