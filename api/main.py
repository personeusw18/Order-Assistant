from typing import List

from fastapi import FastAPI, Depends, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine
import helpers
import gcp

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=engine)

# cores setup
origins = [
    "http://localhost:3000",
    "https://orderassistant.netlify.app",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/restaurant/{restaurant_id}", response_model=schemas.Restaurant)
def get_restaurant(restaurant_id: int, db: SessionLocal = Depends(get_db)):
    restauraunt = crud.get_restaurant(db, restaurant_id)
    return restauraunt

@app.get("/restaurant/", response_model=List[schemas.RestaurantBase])
def get_restaurants(db: SessionLocal = Depends(get_db)):
    restauraunts = crud.get_restaurants(db)
    return restauraunts

@app.post("/order/audio/{restaurant_id}")
def create_audio_order(restaurant_id: int, order_audio: bytes = File(...), db: SessionLocal = Depends(get_db)):
    order_text = gcp.convert_audio_to_text(order_audio)
    entities = gcp.get_entities(order_text)
    identifiers = crud.get_identifiers(db, restaurant_id)
    menu_item_ids = helpers.get_menu_items_in_order(identifiers, entities)
    menu_items = crud.get_menu_items(db, menu_item_ids)
    subtotal, taxes, total = helpers.get_cost(menu_items)
    return { 'order': menu_items, 'subtotal': subtotal, 'taxes': taxes, 'total': total }

@app.post("/order/text/{restaurant_id}")
def create_text_order(restaurant_id: int, order_text: str, db: SessionLocal = Depends(get_db)):
    entities = gcp.get_entities(order_text)
    identifiers = crud.get_identifiers(db, restaurant_id)
    menu_item_ids = helpers.get_menu_items_in_order(identifiers, entities)
    menu_items = crud.get_menu_items(db, menu_item_ids)
    subtotal, taxes, total = helpers.get_cost(menu_items)
    return { 'order': menu_items, 'subtotal': subtotal, 'taxes': taxes, 'total': total }

@app.post('/reset_database')
def reset_database(db: SessionLocal = Depends(get_db)):
    crud.reset_db(db)