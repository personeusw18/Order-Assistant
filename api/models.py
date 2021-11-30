from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float

from database import Base

class Restaurant(Base):

    __tablename__ = 'restaurants'

    # attributes
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    img = Column(String(300), nullable=False)

    # relationships
    menu_items = relationship('MenuItem', back_populates='restaurant', cascade="all, delete")
    identifiers = relationship('Identifier', back_populates='restaurant', cascade="all, delete")


class MenuItem(Base):

    __tablename__ = "menu_items"
    
    # attributes
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    desc = Column(String)
    price = Column(Float)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))

    # relationships
    restaurant = relationship('Restaurant' , back_populates='menu_items')
    identifiers = relationship('Identifier', back_populates='menu_item')

class Identifier(Base):

    __tablename__ = "identifiers"

    # attributes
    id = Column(Integer, primary_key=True, index=True)
    identifier = Column(String)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    
    # relationships
    restaurant = relationship('Restaurant' , back_populates='identifiers')
    menu_item = relationship('MenuItem' , back_populates='identifiers')
