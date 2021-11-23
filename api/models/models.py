from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Float
from database import Base
from database import Base, engine


class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    resturant_name = Column(String, unique=True, index=True)


#class MenuItem(Base):
#    __tablename__ = "menu_items"
#    id = Column(Integer, primary_key=True, index=True)
#    price = Column(Float)
#    name = Column(String)
#    resturant_id = Column(Integer, ForeignKey("menus.id"))


class Restaurants(Base):
    __tablename__ = "restaurants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Addons(Base):
    __tablename__ = "addons"
    id = Column(Integer, primary_key=True, index=True)
    is_standalone = Column(Boolean)
    name = Column(String)
    add_on_price = Column(Integer)
    menu_id = Column(Integer, ForeignKey('menus.id'))


class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    price = Column(Integer)
    menu_id = Column(Integer, ForeignKey('menus.id'))


class Identifiers(Base):
    __tablename__ = "identifiers"
    identifier = Column(String, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id'))


#class AddonItemsMap(Base):
#    __tablename__ = "addonitemsmap"
    #item_id = Column(Integer, ForeignKey('items.id'))
    #addon_id = Column(Integer, ForeignKey('addons.id'))

Base.metadata.create_all(engine)