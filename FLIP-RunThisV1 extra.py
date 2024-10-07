#This program utilizes the time and random libraries to utilize random algorithems to flip chnage the orientation of a servo motor.
#The servo motor is mounted on a clip or base plate and can but mounted in multiple ways.
import RPi.GPIO as GPIO
import time
import random

s1 = 0 #Needs set to the GPIO Pin for servo

GPIO.setmode(GPIO.BOARD)
GPIO.setup(s1, GPIO.out)

pwm=GPIO.PWM(11, 50)
pwm.start()

pwm.ChangeDutyCycle(5)
sleep(1)
pwm.ChangeDutyCycle(7.5)
sleep(1)
pwm.ChangeDutyCycle(10)
sleep(1)

pwm.stop()
GPIO.cleanup()

#Written By Tanner Utz
