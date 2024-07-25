import requests
import pygame
import serial
import RPi.GPIO as gpio
import time
import threading
from time import sleep
from pyfcm import FCMNotification

APIKEY = "AAAAm-rcRzY:APA91bH1jaUT9p8SK3y_7QOSMNSsxiRqxfwcUMIfb4NaVJof139bl4QPwNgCIht1jidBxdf9-KEPgPhpBmMxE9Tkz1EGjEVfCPVeG_wduAyqbrFfDxIkWr2DFW2HqGdalg3b010qAQ1h"
TOKEN = "eA-owhgsR4mBHrAz_ABwHl:APA91bHnmvAzTE5X6uQS9InCra-U8XfmFd5-abaap4C8FL-R3I4Wrgk8WJrrKIp9Jb86fAXeZ0c0z8206YlWiKeGtOhgi5lHk-JzXaGOP3fDt9fvymqXjeOcGVLupzQXMdNgL6dLRx0S"
# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
push_service = FCMNotification(APIKEY)
gpio.setmode(gpio.BCM)
# 마그네틱 setup
gpio.setup(20, gpio.IN)
gpio.setup(16, gpio.IN)
gpio.setup(12, gpio.IN)
gpio.setup(7, gpio.IN)
gpio.setup(8, gpio.IN)
gpio.setup(25, gpio.IN)
gpio.setup(24, gpio.IN)
gpio.setup(23, gpio.IN)

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
# 따로따로 동작하기위해
eme=0
cnt = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
dis = 0
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
    talk = f"<voice name='WOMAN_READ_CALM'>{sound}</voice>"
    if __name__ == '__main__':
        tts = KakaoTTS(talk)
        tts.save("speak.mp3")
        pygame.mixer.init()  
        pygame.mixer.music.load(f"/home/pi/Study/project/speak.mp3")
        
        pygame.mixer.music.play()
        
#보관함용
def casespeak(text):
    sound = text
    talk = f"<voice name='WOMAN_READ_CALM'>{sound}</voice>"
    if __name__ == '__main__':
        tts = KakaoTTS(talk)
        tts.save("casespeak.mp3")
        pygame.mixer.init()  
        pygame.mixer.music.load(f"/home/pi/Study/project/casespeak.mp3")
        pygame.mixer.music.play()
        
def alarmbox():    
    while True:       
        res1=requests.post('http://220.80.88.88:8081/controller/alarm.do', json={
            "USER_ID": "pn0005",
            "MED_BOX": "box1",
            "MED_ALARM" : time.strftime('%H:%M')
        })
        res2=requests.post('http://220.80.88.88:8081/controller/alarm.do', json={
            "USER_ID": "pn0005",
            "MED_BOX": "box2",
            "MED_ALARM" : time.strftime('%H:%M')
        })
        res3=requests.post('http://220.80.88.88:8081/controller/alarm.do', json={
            "USER_ID": "pn0005",
            "MED_BOX": "box3",
            "MED_ALARM" : time.strftime('%H:%M')
        })
        res4=requests.post('http://220.80.88.88:8081/controller/alarm.do', json={
            "USER_ID": "pn0005",
            "MED_BOX": "box4",
            "MED_ALARM" : time.strftime('%H:%M')
        })
        res5=requests.post('http://220.80.88.88:8081/controller/alarm.do', json={
            "USER_ID": "pn0005",
            "MED_BOX": "box5",
            "MED_ALARM" : time.strftime('%H:%M')
        })
        res6=requests.post('http://220.80.88.88:8081/controller/alarm.do', json={
            "USER_ID": "pn0005",
            "MED_BOX": "box6",
            "MED_ALARM" : time.strftime('%H:%M')
        })
        time.sleep(40)
        if res1.text != "0":
            text1 = res1.text
            speak(text1)
            print(time.strftime('%H:%M'))
            print(res1.text)
        elif res2.text != "0":
            text2 = res2.text
            speak(text2)
            print(time.strftime('%H:%M'))
            print(res2.text)
        elif res3.text != "0":
            text3 = res3.text
            speak(text3)
            print(time.strftime('%H:%M'))
            print(res3.text)
        elif res4.text != "0":
            text4 = res4.text
            speak(text4)
            print(time.strftime('%H:%M'))
            print(res4.text)
        elif res5.text != "0":
            text5 = res5.text
            speak(text5)
            print(time.strftime('%H:%M'))
            print(res5.text)
        elif res6.text != "0":
            text6 = res6.text
            speak(text6)
            print(time.strftime('%H:%M'))
            print(res6.text)
        else :
            print("아직")
            
