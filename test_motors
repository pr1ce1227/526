from machine import *
import time
from stepper import Stepper

pin0 = Pin(0, Pin.OUT)
pin1 = Pin(1, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin3 = Pin(3, Pin.OUT)
pin4 = Pin(4, Pin.OUT)
pin5 = Pin(5, Pin.OUT)
pin6 = Pin(6, Pin.OUT)
pin7 = Pin(7, Pin.OUT)
stepper = Stepper(pin0, pin1, pin2, pin3)


try:
    # print("Drive Straight...")
    # pin4.off()
    # pin5.on()
    # pin6.on()
    # pin7.off()

    # time.sleep(3)
    # print("Drive Backwards...")
    # pin4.on()
    # pin5.off()
    # pin6.off()
    # pin7.on()

    # time.sleep(3)

    # print("Turn Left...")
    # pin4.on()
    # pin5.off()
    # pin6.on()
    # pin7.off()

    # time.sleep(3)

    # print("Turn right...")
    # pin4.off()
    # pin5.on()
    # pin6.off()
    # pin7.on()

    # time.sleep(3)

    # print("Stop wheels...")
    # pin4.off()
    # pin5.off()
    # pin6.off()
    # pin7.off()

    # time.sleep(3)

    # print("Turn wheels right then left...")
    # stepper.set_steps(500)
    # stepper.set_clockwise(1)
    # stepper.run()
    # stepper.stop()
    # stepper.set_clockwise(0)
    # stepper.run()
    # print("Finished.")


    print("Turn wheels right then left...")
    stepper.set_steps(1000)
    stepper.set_clockwise(1)
    stepper.run()
    stepper.stop()

    print("Drive Straight...")
    pin4.off()
    pin5.on()
    pin6.on()
    pin7.off()
    time.sleep(1)

    stepper.set_steps(2000)
    stepper.set_clockwise(0)
    stepper.run()
    stepper.stop()

    time.sleep(3)

    print("Drive Straight...")
    pin4.off()
    pin5.on()
    pin6.on()
    pin7.off()
    time.sleep(1)
    
except KeyboardInterrupt:
    pin4.off()
    pin5.off()
    pin6.off()
    pin7.off()

    pin4.off()
    pin5.off()
    pin6.off()
    pin7.off()

