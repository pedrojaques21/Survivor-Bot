#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here - initialize objects
ev3 = EV3Brick()

left_arm_motor = Motor(Port.A)
left_leg = Motor(Port.B)
right_leg = Motor(Port.C)

color_sensor = ColorSensor(Port.S1)
right_shoulder = TouchSensor(Port.S3)
eyes = UltrasonicSensor(Port.S4)

robot = DriveBase(left_leg, right_leg, 25, 105)

# Write your program here.

robot.drive(200, 0) # changing the speed requires changing the wait on line 31

while eyes.distance() > 100:

    color = color_sensor.color()
    print(color)

    if color == Color.BLACK: # limit of the square reached 
        wait(380) # amount of time to wait until robot reaches middle of the square in the matrix
        robot.stop()
        ev3.speaker.say('MY NAME IS AN TE RO')
        robot.drive_time(0, 51, 2000)
        robot.drive(200, 0)