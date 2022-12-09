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
#gyro_sensor = GyroSensor(Port.S2)
right_shoulder = TouchSensor(Port.S3)
eyes = UltrasonicSensor(Port.S4)

robot = DriveBase(left_leg, right_leg, 25, 105)

robot.settings(190, 100, 190, 100)

#Variables
DRIVE_DISTANCE = 200
POSSIBLE_PLAYS = ['RECON', 'MOVEMENT', 'MOVEMENT', 'MOVEMENT'] # Attack move only joins possible plays when zombie is dettected
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
    robot.turn(-128)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(135)
    #atualiza a column_counter
    column_counter = column_counter + 1

def move_right():
    global column_counter
    robot.turn(128)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(-135)
    #atualiza a column_counter
    column_counter = column_counter - 1

def move_double():
    double = choice(POSSIBLE_DOUBLE)

    if double == 'FRONT-FRONT':
        #possible movement when line = 0,1,2,3 and column = 0,1,2,3,4,5
        if line_counter < 4:
            move_front()
            move_front()
        else :
            return move_double()
    elif double == 'FRONT-RIGHT':
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        if (line_counter < 5 and column_counter > 0 ):
            move_front()
            move_right()
        else:
            return move_double()
    elif double == 'FRONT-LEFT':
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        if (line_counter < 5 and column_counter < 5) :
            move_front()
            move_left()
        else:
            return move_double()
    elif double == 'BACK-BACK':
        #possible movement when line = 2,3,4,5 and column = 0,1,2,3,4,5
        if line_counter > 1:
            move_back()
            move_back()
        else :
            return move_double()
    elif double == 'BACK-RIGHT':
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        if (line_counter > 0 and column_counter > 0 ):
            move_back()
            move_right()
        else :
            return move_double()
    elif double == 'BACK-LEFT':
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        if (line_counter > 0 and column_counter < 5):
            move_back()
            move_left()
        else :
            return move_double()
    elif double == 'LEFT-LEFT':
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3
        if column_counter < 4:
            move_left()
            move_left()
        else :
            return move_double()
    elif double == 'LEFT-FRONT':
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        if (line_counter < 5 and column_counter < 5) :
            move_left()
            move_front()
        else : 
            return move_double()
    elif double == 'LEFT-BACK':
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        if (line_counter > 0 and column_counter < 5) :
            move_left()
            move_back()
        else :
            return move_double()
    elif double == 'RIGHT-RIGHT':
        #possible movement when line = 0,1,2,3,4,5 and column = 2,3,4,5
        if column_counter > 1:
            move_right()
            move_right()
        else :
            return move_double()
    elif double == 'RIGHT-FRONT':
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        if (line_counter < 5 and column_counter > 0 ): 
            move_right()
            move_front()
        else: 
            return move_double()
    elif double == 'RIGHT-BACK':
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        if (line_counter > 0 and column_counter >0 ): 
            move_right()
            move_back()
        else:
            return move_double()

def random_movement():
    movement = choice(POSSIBLE_MOVEMENTS)

    if movement == 'FRONT':
        if line_counter < 5:
            move_front()
        else:
            print ('Can not go front!')
            return random_movement()
            
    elif movement == 'BACK':
        if line_counter > 0:
            move_back()
        else:
            print ('Can not go back!')
            return random_movement()
        
    elif movement == 'RIGHT':
        if column_counter > 0:
            move_right()
        else:
            print ('Can not go right!')
            return random_movement()
        
    elif movement == 'LEFT':
        if column_counter < 5:
            move_left()
        else:
            print ('Can not go left!')
            return random_movement()
    elif movement == 'DOUBLE':
        move_double()


'''
def update_robot_position():
    matrix_map[0][0] = 0
    matrix_map[1][0] = 'Robot'
'''

def smell(color):
    
    global POSSIBLE_PLAYS

    if(color == Color.BLUE):     #Color Blue detected, Zombie is 2 blocks away
        print(color)
        ev3.speaker.say('Zombie close')
        wait(2000)
    if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
        POSSIBLE_PLAYS.append('ATTACK') # Zombie is 1 block away so the Attack movement is added to de possible plays array
        print('Recon ' + str(color))                                
        ev3.speaker.say('Zombie very close')
        wait(2000)
    
    return 0

def shot():
    left_arm_motor.run_time(700,3000)
    return 0

def stun():
    left_arm_motor.run_time(700,3000)
    return 0

def random_attack():
    attack = choice(POSSIBLE_ATTACKS)

    if attack == 'STUN':
        ev3.speaker.play_file(SoundFile.KUNG_FU)
    elif attack == 'SHOT':
        shot()
    return 0

def recon():
    if(eyes.distance() <= 370):
        print('Objeto - 1 casas')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas')  

