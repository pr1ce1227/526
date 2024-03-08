from machine import *
import time
from stepper import Stepper

pin0 = Pin(0, Pin.OUT)
pin1 = Pin(1, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin3 = Pin(3, Pin.OUT)


print("Spin stepper motor...")
stepper = Stepper(pin0, pin1, pin2, pin3)
while True:
    try:
        stepper.set_steps(1000)
        stepper.set_clockwise(1)
        stepper.run()
        stepper.stop()
        stepper.set_clockwise(0)
        stepper.run()
        print("Finished.")
    except KeyboardInterrupt:
        break
