import requests
import pygame

# 자신의 REST_API_KEY를 입력하세요!
REST_API_KEY = "bd37be6b8780ba2fa093e026ce6fd291"


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
talk = "반갑습니다"
text = f"<voice name='WOMAN_DIALOG_BRIGHT'>{talk}</voice>"
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
