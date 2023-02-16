from picozero import DigitalInputDevice as DID
from time import sleep

touch = DID(10) #GPIO 10

while True:
    if touch.value ==1:
        print(f'Touched!')
        sleep(1)
    else:
        print(f'Untouched')
        sleep(1)