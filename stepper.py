from machine import Pin
from utime import sleep


class Stepper:
    def __init__(self, pin0, pin1, pin2, pin3):
        self.pin0 = pin0
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.step = 0
        self.steps = 0
        self.clockwise = 0
        self.speed = .001
        self.step_sequence = [
            [0, 1, 1, 1],
            [0, 0, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 0]
        ]

    def set_steps(self, steps):
        self.steps = steps
    
    def set_clockwise(self, clockwise):
        self.clockwise = clockwise

    def set_speed(self, speed):
        self.speed = speed
    
    def move(self):
        if(self.clockwise):
            self.step = (self.step + 1) % 8
        else:
            self.step = (self.step - 1) % 8
        self.pin0.value(self.step_sequence[self.step][0])
        self.pin1.value(self.step_sequence[self.step][1])
        self.pin2.value(self.step_sequence[self.step][2])
        self.pin3.value(self.step_sequence[self.step][3])

    def run(self):
        for i in range(self.steps):
            self.move()
            sleep(.001)
    
    def stop(self):
        self.pin0.off()
        self.pin1.off()
        self.pin2.off()
        self.pin3.off()

    




