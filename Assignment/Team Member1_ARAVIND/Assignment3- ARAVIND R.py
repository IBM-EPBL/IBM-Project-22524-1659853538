#led blink program using python

import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True: 
 GPIO.output(8, GPIO.HIGH) 
 sleep(5) # Sleep for 5 seconds
 GPIO.output(8, GPIO.LOW) 
 sleep(5) # Sleep for 5 seconds


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
 sleep(6) # Sleep for 6 seconds
 GPIO.output(8, GPIO.LOW) 
 sleep(6) # Sleep for 6 seconds

#turn yellow light in traffic signal

 GPIO.output(10, GPIO.HIGH) 
 sleep(6)   # Sleep for 6 seconds
 GPIO.output(10, GPIO.LOW) 
 sleep(6)   # Sleep for 6 seconds

#turn green light in traffic signal

 GPIO.output(12, GPIO.HIGH)
 sleep(6)   # Sleep for 6 seconds
 GPIO.output(12, GPIO.LOW) 
 sleep(6)   # Sleep for 6 seconds
