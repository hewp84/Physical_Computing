#Generic code for reading and displaying Analog Inputs values
#Library Import
import machine
from time import sleep
from machine import PWM, Pin
from time import sleep
from ir_rx.nec import NEC_8

#Global variable declaration
count = 0
state = 0

#Function definition
#Switching function on global variable state
def switch(): 
    global state 
    state = 1-state 
    return state

#Adding function on global variable count
def adder():
    global count
    if count < 10:
        count +=1
        
#Subtracting function on global variable count
def subber():
    global count
    if count >0:
        count -=1

#Callback to save incoming data from remote control
def ir_callback(data, addr, ctrl):
    global ir_data
    global ir_addr
    if data > 0:
        ir_data = data #Assigning a localdrive variable to input from remote control
        ir_addr = addr
        #print(f'Data {data} Addr {addr}') #Just for checking. During operation should be removed
            
#Declaring GPIOs
ir = NEC_8(Pin(17, Pin.IN), ir_callback)
pwm = PWM(Pin(13))
pwm.freq(50)

#Initializing remote control variables
ir_data = 0 #initializing global variables for while True
ir_addr = 0 #initializing global variables for while True

while True:
    #Filtering changes from incoming data
    if ir_data > 0:
        if ir_data == 67:   # Button Right
            adder()		#Adds on variable count
        if ir_data == 68:   # Button Ledt
            subber()		#Subtracts on variable count
        if ir_data == 64: # Button OK
            switch()
            count = count * state #State behaves as on/off
        
        #Actions after pressing buttons
        bar = '*'*count
        print(f'Counter: {bar} {round(count/10*100)}%	\nState: {state}')
        pwm.duty_u16(int(1000 + count/10 * 7200)) #Sending data to servo (1000 - 8200). 
        sleep(0.1)
        ir_data = 0			#resets data coming from remote (filters unnecessary data)

   