#This program utilizes the Button, Time, Random, and GPIO libraries to set a raspberry pis output to a relay so an electric
#motor can be ran in randomly alternating directions for random time variables with an index perimeter limiting
#the total run for the motor in either direction. This code utlizes the hardware of a raspberry pi zero,  4 channel relay
#board,  and 3 momentary switches.
import RPi.GPIO as GPIO
import time
import random

#Declorations for global variables
direction = 1
lFactor = 20

#Declorations for ports
r1 = 16
r2 = 18
r3 = 15
r4 = 13
b1 = 33
b2 = 35
b3 = 37

#Set GPIO Board for relay control
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)
GPIO.setup(r4, GPIO.OUT)
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Initiate all relays as off
GPIO.output(r1, True)
GPIO.output(r2, True)
GPIO.output(r3, True)
GPIO.output(r4, True)

#Start the program with a default direction and prompt
def start():

    print("[Program Initiated By Compiler]")
    
    #Sit in this loop until initiate buttin has been pressed
    while GPIO.input(b1) == True:
        #Wait for button to be pressed
        time.sleep(0.1)
        
    print("[Program Prompted By User]")
    
    #Start in default direction
    GPIO.output(r1, False)
    GPIO.output(r3, False)

#Swap direction based on globally declared direction variable
def swapDirection():
    global direction
    if direction == 1:
        GPIO.output(r1, True)
        GPIO.output(r3, True)
        time.sleep(0.25) #Default to library because this breaks shit
        GPIO.output(r2, False)
        GPIO.output(r4, False)
        direction = 0
    else:
        GPIO.output(r2, True)
        GPIO.output(r4, True)
        time.sleep(0.25) #Default to library because this breaks shit
        GPIO.output(r1, False)
        GPIO.output(r3, False)
        direction = 1
    print("[Direction Has Changed]")
            
#Check if either limits have been reached
def checkPosition():
    if  (GPIO.input(b2) == False) or (GPIO.input(b3) == False):
        swapDirection()
        time.sleep(1) #Give it time to confirm the change in direction
        return True

#Sleep overload function (Checks Position every 1/10 of a second)
def mySleep(sleepCycle):
    count = 0
    while count < sleepCycle * 10:
        if checkPosition():
            break
        time.sleep(0.1)
        count = count + 1

#Master Function
start()
count = 0
while count < lFactor:
    randomChoice = random.randint(0, 1)
    randomTime = random.randint(1, 5)
    if randomChoice == 1:
        swapDirection()
    mySleep(randomTime)
    count = count + 1
        
#Written By Tanner Utz
