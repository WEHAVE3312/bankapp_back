import os
from belvo.client import Client
from dotenv import load_dotenv

load_dotenv()

def configure_belvo() -> Client:
    secret_id = os.environ.get("BELVO_SECRET_ID_PROD")
    secret_password = os.environ.get("BELVO_SECRET_PASSWORD_PROD")
    belvo_client = Client(secret_id, secret_password,"development")
    return belvo_client
