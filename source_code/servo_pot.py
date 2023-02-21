#Generic code for reading and displaying Analog Inputs values
import machine
from time import sleep
from machine import PWM, Pin

analog_port = machine.ADC(26)
pwm = PWM(Pin(7))
pwm.freq(50)

while True:
    servo = analog_port.read_u16()
    print(servo)
    pwm.duty_u16(int(1000 + servo/65365 * 7200))
    sleep(0.1)