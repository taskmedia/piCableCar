#!/bin/python
# this script will stop the servo spinning
# warning: script might not be working if server.py is running

import RPi.GPIO as GPIO
import time

# configuration
SERVO_GPIO_PIN = 17  # PIN to control the servo
SERVO_STOP = 2.5  # number to stop servo spinning

# set GPIO output pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_GPIO_PIN, GPIO.OUT)
p = GPIO.PWM(SERVO_GPIO_PIN, 50)

# stop
p.ChangeDutyCycle(SERVO_STOP)
time.sleep(1)

# exit program
p.stop()
GPIO.cleanup()
