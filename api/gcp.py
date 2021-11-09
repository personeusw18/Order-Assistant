from google.cloud import speech
from google.cloud import language_v1

def convert_audio_to_text(order_audio: bytes) -> str:
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=order_audio)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    response = client.recognize(config=config, audio=audio)
    order_text = ''
    for result in response.results:
        order_text += result.alternatives[0].transcript
    return order_text

def process_language(order: str):
    client = language_v1.LanguageServiceClient()
    document = {
        "content": order,
        "type_": language_v1.Document.Type.PLAIN_TEXT, 
        "language": "en"
    }
    response = client.analyze_entities(request = {
        'document': document, 
        'encoding_type': language_v1.EncodingType.UTF8
    })
    entities = []
    for entity in response.entities:
        entities.append(entity.name)
    return entities