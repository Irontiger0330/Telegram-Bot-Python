import os

import requests
from dotenv import load_dotenv
load_dotenv()

# Use your API key
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')

def sendMessage(sender_id: int, message: str) -> None:

    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"

    payload = {
        "chat_id": sender_id,
        "text": message
    }
    headers = {"Content-Type": "application/json"}

    requests.request("POST", url, json=payload, headers=headers)

def sendPhoto(sender_id: int, photo_url: str, caption: str = '') -> None:

    url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendPhoto"

    payload = {
        "chat_id": sender_id,
        "photo": photo_url,
        "caption": caption
    }
    headers = {"Content-Type": "application/json"}

    requests.request("POST", url, json=payload, headers=headers)