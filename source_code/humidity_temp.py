from machine import Pin
from time import sleep
import dht #Importing library
 
sensor = dht.DHT11(Pin(2)) #GPIO 2
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f'Temperature: {temp:.1f} °C   Humidity: {hum:.1f} %')
    #print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    sleep(2)