
##############################################################################################################################################
#
#FLIP "RunThisV_" - Injectable python script intended for the raspberry pi pico to interface with a man sized target
#Written by Tanner Utz - Created Nov 1, 2021
#
#This program utilizes the time and random libraries to utilize random algorithems to flip and change the orientation of a servo motor.
#The servo motor is mounted on a clip or base plate and can but mounted in multiple ways and interface with multiple targets.
#Two rotary switches will be used for speed, mode, and running status, while a push button switch will be ignored from this program for power
#
#Position 0 inidcates no threat
#Position 1 inidcates no subject
#Position 2 inidcates present threat
#
#Version Updates Below:
#V1 - Default setup to allow altering through various positions randomly. Only 1 mode and speed are available in this version
#End of Version Updates
#
##############################################################################################################################################

from machine import Pin, PWM
import utime
import random

#Servo GP Designation
servoPin = 0

#Setup servo value
servo = PWM(Pin(servoPin))
servo.freq(50)

#Enter program with safe set to position 0
servo.duty_u16(2100)
currentPos = 0

#Running Loop so the program can idle. This never terminates
while True:

    #While neither of the dials are set to off
    while True:
    
        #Run - Needs altered for alternative modes
        
        #These will eventually be customizable by dial switches
        randomChoice = random.randint(0, 2)
        randomTime = random.randint(1, 2)
        
        if randomChoice == 0:
        
            #Rotate to angle 0 from point 0
            servo.duty_u16(2100)
            
            currentPos = 0
            utime.sleep(randomTime)
            
        elif randomChoice == 1:
        
            #Rotate to angle 90 from point 0
            servo.duty_u16(4300)
            
            currentPos = 1
            utime.sleep(randomTime)
            
        else:
        
            #Rotate to angle 180 from point 0
            servo.duty_u16(6500)
            
            currentPos = 2
            utime.sleep(randomTime)
            
    #Exit loop with safe set to position 0
    servo.duty_u16(2100)
    currentPos = 0
    
    #Pause for dial off responce
    utime.sleep(1)
    
#Written by Tanner Utz - Created Nov 1, 2021
