import machine
from time import sleep
from picozero import Button
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#Declaring parameters to display on LCD
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #Using GPIO 0 and 1 for sda and scl respectively
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


#Algorithm to latch a state from button #######
state = 0
button = Button(5) #connecting to GPIO 5

def switch(): 
    global state 
    state = 1-state 
    return state
####################################

# Set the GPIO outputs (PICO view)
enb = machine.Pin(14, machine.Pin.OUT)
in3 = machine.Pin(12, machine.Pin.OUT)
in4 = machine.Pin(13, machine.Pin.OUT)

ena = machine.Pin(15, machine.Pin.OUT)
in1 = machine.Pin(16, machine.Pin.OUT)
in2 = machine.Pin(17, machine.Pin.OUT)

#Analog port for Potetiometer
analog_port = machine.ADC(26) #ADC GPIO 26

while True:
    button.when_pressed = switch  #latch direction of motor
    print(state)
    value = analog_port.read_u16()  #speed variable
    print(value)
# Set the PWM frequency and the GPIO port
    pwm_freq = 1000
    pwma = machine.PWM(ena)
    pwma.freq(pwm_freq)
    
    pwmb = machine.PWM(enb)
    pwmb.freq(pwm_freq)

# Set the direction and speed
#motor 1
    in1.value(state)
    in2.value(1-state)
    pwma.duty_u16(value) 
#motor 2   
    in3.value(state)
    in4.value(1-state)
    pwmb.duty_u16(value) 
#LCD display    
    lcd.backlight_on()
    lcd.putstr(f'Speed: {value/65535*100:.0%}')
    lcd.move_to(0,1)
    lcd.putstr(f'Spin: {state}')
    lcd.move_to(0,0)
    # Wait for 0.2 seconds
    sleep(0.2)

