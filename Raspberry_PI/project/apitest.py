import requests
import pygame

import serial
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(8, gpio.IN)
# 자신의 REST_API_KEY를 입력하세요!
REST_API_KEY = "bd37be6b8780ba2fa093e026ce6fd291"


cnt = 0
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


while True :
    mag = gpio.input(8)
    
    time.sleep(0.5)
    if mag == 0 and cnt == 0:
        talking = "1번 보관함 입니다. 감기약 복용하세요"
        text = f"<voice name='WOMAN_DIALOG_BRIGHT'>{talking}</voice>"
        cnt = 1
        print(mag)
        if __name__ == '__main__':
            tts = KakaoTTS(text)
            tts.save("output2.mp3")

                #init
            pygame.mixer.init()
 
            #load file
            pygame.mixer.music.load("/home/pi/Study/project/output2.mp3")
 
            #play
            pygame.mixer.music.play()
    elif mag == 1:
        
        cnt = 0
        print(mag)
        
