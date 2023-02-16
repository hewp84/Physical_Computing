from picozero import LED, Button
from time import sleep

led = [LED(3),LED(4),LED(5),LED(6),LED(7),LED(8)] #created an array for multiple LEDs. Every number is a GPIO port
button = Button(2) #GPIO 2

while True:
    if button.is_pressed:
        
        for i in range(0,6):
            led[i].on()
            sleep(0.5)
        for j in range(0,6):
            led[j].off()
            sleep(0.5)