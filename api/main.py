from fastapi import FastAPI, Depends, File
from google.cloud import speech

from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/menu/{menu_id}")
def create_menu(menu_id: int, db: SessionLocal = Depends(get_db)):
    # get menu
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