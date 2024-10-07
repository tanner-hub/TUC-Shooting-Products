
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
#End of Version Updates
#
##############################################################################################################################################

from machine import Pin, PWM
import utime
import random

#Servo GP Designation
servoPin = 0

#Set mode switch values
mA = 1    #Off (No activity)
mB = 2    #Friendly - Enemy - Repeat
mC = 3    #Friendly - No Threat - Enemy - No Threat - Repeat
mD = 4    #Friendly - No Threat - Repeat
mE = 5    #Enemy - No Threat - Repeat
mF = 6    #Random with Priority to No threat
mG = 7    #Random with Priority to Friendly
mH = 8    #Random with Priority to Enemy
mI = 9    #Completly Random
mJ = 10   #Unused
mK = 11   #Unused

#Set speed switch values
s0 = 12  #Off (No activity)
s1 = 13  #Set random speed to low-1
s2 = 14  #Set random speed to low-2
s3 = 15  #Set random speed to medium
s4 = 16  #Set random speed to high-1
s5 = 17  #Set random speed to high-2
s6 = 18  #Set constant speed to 20%
s7 = 19  #Set constant speed to 40%
s8 = 20  #Set constant speed to 60%
s9 = 21  #Set constant speed to 80%
s10 = 22 #Set constant speed to 100%

#Set the mode dial
modeA = Pin(mA, Pin.IN)
modeB = Pin(mB, Pin.IN)
modeC = Pin(mC, Pin.IN)
modeD = Pin(mD, Pin.IN)
modeE = Pin(mE, Pin.IN)
modeF = Pin(mF, Pin.IN)
modeG = Pin(mG, Pin.IN)
modeH = Pin(mH, Pin.IN)
modeI = Pin(mI, Pin.IN)
modeJ = Pin(mJ, Pin.IN)
modeK = Pin(mK, Pin.IN)

#Set the speed dial
speed0 = Pin(s0, Pin.IN)
speed1 = Pin(s1, Pin.IN)
speed2 = Pin(s2, Pin.IN)
speed3 = Pin(s3, Pin.IN)
speed4 = Pin(s4, Pin.IN)
speed5 = Pin(s5, Pin.IN)
speed6 = Pin(s6, Pin.IN)
speed7 = Pin(s7, Pin.IN)
speed8 = Pin(s8, Pin.IN)
speed9 = Pin(s9, Pin.IN)
speed10 = Pin(s10, Pin.IN)

#Setup servo value
servo = PWM(Pin(servoPin))
servo.freq(50)

#Enter program with safe set to position 0
servo.duty_u16(2100)

def getDelay()
    if speed1.value() == True:
        randomTime = random.randint(3, 6)
        utime.sleep(randomTime)
    elif speed2.value() == True:
        randomTime = random.randint(2, 5)
        utime.sleep(randomTime)
    elif speed3.value() == True:
        randomTime = random.randint(2, 4)
        utime.sleep(randomTime)
    elif speed4.value() == True:
        randomTime = random.randint(1, 3)
        utime.sleep(randomTime)
    elif speed5.value() == True:
        randomTime = random.randint(0.5, 2)
        utime.sleep(randomTime)
    elif speed6.value() == True:
        utime.sleep(6)
    elif speed7.value() == True:
        utime.sleep(4)
    elif speed8.value() == True:
        utime.sleep(2)
    elif speed9.value() == True:
        utime.sleep(1)
    else:
        utime.sleep(0.5)

def moveToFriend():
    servo.duty_u16(2100)
    getDelay()
    
def moveToNeutral():
    servo.duty_u16(4300)
    getDelay()
    
def moveToEnemy():
    servo.duty_u16(6500)
    getDelay()

#Running Loop so the program can idle. This never terminates
while True:

    #While neither of the dials are set to off
    while modeA.value() == False and speed0.value() == False:
        if modeB.value() == True:
            moveToFriend()
            moveToEnemy()
        elif modeC.value() == True:
            moveToFriend()
            moveToNeutral()
            moveToEnemy()
            moveToNeutral()
        elif modeD.value() == True:
            moveToFriend()
            moveToNeutral()
        elif modeE.value() == True:
            moveToEnemy()
            moveToNeutral()
        elif modeF.value() == True:
            randomPos = random.choice(0, 1, 1, 1, 2)
            if randomPos == 0:
                moveToFriend()
            elif randomPos == 1:
                moveToNeutral()
            else:
                moveToEnemy()
        elif modeG.value() == True:
            randomPos = random.choice(0, 0, 0, 1, 2)
            if randomPos == 0:
                moveToFriend()
            elif randomPos == 1:
                moveToNeutral()
            else:
                moveToEnemy()
        elif modeH.value() == True:
            randomPos = random.choice(0, 1, 2, 2, 2)
            if randomPos == 0:
                moveToFriend()
            elif randomPos == 1:
                moveToNeutral()
            else:
                moveToEnemy()
        elif modeI.value() == True:
            randomPos = random.randint(0, 2)
            if randomPos == 0:
                moveToFriend()
            elif randomPos == 1:
                moveToNeutral()
            else:
                moveToEnemy()
        elif modeJ.value() == True:
            #Unused
            print("Unused mode")
        else:
            #Unused
            print("Unused mode")
            
    #Exit loop with safe set to position 0
    servo.duty_u16(2100)
    
    #Pause for dial off responce
    utime.sleep(1)
    
#Written by Tanner Utz - Created Nov 1, 2021
