import time
from machine import Pin
from ird_lib import read_ircode

led = Pin(14, Pin.OUT)
ird = Pin(16,Pin.IN)
flag = False

while True:
#     global flag
    command = read_ircode(ird)
    #print(command, end = "  ")
    print(flag, end = "  ")
    if command == "1":
        if flag == True:
            led.value(1)
            flag = False
            print("led on")
        else:
            led.value(0)
            flag = True
            print("led off")
    time.sleep(0.1)