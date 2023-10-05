#!/bin/python
# this script will run a web server to control the servo of the cable car


from flask import Flask, send_from_directory
import RPi.GPIO as GPIO
import time

# configuration
SERVER_PORT = 80

SERVO_GPIO_PIN = 17

SERVO_CLOCKWISE = 4  # downhill
SERVO_COUNTERCLOCKWISE = 2  # uphill
SERVO_STOP = 2.5  # stop

# webserver
app = Flask(__name__)
HTML_PAGE = open("src/index.html", "r").read()


@app.route("/")
# website: home
def html_home():
    return HTML_PAGE


@app.route('/img/<path:path>')
# website: images
def html_src(path):
    return send_from_directory('src/img', path)


@app.route("/up")
# website: servo actions - up
def html_up():
    servo_action(SERVO_COUNTERCLOCKWISE)
    return HTML_PAGE


@app.route("/down")
# website: servo actions - down
def html_down():
    servo_action(SERVO_CLOCKWISE)
    return HTML_PAGE


@app.route("/stop")
# website: servo actions - stop
def html_stop():
    servo_action(SERVO_STOP)
    return HTML_PAGE


@app.route('/<path:path>')
# website: catchall - redirect to home
def html_catchall(path):
    return '<meta http-equiv="refresh" content="1; url=/" />'


# function to control servo action
def servo_action(action=SERVO_STOP):
    print("servo action: " + str(action))
    p.ChangeDutyCycle(action)
    time.sleep(0.1)


# set GPIO output pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_GPIO_PIN, GPIO.OUT)
p = GPIO.PWM(SERVO_GPIO_PIN, 50)

# stop servo when started
p.start(SERVO_STOP)


try:
    app.run(host="0.0.0.0", port=SERVER_PORT)
    # stop servo when webserver stopped
    servo_action(SERVO_STOP)
except KeyboardInterrupt:
    # stop servo when script is stopped
    servo_action(SERVO_STOP)
