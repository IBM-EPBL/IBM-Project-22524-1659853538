#led blink program using python

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(8, GPIO.HIGH) 
 sleep(3) # Sleep for 3 seconds
 GPIO.output(8, GPIO.LOW) 
 sleep(3) # Sleep for 3 seconds


#traffic light program using python


import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
while True: 

#turn red light in traffic signal

 GPIO.output(8, GPIO.HIGH) 
 sleep(4) # Sleep for 4 seconds
 GPIO.output(8, GPIO.LOW) 
 sleep(4) # Sleep for 4 seconds

#turn yellow light in traffic signal

 GPIO.output(10, GPIO.HIGH) 
 sleep(4)   # Sleep for 4 seconds
 GPIO.output(10, GPIO.LOW) 
 sleep(4)   # Sleep for 4 seconds

#turn green light in traffic signal

 GPIO.output(12, GPIO.HIGH)
 sleep(4)   # Sleep for 4 seconds
 GPIO.output(12, GPIO.LOW) 
 sleep(4)   # Sleep for 4 seconds
