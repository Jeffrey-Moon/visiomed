import RPi.GPIO as gpio #라이브러리
import time #시간을 조절해줄수 있다.
gpio.setmode(gpio.BCM)  #이름으로 읽어올거기 때문에 BCM
gpio.setup(20, gpio.IN) #출력으로 사용하는 액츄에이터이다.
gpio.setup(21, gpio.IN) #출력으로 사용하는 액츄에이터이다.
gpio.setup(6, gpio.OUT) #출력으로 사용하는 액츄에이터이다.
gpio.setup(18, gpio.OUT) #출력으로 사용하는 액츄에이터이다.
# gpio.cleanup() #사용하면 setup된거 지워준다.
    
try:
    while(True):
        btn1 = gpio.input(21)
        btn2 = gpio.input(20)
        
        if(btn1 == 1):
            gpio.output(6, gpio.HIGH)
        elif(btn1 == 0):
            gpio.output(6, gpio.LOW)
        if(btn2 == 1):
            gpio.output(18, gpio.HIGH)
        elif(btn2 == 0):
            gpio.output(18, gpio.LOW)
        
except KeyboardInterrupt:  #ctrl+c가 KeyboardInterrupt기능이 활성화되고 만났을때 예외문 실행
     gpio.cleanup() #사용하면 setup된거 지워준다.
