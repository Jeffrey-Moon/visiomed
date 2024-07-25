import RPi.GPIO as gpio #라이브러리
import time #시간을 조절해줄수 있다.
# gpio.cleanup()
gpio.setmode(gpio.BCM)
gpio.setup(18, gpio.OUT) #출력으로 사용하는 액츄에이터이다.
try:
    while(True):
        gpio.output(18, gpio.HIGH)
        time.sleep(0.5)
    
        gpio.output(18, gpio.LOW)
        time.sleep(0.5)

        
except KeyboardInterrupt:  #ctrl+c가 KeyboardInterrupt기능이 활성화되고 만났을때 예외문 실행
     gpio.cleanup() #사용하면 setup된거 지워준다.