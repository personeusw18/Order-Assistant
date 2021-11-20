from typing import List

from fastapi import FastAPI, Depends, File
from fastapi.middleware.cors import CORSMiddleware

import crud, models, schemas
from database import SessionLocal, engine
import gcp

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=engine)

# cores setup
origins = [
    "http://localhost:3000",
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

@app.post("/order/audio")
def create_audio_order(menu_id: int, order_audio: bytes = File(...), db: SessionLocal = Depends(get_db)):
    order_text = gcp.convert_audio_to_text(order_audio)
    processed_language = gcp.process_language(order_text)
    # TODO: convert processed language to order
    return { 'order': processed_language }

@app.post("/order/text")
def create_text_order(menu_id: int, order_text: str, db: SessionLocal = Depends(get_db)):
    processed_language = gcp.process_language(order_text)
    # TODO: convert processed language to order
    return { 'order': processed_language }

@app.post('/reset_database')
def reset_database(db: SessionLocal = Depends(get_db)):
    crud.reset_db(db)