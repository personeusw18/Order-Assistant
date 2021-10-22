from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float

from database import Base

class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    resturant_name = Column(String, unique=True, index=True)

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    name = Column(String)
    resturant_id = Column(Integer, ForeignKey("menus.id"))


    