def random_recon():
    print(eyes.distance())
    #Robot in column 0 (cant recon right)
    if (column_counter == 0):
        #Robot in column 0 and line 0 (cant recon right or back)
        if(line_counter == 0):
            #recon front
            print('Front:')
            recon()
            #turn left
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Left:')
            recon()
            wait(1500)
            #turn front
            robot.turn(130)

        #Robot in column 0 and line 5 (cant recon right or front)
        if(line_counter == 5):
            #turn left
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Left:')
            recon()
            wait(1500)
            #turn back
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Back:')
            recon()
            wait(1500)
            #turn front
            robot.turn(-260)
            wait(1500)

        #Robot in column 0 but not in line 0 or 5 (cant recon right)
        if(line_counter != 5 and line_counter != 0):
            #recon fornt
            print('Front:')
            recon()
            wait(1500)
            #turn left
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Left:')
            recon()
            wait(1500)
            #turn back
            robot.turn(-130)
            wait(1500)
            #recon back
            print('Back:')
            recon()
            wait(1500)
            #turn front
            robot.turn(260)
            wait(1500)    

    #Robot in column 5 (cant recon left)
    if (column_counter == 5):
        #Robot in column 5 and line 0 (cant recon left or back)
        if (line_counter == 0):
            #recon front
            print('Front:')
            recon()
            wait(1500)
            #turn right
            robot.turn(130)
            wait(1500)
            #recon right
            print('Right:')
            recon()
            wait(1500)
            #turn front
            robot.turn(-130)
            wait(1500)

        #Robot in column 5 and line 5 (cant recon left or front)
        if (line_counter == 5):
            #turn right
            robot.turn(130)
            wait(1500)
            #recon right
            print('Right:')
            recon()
            wait(1500)
            #turn back
            robot.turn(130)
            wait(1500)
            #recon back
            print('Back:')
            recon()
            wait(1500)
            #turn front
            robot.turn(-260)
            wait(1500)
            
        #Robot in column 5 and not in line 5 or 0 (cant recon left)
        if(line_counter != 5 and line_counter != 0):
            #recon front
            print('Front:')
            recon()
            wait(1500)
            #turn right
            robot.turn(130)
            wait(1500)
            #recon right
            print('Right:')
            recon()
            wait(1500)
            #turn back
            robot.turn(130)
            wait(1500)
            #recon back
            print('Back:')
            recon()
            wait(1500)
            #turn front
            robot.turn(-260)
            wait(1500)

    if (line_counter == 0 and column_counter != 0 and column_counter != 5):
        #recon front
        print('Front:')
        recon()
        wait(1500)
        #turn right
        robot.turn(130)
        wait(1500)
        #recon right
        print('Right:')
        recon()
        wait(1500)
        #turn left
        robot.turn(-260)
        wait(1500)
        #recon left
        print('Left:')
        recon()
        wait(1500)
        #turn front
        robot.turn(130)
        wait(1500)
        
    if (line_counter == 5 and column_counter != 0 and column_counter != 5):
        #turn right
        robot.turn(130)
        wait(1500)
        #recon right
        print('Right:')
        recon()
        wait(1500)
        #turn back
        robot.turn(130)
        wait(1500)
        #recon back
        print('Back:')
        recon()
        wait(1500)
        #turn left
        robot.turn(130)
        wait(1500)
        #recon left
        print('Left:')
        recon()
        wait(1500)
        #turn front
        robot.turn(130)
        wait(1500)
        
    if (line_counter != 5 and line_counter != 0 and column_counter != 0 and column_counter != 5):
        #recon front
        print('Front:')
        recon()
        wait(1500)
        #turn right
        robot.turn(130)
        wait(1500)
        #recon right
        print('Right:')
        recon()
        wait(1500)
        #turn back
        robot.turn(130)
        wait(1500)
        #recon back
        print('Back:')
        recon()
        wait(1500)
        #turn left
        robot.turn(130)
        wait(1500)
        #recon left
        print('Left:')
        recon()
        wait(1500)
        #turn front
        robot.turn(130)
        wait(1500)

def detect_bullet(color):
    if(color == Color.YELLOW):     #Color yellow detected, bullet
        print(color)
        ev3.speaker.say('Bullet found')
        wait(2000)

def detect_motorcycle_part(color): 
    if(color == Color.GREEN):     #Color green detected, motorcycle part
        print(color)
        ev3.speaker.say('Motorcycle part found')
        wait(2000)
        
# Write your program here.
while(True):
    if right_shoulder.pressed():
        print(right_leg.angle())
        print(left_leg.angle())
        print('Starting play - Right Shoulder pressed') # DELETE LATER

        play = choice(POSSIBLE_PLAYS)

        print('I am going to '+ play)

        if play == 'RECON':
            ev3.speaker.say('DOING RECON')
            random_recon()
        elif play == 'ATTACK':
            ev3.speaker.say('ATTACKING')
            random_attack()
        elif play == 'MOVEMENT':
            ev3.speaker.say('ON MY WAY')
            random_movement()
            print('My position is: ' + str(line_counter) + ', ' + str(column_counter))

        plays_counter = plays_counter + 1
        
        color = color_sensor.color()
        print(color)
        smell(color)
        detect_bullet(color)
        detect_motorcycle_part(color)