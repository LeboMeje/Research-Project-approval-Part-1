import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIR_PIN = 11

GPIO.setup(PIR_PIN, GPIO.IN)

while True:
    if GPIO.input(PIR_PIN):
        print("Motion detected!")
    else:
        print("No motion detected")
    time.sleep(1)
