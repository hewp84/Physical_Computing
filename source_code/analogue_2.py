#Generic code for reading and displaying Analog Inputs values
import machine
from time import sleep

analog_port = machine.ADC(26)

while True:
    value = analog_port.read_u16()
    print(value)
    sleep(0.4)