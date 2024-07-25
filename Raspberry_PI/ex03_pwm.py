#pulse width modulation 펄스폭 변조
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT)
p = gpio.PWM(18, 500) #1초에 같은 패턴을 500번 하겠다
p.start(0)

try:
    while(True):
        for i in range(0,101):
            p.ChangeDutyCycle(i)
            time.sleep(0.3)
        for i in range(100,-1,-1):
            p.ChangeDutyCycle(i)
            time.sleep(0.3)

        
except KeyboardInterrupt:  #ctrl+c가 KeyboardInterrupt기능이 활성화되고 만났을때 예외문 실행
     gpio.cleanup() #사용하면 setup된거 지워준다.
