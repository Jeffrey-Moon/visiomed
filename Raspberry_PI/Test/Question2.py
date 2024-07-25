import RPi.GPIO as gpio #라이브러리
import time #시간을 조절해줄수 있다.
# gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
gpio.setup(19, gpio.OUT) 
gpio.setup(20, gpio.OUT) 
 
try:
    while(True):
        gpio.output(18, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(18, gpio.LOW)
        time.sleep(0.5)
        
        gpio.output(19, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(19, gpio.LOW)
        time.sleep(0.5)
        
        gpio.output(20, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(20, gpio.LOW)
        time.sleep(0.5)

        
except KeyboardInterrupt:  
     gpio.cleanup() 
