import requests

PUSHBULLET_API_KEY = "your-api-key"
PUSHBULLET_DEVICE_ID = "your-device-id"

def send_push_notification(title, message):
    headers = {
        "Access-Token": PUSHBULLET_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
