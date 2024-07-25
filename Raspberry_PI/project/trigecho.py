import RPi.GPIO as GPIO
import time
 
trig = 19
echo = 26
 

 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
cnt = 0
while(True):
    
    GPIO.output(trig, False)
    time.sleep(0.5)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
            
    while GPIO.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    if distance < 30 and cnt == 0 :
        cnt = 9000
        print(f"Distance : {distance}cm")
    elif distance >30 and cnt == 9000 :
        cnt = 0
        print(f"Distance : {distance}cm")