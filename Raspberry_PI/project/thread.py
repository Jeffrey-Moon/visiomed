import threading
from time import sleep

def hello_1():
	while True:
		print("1")
		time.sleep(60)
		text= res.text
		speak(text)


def hello_1_thread():
	thread=threading.Thread(target=hello_1) #thread를 동작시킬 함수를 target 에 대입해줍니다
	thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
	thread.start() #thread를 시작합니다

if __name__ == "__main__":
	hello_1_thread()
	
	
	
	
	    # 초음파
    gpio.output(trig, False)
    time.sleep(1)
    gpio.output(trig, True)
    time.sleep(1)
    gpio.output(trig, False)
    while gpio.input(echo) == 0:
        pulse_start = time.time()
            
    while gpio.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    if distance < 500  and cnt == 0 :
        cnt = 9000
        hi = "반갑습니다. 당신의 건강을 챙겨주는, 닥터, 복순이 입니다."
        speak(hi)
        print(f"Distance : {distance}cm")
        
    elif distance > 500 and cnt == 9000 :
        cnt = 0
        print(f"Distance : {distance}cm")
    
    

