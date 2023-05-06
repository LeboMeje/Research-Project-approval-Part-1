import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

RELAY_PIN = 12

GPIO.setup(RELAY_PIN, GPIO.OUT)

while True:
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAY_PIN, GPIO.LOW)
    time.sleep(1)
