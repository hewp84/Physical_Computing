from machine import Pin
from time import sleep
from ir_rx.nec import NEC_8

state = 0

def switch(): 
    global state 
    state = 1-state 
    return state

def ir_callback(data, addr, ctrl):
    global ir_data
    global ir_addr
    if data > 0:
        ir_data = data #Assigning a localdrive variable to input from remote control
        ir_addr = addr
        print(f'Data {data} Addr {addr}') #Just for checking. During operation should be removed
            
  
#Declaring var pins
ir = NEC_8(Pin(17, Pin.IN), ir_callback)
red = Pin(1, Pin.OUT)
yellow = Pin(2, Pin.OUT)
green = Pin(3, Pin.OUT)

ir_data = 0 #initializing global variables for while True
ir_addr = 0 #initializing global variables for while True

while True:
    if ir_data > 0:
        if ir_data == 22:   # Button 1
            switch()		#Activate a toggle effect on variable state
            red.value(state) #bound variable state with the value of the red LED
        if ir_data == 25:   # Button 2
            switch()		#Activate a toggle effect on variable state
            yellow.value(state) #bound variable state with the value of the yellow LED
        if ir_data == 13:   # Button 3
            switch()		#Activate a toggle effect on variable state
            green.value(state) #bound variable state with the value of the green LED
        ir_data = 0			#resets data coming from remote (filters unnecessary data)
        
        
        