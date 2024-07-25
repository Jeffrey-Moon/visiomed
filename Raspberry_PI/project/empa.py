import RPi.GPIO as GPIO
import time

triggerPin = 19
echoPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
try:
    while True:
      GPIO.output(triggerPin, GPIO.LOW)
      time.sleep(0.00001)                
      GPIO.output(triggerPin, GPIO.HIGH)

      while GPIO.input(echoPin) == 0:
         start = time.time()
      while GPIO.input(echoPin) == 1:
         stop = time.time()

      rtTotime = stop - start

      distance = rtTotime * ( 34000 / 2 )
      print("distance : %.2f cm" %distance)
      time.sleep(1) 
except KeyboardInterrupt:
   GPIO.cleanup()
   
   
   
   
   
   
   gpio.output(trig, False)
    time.sleep(1)
    gpio.output(trig, True)
    time.sleep(1 )
    gpio.output(trig, False)
    while gpio.input(echo) == 0:
        pulse_start = time.time()
            
    while gpio.input(echo) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)