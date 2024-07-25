#gpio 18번 핀에 연결되어있는 LED ON/OFF 기능을 만들어보자
#그리고 이것을 모듈로 만들어서 쓰자. 어차피 계속 쓸거니깐
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)

def ledOn():
    gpio.output(18, gpio.HIGH)
    
def ledOff():
    gpio.output(18, gpio.LOW)
    
def ledClear():
    gpio.cleanup()