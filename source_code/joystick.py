#Joystick Reading

import machine
from time import sleep
from picozero import Button

button = Button(25) #connecting to GPIO 25
x_dim = machine.ADC(26) # connecting to ADC GPIO 26
y_dim = machine.ADC(27) # connecting to ADC GPIO 27

while True:
    x_value = x_dim.read_u16()
    y_value = y_dim.read_u16()
    print(f'Button: {button.value} , x-dimension: {x_value} , y-dimension: {y_value}')
    sleep(0.1)