from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #Using GPIO 0 and 1 for sda and scl respectively
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

number = int(input(f'Enter number: '))
square = number **2

lcd.backlight_on()
lcd.putstr("The number" + str(number))
lcd.move_to(0,1)
lcd.putstr(f'The square is {square}')