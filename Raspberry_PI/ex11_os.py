#시스템 명령어 자체를 파이썬에서 쓰기 위한 라이브러리
import os
#system 명령어 호출기 

#os.system('ifconfig')
#os.system('raspistill -o img.jpg')
################################################################
#.h264 동영상 파일 생성
os.system('raspivid -o test.h246')
# 파일 변환 (.mp4)
os.system('MP4Box -add test.h264 test.mp4')
