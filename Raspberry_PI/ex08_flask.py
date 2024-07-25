import led
import ex07_select as slt
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/") #여기는 uri, 기본경로 설정
def Hello():
    return render_template('main.html') 

@app.route("/led/on")
def Ledon():
    led.ledOn()
    return "led on"

@app.route("/led/off")
def Ledoff():
    led.ledOff()
    return "led off"

@app.route("/select")
def select():
    r = slt.select_sensordb()
    return r

if __name__ == "__main__":
    app.run(host='192.168.8.104')