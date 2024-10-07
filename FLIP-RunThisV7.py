
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
#V2 - Here I implement different modes (fixed logic) and speeds (fixed logic) with seperate function calls
#V3 - Two unused modes are added and repeatable position changes are removed from the code through the tempPos variable
#V4 - All calls to the utime.sleep function are changed to utime.sleep_ms to increase the resolution of random logic
#V5 - Add a duel mode where the singal is detected from a addon port for a plug in light (Intention is to activate the light [not yet implemented])
#V6 - Program is altered to use a constant mode and speed button listener to avoid using dial switches with 22 points of soldering
#End of Version Updates
#
##############################################################################################################################################

from machine import Pin, PWM
import utime
import random

#Servo GP Designation
servoPin = 0

#Establish Null value for memeory keeping
tempPos = None

#Set mode switch values
#mode 0  Default duel mode
#mode 1  Off (No activity)
#mode 2  Friendly - Enemy - Repeat
#mode 3  Friendly - No Threat - Enemy - No Threat - Repeat
#mode 4  Friendly - No Threat - Repeat
#mode 5  Enemy - No Threat - Repeat
#mode 6  Random with Priority to No threat
#mode 7  Random with Priority to Friendly
#mode 8  Random with Priority to Enemy
#mode 9  Random with Average Priority
#mode 10 Random without Friendly
#mode 11 Random without No Threat

#Set speed switch values
#speed 0  Off (No activity)
#speed 1  Set random speed to low-1
#speed 2  Set random speed to low-2
#speed 3  Set random speed to medium
#speed 4  Set random speed to high-1
#speed 5  Set random speed to high-2
#speed 6  Set constant speed to 20%
#speed 7  Set constant speed to 40%
#speed 8  Set constant speed to 60%
#speed 9  Set constant speed to 80%
#speed 10 Set constant speed to 100%


#Set the mode button and current value
mode = Pin(mZ, Pin.In)
currMode = 0

#Set the speed button and current value
speed = Pin(s0, Pin.IN)
currSpeed = 0

#Setup servo value
servo = PWM(Pin(servoPin))
servo.freq(50)

#Enter program with safe set to position 0
servo.duty_u16(2100)

#checkMode hasn't been implemented yet
def checkMode()
    if mode.value() == True:
        if currMode == 11:
            currMode == 1
        else:
            currMode++
#checkSpeed hasn't been implemented yet
def checkSpeed()
    if speed.value() == True:
        if currSpeed == 10:
            currSpeed = 0
        else:
            currSpeed++

def getDelay()
    if currSpeed == 1:
        randomTime = random.randint(2250, 4000)
        utime.sleep_ms(randomTime)
    elif currSpeed == 2:
        randomTime = random.randint(1750, 3000)
        utime.sleep_ms(randomTime)
    elif currSpeed == 3:
        randomTime = random.randint(1250, 2000)
        utime.sleep_ms(randomTime)
    elif currSpeed == 4:
        randomTime = random.randint(750, 1500)
        utime.sleep_ms(randomTime)
    elif currSpeed == 5:
        randomTime = random.randint(250, 1000)
        utime.sleep_ms(randomTime)
    elif currSpeed == 6:
        utime.sleep_ms(4000)
    elif currSpeed == 7:
        utime.sleep_ms(2000)
    elif currSpeed == 8:
        utime.sleep_ms(1000)
    elif currSpeed == 9:
        utime.sleep_ms(500)
    else:
        utime.sleep_ms(250)

def moveToFriend():
    servo.duty_u16(2100)
    tempPos = 0
    getDelay()
    
def moveToNeutral():
    servo.duty_u16(4300)
    tempPos = 1
    getDelay()
    
def moveToEnemy():
    servo.duty_u16(6500)
    tempPos = 2
    getDelay()

#Running Loop so the program can idle. This never terminates
while True:
    if currMode == 0 or currSpeed == 0:
        #Do nothing
    elif currMode == 1:
        randomPos = random.choice(1, 1, 2, 1, 1)
        if randomPos == 1:
            moveToNeutral()
        elif randomPos == 2:
            moveToEnemy()
    elif currMode == 2:
        moveToFriend()
        moveToEnemy()
    elif currMode == 3:
        moveToFriend()
        moveToNeutral()
        moveToEnemy()
        moveToNeutral()
    elif currMode == 4:
        moveToFriend()
        moveToNeutral()
    elif currMode == 5:
        moveToEnemy()
        moveToNeutral()
    elif currMode == 6:
        randomPos = random.choice(0, 1, 1, 1, 2)
        if randomPos == 0 and tempPos != 0:
            moveToFriend()
        elif randomPos == 1 and tempPos != 1:
            moveToNeutral()
        elif randomPos == 2 and tempPos != 2:
            moveToEnemy()
    elif currMode == 7:
        randomPos = random.choice(0, 0, 0, 1, 2)
        if randomPos == 0 and tempPos != 0:
            moveToFriend()
        elif randomPos == 1 and tempPos != 1:
            moveToNeutral()
        elif randomPos == 2 and tempPos != 2:
            moveToEnemy()
    elif currMode == 8:
        randomPos = random.choice(0, 1, 2, 2, 2)
        if randomPos == 0 and tempPos != 0:
            moveToFriend()
        elif randomPos == 1 and tempPos != 1:
            moveToNeutral()
        elif randomPos == 2 and tempPos != 2:
            moveToEnemy()
    elif currMode == 9:
        randomPos = random.randint(0, 1, 2)
        if randomPos == 0 and tempPos != 0:
            moveToFriend()
        elif randomPos == 1 and tempPos != 1:
            moveToNeutral()
        elif randomPos == 2 and tempPos != 2:
            moveToEnemy()
    elif currMode == 10:
        randomPos = random.randint(1, 2)
        if randomPos == 1 and tempPos != 1:
            moveToNeutral()
        elif randomPos == 2 and tempPos != 2:
            moveToEnemy()
    elif currMode == 11:
        randomPos = random.randint(0, 2)
        if randomPos == 1 and tempPos != 1:
            moveToNeutral()
        elif randomPos == 2 and tempPos != 2:
            moveToEnemy()
    else:
        #Skipped Move
        print("* The randome value cannot be the same as the previous value for a successful movement.")
            
    #Exit loop with safe set to position 0
    servo.duty_u16(2100)
    
    #Pause for dial off responce
    utime.sleep_ms(1000)
    
#Written by Tanner Utz - Created Nov 1, 2021
