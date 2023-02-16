from picozero import DigitalInputDevice as DID, Buzzer
from time import sleep
#Photointerrupter sensor
phi = DID(7) #GPIO 7
#Add some fun to the output by generating a beep
buzz = Buzzer(12) # GPIO 12
counter = 0
last = 0
#state = 0
while True:
    state = phi.value
    if phi.value != last:
        if state == 1:
            counter += 1
            print(counter)
            buzz.on()
            sleep(1)
            buzz.off()
    last = state