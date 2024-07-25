import ex04_spidevRead as sr 
import led

try:
    while(True):
        readData = sr.analog_read(0)
        print(readData)
    
        if(readData <=450):
            led.ledOn();
        else:
            led.ledOff();

        
except KeyboardInterrupt:  #ctrl+c가 KeyboardInterrupt기능이 활성화되고 만났을때 예외문 실행
     led.ledClear() #사용하면 setup된거 지워준다.