boxalarm = threading.Thread(target=alarmbox)
boxalarm.start()

def sendMessage(body, title):
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }
    # 토큰값을 이용해 1명에게 푸시알림을 전송함}
    result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)

    # 전송 결과 출력
    print(result)

def NFC():
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        speak(line)

# 아두이노 시리얼 통신
ser = serial.Serial('/dev/ttyACM1', 115200)  #포트번호
while True:    
    warning = gpio.input(5)
    mag1 = gpio.input(23) 
    mag2 = gpio.input(24) 
    mag3 = gpio.input(25)
    mag4 = gpio.input(8)
    mag5 = gpio.input(7) 
    mag6 = gpio.input(12)
    mag7 = gpio.input(16) 
    mag8 = gpio.input(20) 
    access = time.strftime('%Y-%m-%d %H:%M') 
    time.sleep(0.5)
    if __name__ == '__main__':
        NFC()
    gpio.output(trig, False)
    time.sleep(0.5)
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)
    while gpio.input(echo) == 0:
        pulse_start = time.time()    
    while gpio.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)    
    
    if distance > 50 and dis == 0:
        dis = 7777
        print(f"Distance : {distance}cm")            
            
    elif distance < 50 and dis == 7777 :
        dis = 0
        hi = "반갑습니다. 당신의 건강을 챙겨주는, 복순이 입니다."
        speak(hi)
        print(f"Distance : {distance}cm")
    
    # 마그네틱, 비상버튼 
    
    if mag1 == 0 and cnt1 == 0:
        cnt1 = 1000 
        res = requests.post('http://220.80.88.88:8081/controller/mkbox.do', json={
            "USER_ID": "pn0005", 
            "MED_BOX": "box1" 
            }) 
        requests.post('http://220.80.88.88:8081/controller/mkbox2.do', json={ 
            "USER_ACCESS": access, 
            "USER_ID": "pn0005" 
            })  
        result = res.text 
        print(f"mag1 = {mag1}") 
        casespeak(result) 
    elif mag1 == 1 and cnt1 == 1000: 
        cnt1 = 0 
        print(f"mag1 = {mag1}")
        
    if mag2 == 0 and cnt2 == 0:
        cnt2 = 2000 
        res = requests.post('http://220.80.88.88:8081/controller/mkbox.do', json={ 
            "USER_ID": "pn0005",
            "MED_BOX": "box2",
            })
        requests.post('http://220.80.88.88:8081/controller/mkbox2.do', json={ 
            "USER_ACCESS": access, 
            "USER_ID": "pn0005" 
            }) 
        #2022-05-15 08:19 
        result = res.text
        print(f"mag2 = {mag2}")
        casespeak(result)
    elif mag2 == 1 and cnt2 == 2000: 
        cnt2 = 0 
        print(f"mag2 = {mag2}") 
     
    if mag3 == 0 and cnt3 == 0: 
        cnt3 = 3000
        res = requests.post('http://220.80.88.88:8081/controller/mkbox.do', json={ 
            "USER_ID": "pn0005", 
            "MED_BOX": "box3", 
            }) 
        requests.post('http://220.80.88.88:8081/controller/mkbox2.do', json={ 
            "USER_ACCESS": access, 
            "USER_ID": "pn0005" 
            }) 
        #2022-05-15 08:19 
        result = res.text 
        print(f"mag3 = {mag3}") 
        casespeak(result) 
     
    elif mag3 == 1 and cnt3 == 3000: 
        cnt3 = 0 
        print(f"mag3 = {mag3}") 
     
    if mag4 == 0 and cnt4 == 0: 
        cnt4 = 4000 
        res = requests.post('http://220.80.88.88:8081/controller/mkbox.do', json={ 
            "USER_ID": "pn0005", 
            "MED_BOX": "box4", 
            }) 
        requests.post('http://220.80.88.88:8081/controller/mkbox2.do', json={ 
            "USER_ACCESS": access, 
            "USER_ID": "pn0005" 
            }) 
        #2022-05-15 08:19 
        result = res.text 
        print(f"mag4 = {mag4}") 
        casespeak(result)              
    
    elif mag4 == 1 and cnt4 == 4000: 
        cnt4 = 0 
        print(f"mag4 = {mag4}") 
             
    if mag5 == 0 and cnt5 == 0: 
        cnt5 = 5000 
        res = requests.post('http://220.80.88.88:8081/controller/mkbox.do', json={ 
            "USER_ID": "pn0005", 
            "MED_BOX": "box5", 
            }) 
        requests.post('http://220.80.88.88:8081/controller/mkbox2.do', json={ 
            "USER_ACCESS": access, 
            "USER_ID": "pn0005" 
            }) 
        #2022-05-15 08:19 
        result = res.text 
        print(f"mag5 = {mag5}") 
        casespeak(result)        
     
    elif mag5 == 1 and cnt5 == 5000: 
        cnt5 = 0 
        print(f"mag5 = {mag5}")  
     
    if mag6 == 0 and cnt6 == 0: 
        cnt6 = 6000 
        res = requests.post('http://220.80.88.88:8081/controller/mkbox.do', json={ 
            "USER_ID": "pn0005", 
            "MED_BOX": "box6", 
            }) 
        requests.post('http://220.80.88.88:8081/controller/mkbox2.do', json={ 
            "USER_ACCESS": access, 
            "USER_ID": "pn0005" 
            }) 
        #2022-05-15 08:19 
        result = res.text 
        print(f"mag6 = {mag6}") 
        casespeak(result)      
     
    elif mag6 == 1 and cnt6 == 6000: 
        cnt6 = 0 
        print(f"mag6 = {mag6}") 
     
    if mag7 == 0 and cnt7 == 0: 
        cnt7 = 7000 
        result = "7번, 상비약을, 보관하는, 보관함 입니다." 
        print(f"mag7 = {mag7}") 
        casespeak(result)    
     
    elif mag7 == 1 and cnt7 == 7000: 
        cnt7 = 0 
        print(f"mag7 = {mag7}")  
     
    if mag8 == 0 and cnt8 == 0: 
        cnt8 = 8000 
        result = "8번, 상비약을, 보관하는, 보관함 입니다." 
        print(f"mag8 = {mag8}") 
        casespeak(result)    
     
    elif mag8 == 1 and cnt8 == 8000:
        cnt8 = 0
        print(f"mag8 = {mag8}")
        
    if warning == 1 and eme == 0:
        eme = 200000
        print(f"warning = {warning}")
        res = requests.post('http://220.80.88.88:8081/controller/warning.do', json={ 
            "USER_ID": "pn0005", 
            })
        name = res.text 
        print(name) 
        #init
        pygame.mixer.init()
        #load file
        pygame.mixer.music.load("/home/pi/Study/project/newtone.mp3") 
        #play 
        pygame.mixer.music.play()
            
        sendMessage(f"{name}님께서 긴급 비상버튼을 누르셨습니다\n'생활관리'에서 확인 요망.", "긴급 알림")
    elif warning == 0 and eme == 200000 :
        eme = 0
        print(f"warning = {warning}")
    

 
    #<voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice> 
 
    #<voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice> 
 
    #<voice name="WOMAN_DIALOG_BRIGHT"> 안녕하세요. 여성 밝은 대화체예요.</voice> 
 
    #<voice name="MAN_DIALOG_BRIGHT"> 안녕하세요. 남성 밝은 대화체예요.</voice> 