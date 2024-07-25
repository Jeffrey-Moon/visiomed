import requests
import pygame
import serial
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
# 마그네틱 setup
gpio.setup(8, gpio.IN)
gpio.setup(7, gpio.IN)

# warning setup
gpio.setup(20, gpio.IN)

# 초음파 setup
trig = 19
echo = 26
gpio.setwarnings(False)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
# 자신의 REST_API_KEY를 입력하세요!
# 카카오 tts api key
REST_API_KEY = "bd37be6b8780ba2fa093e026ce6fd291"
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

def speak(text):
    if __name__ == '__main__':
        tts = KakaoTTS(text)
        tts.save("speak.mp3")
        pygame.mixer.init()  
        pygame.mixer.music.load(f"/home/pi/Study/project/speak.mp3")
        pygame.mixer.music.play()
# 붙 0
# 떨 1
# 아두이노 시리얼 통신
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
while True:      
    # 초음파
    gpio.output(trig, False)
    time.sleep(1  )
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
    if distance < 50  and cnt == 0 :
        cnt = 9000
        hi = "반갑습니다. 당신의 건강을 챙겨주는, 닥터, 복순이 입니다."
        text = f"<voice name='WOMAN_DIALOG_BRIGHT'>{hi}</voice>"
        if __name__ == '__main__':
            tts = KakaoTTS(text)
            tts.save("hi.mp3")

                #init
            pygame.mixer.init()
 
            #load file
            pygame.mixer.music.load("/home/pi/Study/project/hi.mp3")
 
            #play
            pygame.mixer.music.play()
        print(f"Distance : {distance}cm")
        
    elif distance > 50 and cnt == 9000 :
        cnt = 0
        print(f"Distance : {distance}cm")
    
    
    # 마그네틱, 비상버튼
    mag1 = gpio.input(8)
    mag2 = gpio.input(7)
    warning = gpio.input(20)
    time.sleep(0.5)
    if mag1 == 0 and cnt == 0:
        cnt = 1000
        talking = "1번 보관함 입니다. 감기약 복용하세요"
        text = f"<voice name='WOMAN_DIALOG_BRIGHT'>{talking}</voice>"
        print(f"mag1 = {mag1}")
        if __name__ == '__main__':
            tts = KakaoTTS(text)
            tts.save("case1.mp3")

                #init
            pygame.mixer.init()
 
            #load file
            pygame.mixer.music.load("/home/pi/Study/project/case1.mp3")
 
            #play
            pygame.mixer.music.play()

    elif mag1 == 1 and cnt == 1000:
        cnt = 0
        print(f"mag1 = {mag1}")
    

    if mag2 == 0 and cnt == 0:
        talking = "2번 보관함 입니다. 감기약 복용하세요"
        text = f"<voice name='WOMAN_DIALOG_BRIGHT'>{talking}</voice>"
        cnt = 2000
        print(f"mag2 = {mag2}")
        if __name__ == '__main__':
            tts = KakaoTTS(text)
            tts.save("case2.mp3")

                #init
            pygame.mixer.init()
 
            #load file
            pygame.mixer.music.load("/home/pi/Study/project/case2.mp3")
 
            #play
            pygame.mixer.music.play()
            
    elif mag2 == 1 and cnt == 2000:
        cnt = 0
        print(f"mag2 = {mag2}")
    
    if warning == 1 and cnt == 0:
        cnt = 10000
        print(f"warning = {warning}")
        
                #init
        pygame.mixer.init()
 
            #load file
        pygame.mixer.music.load("/home/pi/Study/project/sirr.mp3")
 
            #play
        pygame.mixer.music.play()
    elif warning == 0 and cnt == 10000:
        cnt = 0
        print(f"warning = {warning}")
        pygame.mixer.quit()
    
    if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            text = f"<voice name='WOMAN_DIALOG_BRIGHT'>{line}</voice>"
            if __name__ == '__main__':
                tts = KakaoTTS(text)
                tts.save("output1.mp3")
#<voice name="WOMAN_READ_CALM"> 지금은 여성 차분한 낭독체입니다.</voice>
#<voice name="MAN_READ_CALM"> 지금은 남성 차분한 낭독체입니다.</voice>
#<voice name="WOMAN_DIALOG_BRIGHT"> 안녕하세요. 여성 밝은 대화체예요.</voice>
#<voice name="MAN_DIALOG_BRIGHT"> 안녕하세요. 남성 밝은 대화체예요.</voice>
    #init
            pygame.mixer.init()
 
    #load file
            pygame.mixer.music.load("/home/pi/Study/project/output1.mp3")
 
    #play
            pygame.mixer.music.play()


