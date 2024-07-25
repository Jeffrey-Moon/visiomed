import RPi.GPIO as gpio
import time
import pygame
gpio.setmode(gpio.BCM)
gpio.setup(5, gpio.IN)
cnt = 0

while True : 
    mag = gpio.input(5)
    time.sleep(1)
    if mag == 1 and cnt == 0 :
        cnt =10000
        print(mag)

        
    elif mag == 0 and cnt == 10000 :
        
        print(mag)
        pygame.mixer.quit()
        cnt = 0
    
