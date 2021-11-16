from fastapi import FastAPI, Depends, File
from sqlalchemy.sql.functions import mode
import models.models
from models.models import Menu
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
import gcp

app = FastAPI()

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

def get_db():
    db = SessionLocal()
    #print(db)
    try:
        yield db
    finally:
        db.close()

@app.get("/menu/{menu_id}")
def get_menu(menu_id: int, db: SessionLocal = Depends(get_db)):
    # get menu
    #print(db)
    return {"menu_id": menu_id}

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

@app.post("/menu")
def create_menu(menu_id: int, resturant_name: str, db: SessionLocal = Depends(get_db)):
    # create menu object
    db_menu = Menu(id= menu_id, resturant_name=resturant_name)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return {"Created menu": menu_id}


@app.post("/dummy_order")
def dummy_order():
    return [
        ["fries", 2],
        ["coffee", 1],
    ]