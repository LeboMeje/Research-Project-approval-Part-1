import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)

DHT_PIN = 17

GPIO.setup(DHT_PIN, GPIO.IN)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temperature: {:.1f}°C, Humidity: {:.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from DHT11 sensor")
    time.sleep(1)
