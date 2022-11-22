#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#import numpy as np
import random as rand

# Create your objects here - initialize objects
ev3 = EV3Brick()

left_arm_motor = Motor(Port.A)
left_leg = Motor(Port.B)
right_leg = Motor(Port.C)


color_sensor = ColorSensor(Port.S1)
gyro_sensor = GyroSensor(Port.S2)
right_shoulder = TouchSensor(Port.S3)
eyes = UltrasonicSensor(Port.S4)

robot = DriveBase(left_leg, right_leg, 25, 105)

#Variables
DRIVE_DISTANCE = 200

POSSIBLE_PLAYS = np.array(['RECON', 'ATTACK', 'MOVEMENT'])
POSSIBLE_ATTACKS = np.array(['SHOT', 'STUN'])

matrix_map = np.array([
    ['Robot',2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,'Hornet']])

# Write your program here.

def move_front:
    #verifica a posição na matriz
    robot.straight(DRIVE_DISTANCE)#movimentar em frente
    #atualiza a posição na matriz

def move_back:
    robot.straight(-180)

def move_left:
    robot.turn(90)
    robot.straight(DRIVE_DISTANCE)

def move_right:
    robot.turn(-90)
    robot.straight(DRIVE_DISTANCE)

def random_movement:
    possible_movements = np.array(['FRONT', 'BACK', 'RIGHT', 'LEFT'])

    movement = rand.choice(possible_movements)

    match movement:
        case 'FRONT':
            move_front()
        case 'BACK':
            move_back()
        case 'RIGHT':
            move_right()
        case 'LEFT':
            move_left()
        case _:
            return 0

# Write your program here.
if right_shoulder.pressed():
    play = rand.choice(POSSIBLE_PLAYS)

    match play:
        case 'RECON':
            return 1
        case 'ATTACK':
            return 2
        case 'MOVEMENT':
            return 3
        case _:
            return 0
