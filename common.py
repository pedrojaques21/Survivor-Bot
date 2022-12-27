#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from urandom import randint, choice
from array import *

ev3 = EV3Brick()

gun = Motor(Port.A)
left_leg = Motor(Port.B)
right_leg = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)
#gyro_sensor = GyroSensor(Port.S2)
right_shoulder = TouchSensor(Port.S3)
left_shoulder = TouchSensor(Port.S2)
eyes = UltrasonicSensor(Port.S4)

#Variables

BACK_DISTANCE = -200
DRIVE_DISTANCE = 200
POSSIBLE_MOVEMENTS = ['FRONT', 'BACK', 'RIGHT', 'LEFT', 'DOUBLE']
POSSIBLE_DOUBLE = ['FRONT-FRONT','FRONT-RIGHT','FRONT-LEFT','BACK-BACK','BACK-RIGHT','BACK-LEFT','LEFT-LEFT',
    'LEFT-FRONT','LEFT-BACK','RIGHT-RIGHT','RIGHT-FRONT','RIGHT-BACK']
POSSIBLE_ATTACKS = ['STUN'] # SHOT only joins array when the bullet is found!

line_counter = 0
column_counter = 0
plays_counter = 0
motorcycle_parts_counter = 0

run_front = 0
run_back = 0
run_left = 0
run_right = 0

left_object_1 = 0
left_object_2 = 0
left_object_3 = 0
left_object_4 = 0

right_object_1 = 0
right_object_2 = 0
right_object_3 = 0
right_object_4 = 0

front_object_1 = 0
front_object_2 = 0
front_object_3 = 0
front_object_4 = 0

back_object_1 = 0
back_object_2 = 0
back_object_3 = 0
back_object_4 = 0
