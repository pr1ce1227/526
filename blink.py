from machine import Pin
from utime import sleep


pin0 = Pin(0, Pin.OUT)
pin1 = Pin(1, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin3 = Pin(3, Pin.OUT)



print("LED starts flashing...")
idx = 0
while True:
    try:
        if(idx == 0):
            pin0.on()
            pin1.off()
            pin2.off()
            pin3.off()
            sleep(1)
        elif(idx == 1):
            pin0.off()
            pin1.on()
            pin2.off()
            pin3.off()
            sleep(1)
        elif(idx == 2):
            pin0.off()
            pin1.off()
            pin2.on()
            pin3.off()
            sleep(1)
        elif(idx == 3):
            pin0.off()
            pin1.off()
            pin2.off()
            pin3.on()
            sleep(1)
        idx = (idx + 1) % 4
    except KeyboardInterrupt:
        break

pin0.off()
pin1.off()
pin2.off()
pin3.off()

print("Finished.")