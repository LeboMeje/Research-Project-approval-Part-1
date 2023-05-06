#Research & Project approval (Part 1)


# Portfolio project
This is a presentation of portfolio project based on an IoT smart home system.

## Project:
IoT Smart Home System App

## Description:
Build an IoT smart home system that can control lights, temperature, and security.

## Technologies
* Raspberry Pi
* Pushbullet API
* Flask web framework
* 8-channel relay module
* Tested on Ubuntu 20.04 LTS

# How it works
This program is designed to:

Set up the Raspberry Pi and sensors. Connect the DHT11 temperature and humidity sensor and HC-SR501 PIR motion sensor to the Raspberry Pi's GPIO pins.
You'll need to download and install the Adafruit_DHT library to interface with the DHT11 sensor.
Control lights with the relay module.
Connect the 8-channel relay module to the Raspberry Pi's GPIO pins.
You can use the relay module to control lights or other appliances.
Send alerts to user's phone using the Pushbullet API.
Sign up for a free account on Pushbullet and create an access token.
You can then use the Pushbullet API to send alerts to your phone.
The app will consist of a Flask web server, temperature and humidity sensor, motion sensor, relay module, and a Pushbullet API for push notifications.


| Files |
| ----- |
| `temperature_humidity_sensor.py` |
| `motion_sensor.py` |
| `relay_controller.py` |
| `pushbullet_api.py` |
| `app.py` |
| `home.html` |
| `style.css` |

## Contributor
Lebohang Meje


