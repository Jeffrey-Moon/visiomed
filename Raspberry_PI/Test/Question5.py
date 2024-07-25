from flask import Flask
app = Flask(__name__)

import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

@app.route("/") #여기는 uri, 기본경로 설정
def Hello():
    return "Hello World" #여기는 uri, 기본경로 설정


@app.route("/led/on")
def Ledon():
    gpio.output(18, gpio.HIGH)
    return "led on"

@app.route("/led/off")
def Ledoff():
    gpio.output(18, gpio.LOW)
    return "led off"

if __name__ == "__main__":
    app.run(host="localhost")