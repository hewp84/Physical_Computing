from picozero import DigitalInputDevice as DID
from time import sleep

sensor = DID(7)  #GPIO 7

while True:
    if sensor.value == 0:
        print("Low signal")
        sleep(1)
    else:
        print("High signal")
        sleep(1)
    