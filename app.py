from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import requests

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)

DHT_PIN = 17
PIR_PIN = 11
RELAY_PIN = 12

GPIO.setup(DHT_PIN, GPIO.IN)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)

PUSHBULLET_API_KEY = "your-api-key"
PUSHBULLET_DEVICE_ID = "your-device-id"

@app.route("/")
def home():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
    if GPIO.input(PIR_PIN):
        motion_detected = True
    else:
        motion_detected = False
    context = {
        "temperature": temperature,
        "humidity": humidity,
        "motion_detected": motion_detected
    }
    return render_template("home.html", **context)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
