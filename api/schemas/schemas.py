from pydantic import BaseModel

class Menu(BaseModel):
    id: int
    resturant_name: str

    class Config:
        orm_mode = True
