#사진 촬영
import picamera as pc
import time
camera = pc.PiCamera()
camera.start_preview() #미리보기 화면 시작
time.sleep(5)
for i in range(3):
    camera.capture("picture{}.jpg".format(i)) #저장 및 저장 제목
    
camera.stop_preview()  #미리보기 화면 종료    
camera.close()
