import time
from machine import Pin
from picozero import LED
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

red = LED(13)
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
        
def light():
    red.toggle()
    
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(data)
        if data == 22:
            light()
        if data == 67:
            adder()
        if data == 68:
            subber()
        
ir = NEC_8(Pin(17, Pin.IN), callback)

while True:
    pass