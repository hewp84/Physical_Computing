from machine import Pin
import utime

#ultrasonic distance ranging measured in centimeters

#create a function called distance
def getDistance(trigger, echo):
    # produce the square wave of 10 microsecondss
    trigger.low() #give a short low level and ensure a high pulse:
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10) #pull up the high levels, wait for 10 microseconds and set to low level
    trigger.low()
    while echo.value() == 0: #build a while loop to detect if the pin is 0, record the current time
        start = utime.ticks_us()
    while echo.value() == 1: #build a while loop to detect if the pin is 1，record the current time
        end = utime.ticks_us()
    d = (end - start) * 0.0343 / 2 #traveling time x speed of sound(343.2 m/s，0.0343 for each microsecond)，the total distance is divided by 2
    return d
# set pins
trigger = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)
# main program
while True:
    distance = getDistance(trigger, echo)
    print(f'The distance is ：{distance:.2f} cm')
    utime.sleep(0.1)