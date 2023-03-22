#Calculator
from machine import Pin
from time import sleep
from ir_rx.nec import NEC_8

#Dictionary to convert ir_Data to name button
buttons = {22:'1',25:'2', 13:'3',12:'4',24:'5',94:'6',8:'7',28:'8',90:'9',82:'0', 70:'+',21:'-',68:'*',67:'/'}

def ir_callback(data, addr, ctrl):
    global ir_data
    global ir_addr
    if data > 0:
        ir_data = data #Assigning a localdrive variable to input from remote control
        ir_addr = addr
#Declaring var pins
ir = NEC_8(Pin(17, Pin.IN), ir_callback)

ir_data = 0 #initializing global variables for while True
ir_addr = 0 #initializing global variables for while True
string = ''
while True:
    if ir_data > 0:
        if ir_data == 64: #Button Ok
            print(eval(string))
            string = ''
        else:
            string = string + buttons[ir_data]
            print(string)
        
    ir_data = 0
        
        
        
