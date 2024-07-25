import picamera

#with ~as 구문 : with 안에 있는 구문이 종료되면 자동으로 해당 객체의 close()함수를 호출
with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.start_preview()
    camera.start_recording('vid.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()