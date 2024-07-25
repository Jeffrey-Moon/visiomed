import requests
import pygame
import serial
import RPi.GPIO as gpio
import time
import threading
from time import sleep

gpio.setmode(gpio.BCM)
# 마그네틱 setup
gpio.setup(23, gpio.IN)
gpio.setup(24, gpio.IN)
gpio.setup(25, gpio.IN)
gpio.setup(8, gpio.IN)
gpio.setup(7, gpio.IN)
gpio.setup(12, gpio.IN)
gpio.setup(16, gpio.IN)
gpio.setup(20, gpio.IN)

# warning setup
gpio.setup(5, gpio.IN)

# 초음파 setup
trig = 19
echo = 26

gpio.setwarnings(False)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
# 자신의 REST_API_KEY를 입력하세요!
# 카카오 tts api key
REST_API_KEY = "9bae2e4900e6999c19de206b14951015"
cnt = 0
check = False
# 카카오 tts mp3파일 저장 및 변환
class KakaoTTS:

    def __init__(self, text, API_KEY=REST_API_KEY):
        self.resp = requests.post(
            url="https://kakaoi-newtone-openapi.kakao.com/v1/synthesize",
            headers={
                "Content-Type": "application/xml",
                "Authorization": f"KakaoAK {API_KEY}"
            },
            data=f"<speak>{text}</speak>".encode('utf-8')
        )

    def save(self, filename="output.mp3"):
        with open(filename, "wb") as file:
            file.write(self.resp.content)

#NFC, 나머지 기능들
def speak(text):
    sound = text
    talk = f"<voice name='WOMAN_DIALOG_BRIGHT'>{sound}</voice>"
    if __name__ == '__main__':
        tts = KakaoTTS(talk)
        tts.save("speak.mp3")
        pygame.mixer.init()  
        pygame.mixer.music.load(f"/home/pi/Study/project/speak.mp3")
        
        pygame.mixer.music.play()
        
#보관함용
def casespeak(text):
    sound = text
    talk = f"<voice name='WOMAN_DIALOG_BRIGHT'>{sound}</voice>"
    if __name__ == '__main__':
        tts = KakaoTTS(talk)
        tts.save("casespeak.mp3")
        pygame.mixer.init()  
        pygame.mixer.music.load(f"/home/pi/Study/project/casespeak.mp3")
        pygame.mixer.music.play()


 
def NFC():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        speak(line)



# 아두이노 시리얼 통신
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
while True:
    if __name__ == '__main__':
        NFC()
    
    
    #gpio.output(trig, False)
    #time.sleep(0.0005)
    #gpio.output(trig, True)
    #time.sleep(0.0001)
    #gpio.output(trig, False)
    #while gpio.input(echo) == 0:
    #    pulse_start = time.time()    
    #while gpio.input(echo) == 1:
    #    pulse_end = time.time()
    #pulse_duration = pulse_end - pulse_start
    #distance = pulse_duration * 17000
    #distance = round(distance, 2)
    #if distance >50 and cnt == 0 :
    #    cnt = 9000
        
     #   print(f"Distance : {distance}cm")
        
    #elif distance < 50 and cnt == 9000 :
    #    cnt = 0
    #    print(f"Distance : {distance}cm")
    #    hi = "반갑습니다. 당신의 건강을 챙겨주는, 복순이 입니다."
    #    speak(hi)
    #    print(f"Distance : {distance}cm")
        
    # 마그네틱, 비상버튼
    mag1 = gpio.input(20)
    mag2 = gpio.input(16)
    mag3 = gpio.input(12)
    mag4 = gpio.input(7)
    mag5 = gpio.input(8)
    mag6 = gpio.input(25)
    mag7 = gpio.input(24)
    mag8 = gpio.input(23)
    time.sleep(0.5)
    if mag1 == 0 and cnt == 0:
        cnt = 1000
        print(f"mag1 = {mag1}")
        result = "1번, 보관함 입니다, 혈압약, 식후 30분 후, 복용하세요."
        casespeak(result)

    elif mag1 == 1 and cnt == 1000:
        cnt = 0
        print(f"mag1 = {mag1}")
        

    if mag2 == 0 and cnt == 0:
        cnt = 2000
        result = "2번, 보관함 입니다, 감기약, 식후 30분 후, 복용하세요."
        print(f"mag2 = {mag2}")
        casespeak(result)
                
    elif mag2 == 1 and cnt == 2000:
        cnt = 0
        print(f"mag2 = {mag2}")
        
    if mag3 == 0 and cnt == 0:
        cnt = 3000
        
        print(f"mag3 = {mag3}")
        result = "3번, 보관함 입니다, 독감약, 식후 30분 후, 복용하세요."
        casespeak(result)



    elif mag3 == 1 and cnt == 3000:
        cnt = 0
        print(f"mag3 = {mag3}")
        
    if mag4 == 0 and cnt == 0:
        cnt = 4000

        print(f"mag4 = {mag4}")
        result = "4번, 보관함 입니다, 혈압약, 식후 30분 후, 복용하세요."
        casespeak(result)
                
    elif mag4 == 1 and cnt == 4000:
        cnt = 0
        print(f"mag4 = {mag4}")
        
    if mag5 == 0 and cnt == 0:
        cnt = 5000
        print(f"mag5 = {mag5}")
        result = "5번, 보관함 입니다, 코로나약, 식후 30분 후, 복용하세요."
        casespeak(result)
        
    elif mag5 == 1 and cnt == 5000:
        cnt = 0
        print(f"mag5 = {mag5}")

    if mag6 == 0 and cnt == 0:
        cnt = 6000
        result = "6번, 보관함 입니다, 오미크론약, 식후 30분 후, 복용하세요."
        print(f"mag6 = {mag6}")
        casespeak(result)
        
    elif mag6 == 1 and cnt == 6000:
        cnt = 0
        print(f"mag6 = {mag6}")
    
    if mag7 == 0 and cnt == 0:
        cnt = 7000
        result = "7번, 상비약을, 보관하는, 보관함 입니다."
        print(f"mag7 = {mag7}")
        casespeak(result)
        
    elif mag7 == 1 and cnt == 7000:
        cnt = 0
        print(f"mag7 = {mag7}")
    
    if mag8 == 0 and cnt == 0:
        cnt = 8000
        result = "8번, 상비약을, 보관하는, 보관함 입니다."
        print(f"mag8 = {mag8}")
        casespeak(result)
        
    elif mag8 == 1 and cnt == 8000:
        cnt = 0
        print(f"mag8 = {mag8}")
    #NFC
#    if ser.in_waiting > 0:
#        line = ser.readline().decode('utf-8').rstrip()
#        print(line)
#        speak(line)
    #<voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice>
    #<voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice>
    #<voice name="WOMAN_DIALOG_BRIGHT"> 안녕하세요. 여성 밝은 대화체예요.</voice>
    #<voice name="MAN_DIALOG_BRIGHT"> 안녕하세요. 남성 밝은 대화체예요.</voice>
        #init
    warning = gpio.input(5)
    time.sleep(0.5)
     #비상버튼
    if warning == 1 and cnt == 0:
        cnt = 10000
        print(f"warning = {warning}")
            
                    #init
        pygame.mixer.init()
     
                #load file
        pygame.mixer.music.load("/home/pi/Study/project/sirr.mp3")
     
                #play
        pygame.mixer.music.play(-1)
        
    elif warning == 0 and cnt == 10000:
        cnt = 0
        print(f"warning = {warning}")
        pygame.mixer.quit()

