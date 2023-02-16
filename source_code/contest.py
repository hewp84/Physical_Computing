from picozero import LED, Button
from time import sleep

green = LED(15)
red = LED(18)
yellow = LED(17)

button1 = Button(1) # green team
button2 = Button(7) # red team

while True:
    yellow.on()
    if button1.value == 0:
        yellow.off()
        green.on()
        red.off()
        print(f'Team Green wins')
        sleep(2)
        green.off()
    elif button2.value == 1:
        yellow.off()
        red.on()
        green.off()
        print(f'Team Red wins')
        sleep(2)
        red.off()


        