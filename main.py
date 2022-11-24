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
DRIVE_SPEED = 100

POSSIBLE_PLAYS = ['RECON', 'MOVEMENT', 'ATTACK'] # Attack move only joins possible plays when zombie is dettected
POSSIBLE_ATTACKS = ['STUN'] # SHOT only joins array when bullet is found

matrix_map = [
    ['Robot',2,3,4,5,'Zombie'],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    ['Zombie',2,3,4,5,'Hornet']]

# Write your program here.

def move_front():
    #verifica a posição na matriz
    robot.drive(DRIVE_SPEED)#movimentar em frente
    if color_sensor.color() == Color.BLACK:
        robot.stop()
    #atualiza a posição na matriz

def move_back():
    robot.straight(-180)

def move_left():
    robot.turn(127.5)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(-135)

def move_right():
    robot.turn(-127.5)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(135)

def random_movement():
    possible_movements = ['FRONT', 'BACK', 'RIGHT', 'LEFT']

    movement = choice(possible_movements)

    if movement == 'FRONT':
        move_front()
        update_robot_position()
    elif movement == 'BACK':
        move_back()
    elif movement == 'RIGHT':
        move_right()
    elif movement == 'LEFT':
        move_left()

def update_robot_position():
    matrix_map[0][0] = 0
    matrix_map[1][0] = 'Robot'

def shot():
    #only shots if a bullet has been found
    #left_arm_motor shots a ball
    return 0

def random_attack():
    attack = choice(POSSIBLE_ATTACKS)
    return 0

# Write your program here.
while(True):
    if right_shoulder.pressed():
        print('pressed') # DELETE LATER
        play = choice(POSSIBLE_PLAYS)
        print(play)
        if play == 'RECON':
            #does recognizion move
            ev3.speaker.play_file(SoundFile.YES)
        elif play == 'ATTACK':
            #random_attack()
            ev3.speaker.play_file(SoundFile.KUNG_FU)
        elif play == 'MOVEMENT':
            random_movement()
