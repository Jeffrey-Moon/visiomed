import RPi.GPIO as gpio #라이브러리
import time #시간을 조절해줄수 있다.
gpio.setmode(gpio.BCM)  #이름으로 읽어올거기 때문에 BCM
gpio.setup(20, gpio.IN) #출력으로 사용하는 액츄에이터이다.
gpio.setup(21, gpio.IN) #출력으로 사용하는 액츄에이터이다.
gpio.setup(18, gpio.OUT) #출력으로 사용하는 액츄에이터이다.
p = gpio.PWM(18, 500) #1초에 같은 패턴을 500번 하겠다
p.start(0)

try:
    while(True):
        btn1 = gpio.input(21)
        btn2 = gpio.input(20)
        
        if(btn1 == 1):
            p.ChangeDutyCycle(50)
            time.sleep(0.3)
        if(btn2 == 1):
            p.ChangeDutyCycle(100)
            time.sleep(0.3)
        
except KeyboardInterrupt:  #ctrl+c가 KeyboardInterrupt기능이 활성화되고 만났을때 예외문 실행
     gpio.cleanup() #사용하면 setup된거 지워준다.

