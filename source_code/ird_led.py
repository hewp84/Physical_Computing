import time
from machine import Pin
from ird_lib import read_ircode

led = Pin(14, Pin.OUT)
ird = Pin(16,Pin.IN)
state = 0
count = 0

def switch(): 
    global state 
    state = 1-state 
    return state
def adder():
    global count
    if count < 5:
        count +=1
        print(count)
def subber():
    global count
    if count >0:
        count -=1
        print(count)

while True:
    command = read_ircode(ird)
    if command == "1":
        switch()
        led.value(state)
        print(command)
    if command == "Right":
        adder()
        
    if command == "Left":
        subber()
        
            