from fastapi import FastAPI
from pydantic import BaseSettings, Field

# Set up env vars
class Settings(BaseSettings):
    type: str = Field('', env='type')
    project_id: str = Field('', env='project_id')
    private_key_id: str = Field('', env='private_key_id')
    private_key: str = Field('', env='private_key')
    client_email: str = Field('', env='client_email')
    client_id: str = Field('', env='client_id')
    auth_uri: str = Field('', env='auth_uri')
    token_uri: str = Field('', env='token_uri')
    auth_provider_x509_cert_url: str = Field('', env='auth_provider_x509_cert_url')
    client_x509_cert_url: str = Field('', env='client_x509_cert_url')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
