from picozero import LED, Button
from time import sleep
from machine import Timer

button = Button(21)
c = 0
while True:
    if button.is_pressed:
        
        
        c+=1
        sleep(0.2)
        if c == 1:
            print("One click")
        elif c == 2:
            print("Two click")
            sleep(0.2)
            c=0
        