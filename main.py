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
DRIVE_DISTANCE = 180

POSSIBLE_PLAYS = ['RECON', 'MOVEMENT', 'ATTACK'] # Attack move only joins possible plays when zombie is dettected
POSSIBLE_MOVEMENTS = ['FRONT', 'BACK', 'RIGHT', 'LEFT', 'DOUBLE']
POSSIBLE_DOUBLE = ['FRONT-FRONT','FRONT-RIGHT','FRONT-LEFT','BACK-BACK','BACK-RIGHT','BACK-LEFT','LEFT-LEFT','LEFT-FRONT','LEFT-BACK','RIGHT-RIGHT','RIGHT-FRONT','RIGHT-BACK']
POSSIBLE_ATTACKS = ['STUN'] # SHOT only joins array when bullet is found

'''
matrix_map = [
    ['Robot',2,3,4,5,'Zombie'],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    ['Zombie',2,3,4,5,'Hornet']]


MAX_LINES = 5
MAX_COLUMNS = 5

'''

line_counter = 0
column_counter = 0
plays_counter = 0

# Write your program here.

def move_front():
    global line_counter
    robot.straight(180)
    #atualiza a line_counter
    line_counter = line_counter + 1

def move_back():
    global line_counter
    robot.straight(-180)
    #atualiza a line_counter
    line_counter = line_counter - 1

def move_left():
    global column_counter
    robot.turn(-127.5)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(135)
    #atualiza a column_counter
    column_counter = column_counter + 1

def move_right():
    global column_counter
    robot.turn(127.5)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(-135)
    #atualiza a column_counter
    column_counter = column_counter - 1

def move_double():
    double = choice(POSSIBLE_DOUBLE)

    if double == 'FRONT-FRONT':
        #possible movement when line = 0,1,2,3
        move_front()
        move_front()
    elif double == 'FRONT-RIGHT':
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        move_front()
        move_right()
    elif double == 'FRONT-LEFT':
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        move_front()
        move_left()
    elif double == 'BACK-BACK':
        #possible movement when line = 2,3,4 and column = 0,1,2,3,4,5
        move_back()
        move_back()
    elif double == 'BACK-RIGHT':
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        move_back()
        move_right()
    elif double == 'BACK-LEFT':
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        move_back()
        move_left()
    elif double == 'LEFT-LEFT':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3
        move_left()
        move_left()
    elif double == 'LEFT-FRONT':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3,4
        move_left()
        move_front()
    elif double == 'LEFT-BACK':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3,4,5
        move_left()
        move_back()
    elif double == 'RIGHT-RIGHT':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3,4,5
        move_right()
        move_right()
    elif double == 'RIGHT-FRONT':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3,4,5
        move_right()
        move_front()
    elif double == 'RIGHT-BACK':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3,4,5
        move_right()
        move_back()


def random_movement():
    movement = choice(POSSIBLE_MOVEMENTS)

    if movement == 'FRONT':
        if line_counter != 5:
            move_front()
        else:
            print ('not front')
            return random_movement()
            
    elif movement == 'BACK':
        if line_counter != 0:
            move_back()
        else:
            print ('not back')
            return random_movement()
        
    elif movement == 'RIGHT':
        if column_counter != 0:
            move_right()
        else:
            print ('not right')
            return random_movement()
        
    elif movement == 'LEFT':
        if column_counter != 5:
            move_left()
        else:
            print ('not left')
            return random_movement()
    elif movement == 'DOUBLE':
        move_double()


'''
def update_robot_position():
    matrix_map[0][0] = 0
    matrix_map[1][0] = 'Robot'
'''

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
            print(line_counter)
            print(column_counter)
