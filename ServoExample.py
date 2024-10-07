from machine import Pin, PWM
import utime

servo = PWM(Pin(0))

servo.freq(50)

#start 2100 end 6500
while True:

    servo.duty_u16(2100)
    utime.sleep(2)
    
    servo.duty_u16(6500)
    utime.sleep(2)
