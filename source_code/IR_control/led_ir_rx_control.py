import time
from machine import Pin
from picozero import LED
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses

red = LED(13)

def light():
    red.toggle()
    
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(data)
        if data == 22:
            light()    
        
ir = NEC_8(Pin(17, Pin.IN), callback)

while True:
    pass
    