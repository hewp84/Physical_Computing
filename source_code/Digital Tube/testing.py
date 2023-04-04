import time
import tm1650_lib as tm1650
from machine import Pin

tm1650.init()

while True:
    for i in range(0, 9999):
        tm1650.ShowNum(i)
        time.sleep(0.01)
