from fastapi import FastAPI, Depends, File
from google.cloud import speech
from sqlalchemy.sql.functions import mode
import models.models
from models.models import Menu
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware

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

@app.post("/order")
def create_order(menu_id: int, order_audio: bytes = File(...), db: SessionLocal = Depends(get_db)):
    print(menu_id)
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=order_audio)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    print(response)
    return { 'order': [] }

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