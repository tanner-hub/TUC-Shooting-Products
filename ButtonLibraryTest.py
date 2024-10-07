import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    input_state = GPIO.input(33)
    if input_state == False:
        print('Button has been pressed')
        time.sleep(0.1)


#my original code uses the wrong port designations, use 33, 35, 37
