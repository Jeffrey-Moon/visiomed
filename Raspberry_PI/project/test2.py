import requests
import pygame
import serial
import RPi.GPIO as gpio
import time
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

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
        pygame.mixer.music.play()
def casespeak(text):
    if __name__ == '__main__':
        tts = KakaoTTS(text)
        tts.save("casespeak.mp3")
        pygame.mixer.init()  
        pygame.mixer.music.load(f"/home/pi/Study/project/casespeak.mp3")
        
        #pygame.mixer.music.pause()
        pygame.mixer.music.play()
        pygame.mixer.music.play()


speak("안녕하세요")
casespeak("반갑습니다")