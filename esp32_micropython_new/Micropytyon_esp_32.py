import machine
import time
from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=2, echo_pin=0, echo_timeout_us=100000)




Buzzer= machine.Pin(15, machine.Pin.OUT)
led = machine.Pin(2, machine.Pin.OUT)
while True:
    Buzzer.value(1)
    led.value(1)
    time.sleep(0.5)
    led.value(0)
try:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
except OSError as ex:
    print('ERROR getting distance:', ex)