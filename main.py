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

from attack import *
from smell import *
from heuristica import *

#Defining Robotics
ev3 = EV3Brick()

gun = Motor(Port.A)
left_leg = Motor(Port.B)
right_leg = Motor(Port.C)
color_sensor = ColorSensor(Port.S1)
left_shoulder = TouchSensor(Port.S2)
right_shoulder = TouchSensor(Port.S3)
eyes = UltrasonicSensor(Port.S4)

start = [0,0]
goal = [5,5]

robot = DriveBase(left_leg, right_leg, 25, 105)
robot.settings(190, 100, 190, 100)

#Constants
BACK_DISTANCE = -200
DRIVE_DISTANCE = 200

POSSIBLE_MOVEMENTS = ['FRONT', 'BACK', 'RIGHT', 'LEFT', 'DOUBLE']
POSSIBLE_DOUBLE = ['FRONT-FRONT','FRONT-RIGHT','FRONT-LEFT','BACK-BACK','BACK-RIGHT','BACK-LEFT','LEFT-LEFT',
    'LEFT-FRONT','LEFT-BACK','RIGHT-RIGHT','RIGHT-FRONT','RIGHT-BACK']
POSSIBLE_ATTACKS = ['STUN'] # SHOT only joins array when the bullet is found!

#Variables
plays_counter = 0

left_object = 0
right_object = 0
front_object = 0
back_object = 0

run_left = 0
run_front = 0
run_back = 0
run_right = 0

parts_counter = 0
parts_moto = 0

robot_position = [0,0] #coordinates x, y

map = [
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0']]

#map view
#   ------------------------------->x(represents columns)
#   |
#   |
#   |
#   |
#   |
#   |
#   y(represents lines)

def detect_bullet():

    global POSSIBLE_ATTACKS, color_sensor
    color = color_sensor.color()
    if(color == Color.BROWN or color == Color.YELLOW): # Color detected, BROWN OR YELLOW because of the lightning
        print("Color detected: " + str(color))
        ev3.speaker.say('Bullet found!')
        POSSIBLE_ATTACKS.append('SHOT')
        wait(2000)

def detect_motorcycle_part(): 

    global parts_counter
    if(parts_counter == 0):
        color = color_sensor.color()
        if(color == Color.GREEN):     #Color green detected, motorcycle part
            print(color)
            ev3.speaker.say('Motorcycle part found!')
            ev3.speaker.play_file(SoundFile.CHEERING)
            parts_counter = parts_counter + 1
            print('Parts found: ' + str(parts_counter))
            wait(2000)
            goal = [5,5]
    else:
        ev3.speaker.say('Already have motorcycle part')


def shot():
    gun.run_time(700,3000)
    return 0

def stun():
    gun.run_time(700,4000)
    return 0

def random_attack():
    attack = choice(POSSIBLE_ATTACKS)
    print ('ATTACK: ' + str(attack))
    if attack == 'STUN':
        ev3.speaker.play_file(SoundFile.KUNG_FU)
        stun()
        wait(1000)
    else:
        ev3.speaker.play_file("gun_shot.wav")
        shot()
        wait(1000)

def update_robot_position (lines,columns):
    map[lines][columns] = 'robot'

def reset_robot_position (lines, columns):
    map[lines][columns] = '0'


def update_matrix_info(x,y):
    map[y][x]='object'

def recon_right():
    global right_object
    if(eyes.distance() <= 370):
        if(robot_position[0]>=1):
            print('Objeto - 1 casas - Right')
            right_object = 1
            update_matrix_info(robot_position[0]-1, robot_position[1])
            #update_data_matrix('right')
      
    if(eyes.distance()>=380 and eyes.distance()<=640):
        if(robot_position[0]>=2):
            print('Objeto - 2 casas - Right')
            right_object = 2
            update_matrix_info(robot_position[0]-2, robot_position[1])
            #update_data_matrix('right')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        if(robot_position[0]>=3):
            print('Objeto - 3 casas - Right')
            right_object = 3
            update_matrix_info(robot_position[0]-3, robot_position[1])
            #update_data_matrix('right')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        if(robot_position[0]>=4):
            print('Objeto - 4 casas - Right')  
            right_object = 4
            update_matrix_info(robot_position[0]-4, robot_position[1])
            #update_data_matrix('right')

    return 0

def recon_left():
    global left_object
    
    if(eyes.distance() <= 370):
        if(robot_position[0]<=4):
            print('Objeto - 1 casas - Left')
            left_object = 1
            update_matrix_info(robot_position[0]+1, robot_position[1])
            #update_data_matrix('left') 
    if(eyes.distance()>=380 and eyes.distance()<=640):
        if(robot_position[0]<=3):
            print('Objeto - 2 casas - Left')
            left_object = 2
            update_matrix_info(robot_position[0]+2, robot_position[1])
            #update_data_matrix('left')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        if(robot_position[0]<=2):
            print('Objeto - 3 casas - Left')
            left_object = 3
            update_matrix_info(robot_position[0]+3, robot_position[1])
            #update_data_matrix('left')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        if(robot_position[0]<=1):
            print('Objeto - 4 casas - Left')  
            left_object = 4
            update_matrix_info(robot_position[0]+4, robot_position[1])
            #update_data_matrix('left')

    return 0

def recon_front():
    global front_object
    
    if(eyes.distance() <= 370):
        if(robot_position[1]<=4):
            print('Objeto - 1 casas - Front')
            front_object = 1
            update_matrix_info(robot_position[0], robot_position[1]+1)
            #update_data_matrix('front')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        if(robot_position[1]<=3):
            print('Objeto - 2 casas - Front')
            front_object = 2
            update_matrix_info(robot_position[0], robot_position[1]+2)
        # update_data_matrix('front')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        if(robot_position[1]<=2):
            print('Objeto - 3 casas - Front')
            front_object = 3
            update_matrix_info(robot_position[0], robot_position[1]+3)
            #update_data_matrix('front')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        if(robot_position[1]<=1):
            print('Objeto - 4 casas - Front')  
            front_object = 4
            update_matrix_info(robot_position[0], robot_position[1]+4)
            #update_data_matrix('front')
    return 0

def recon_back():
    global back_object
    
    if(eyes.distance() <= 370):
        if(robot_position[1]>=1):
            print('Objeto - 1 casas - Back')
            back_object = 1
            update_matrix_info(robot_position[0], robot_position[1]-1)
            #update_data_matrix('back')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        if(robot_position[1]>=2):
            print('Objeto - 2 casas - Back')
            back_object = 2
            update_matrix_info(robot_position[0], robot_position[1]-2)
            #update_data_matrix('back')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        if(robot_position[1]>=3):
            print('Objeto - 3 casas - Back')
            back_object = 3
            update_matrix_info(robot_position[0], robot_position[1]-3)
            #update_data_matrix('back')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        if(robot_position[1]>=4):
            print('Objeto - 4 casas - Back')  
            back_object = 4
            update_matrix_info(robot_position[0], robot_position[1]-4)
            #update_data_matrix('back')

    return False

def move(f,r,b,l):

    global parts_counter
    global front_object, right_object, left_object, back_object
    global run_left, run_front, run_back, run_right

    auxF = 0
    auxL = 0
    auxB = 0
    auxR = 0
    aux = 0

    front_object = f
    right_object = r
    left_object = l
    back_object = b

    if (front_object != 0):
        auxF = 1
    if (right_object != 0):
        auxL = 1
    if (left_object != 0):
        auxB = 1
    if (back_object != 0):
        auxR = 1

    aux = auxF + auxB + auxL + auxR
    if(parts_counter == 0):
        if (aux == 1):
            if(front_object != 0):
                if(run_front == 0):
                    if(front_object == 1):
                        color = color_sensor.color()
                        if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            random_attack()
                            run_front = 1
                        else:
                            move_front()
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                    elif(front_object == 2):
                        color = color_sensor.color()
                        if(color == Color.BLUE):
                            wait(1000)
                            move_front()
                            color = color_sensor.color()
                            if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                                robot.straight(DRIVE_DISTANCE/2)
                                color = color_sensor.color()
                                if(color == Color.RED):
                                    print('Recon ' + str(color))                                
                                    ev3.speaker.say('Zombie very close')
                                    wait(2000)
                                    robot.straight(-DRIVE_DISTANCE/2)
                                    wait(1000)
                                    random_attack()
                                    run_front = 1
                                else:
                                    wait(1000)
                                    detect_motorcycle_part()
                                    detect_bullet()
                                    wait(1000)
                                    robot.straight(DRIVE_DISTANCE/2)
                            else:
                                robot.straight(DRIVE_DISTANCE/2)
                                wait(1000)
                                detect_motorcycle_part()
                                detect_bullet()
                                wait(1000)
                                robot.straight(DRIVE_DISTANCE/2)
                        else:
                            secure_movement()
                    elif (front_object ==3):
                        secure_movement()
                    else:
                        move_front()
                        move_front()
                else:
                    run_front = 0
                    if(robot_position[0] <4):
                        move_left()
                        move_left()
                    elif(robot_position[0] >4):
                        move_right()
                        move_right()
                    elif(robot_position[1] >4):
                        move_back()
                        move_back()
    #LEFT---------------------------------------------------------------------------------------------
            if(left_object != 0):
                if(run_left == 0):
                    if(left_object == 1):
                        color = color_sensor.color()
                        if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                            robot.turn(-128)
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            random_attack()
                            run_left = 1
                            robot.turn(128)
                        else:
                            move_left()
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                    elif(left_object == 2):
                        color = color_sensor.color()
                        if(color == Color.BLUE):
                            wait(1000)
                            move_left()
                            color = color_sensor.color()
                            if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                                robot.turn(-128)
                                robot.straight(DRIVE_DISTANCE/2)
                                color = color_sensor.color()
                                if(color == Color.RED):
                                    print('Recon ' + str(color))                                
                                    ev3.speaker.say('Zombie very close')
                                    wait(2000)
                                    robot.straight(-DRIVE_DISTANCE/2)
                                    wait(1000)
                                    random_attack()
                                    run_left = 1
                                    robot.turn(128)
                                else:
                                    wait(1000)
                                    detect_motorcycle_part()
                                    detect_bullet()
                                    wait(1000)
                                    robot.straight(DRIVE_DISTANCE/2)
                                    robot.turn(128)
                            else:
                                robot.turn(-128)
                                robot.straight(DRIVE_DISTANCE/2)
                                wait(1000)
                                detect_motorcycle_part()
                                detect_bullet()
                                wait(1000)
                                robot.straight(DRIVE_DISTANCE/2)
                                robot.turn(128)
                        else:
                            secure_movement()
                    elif (left_object ==3):
                        secure_movement()
                    else:
                        move_left()
                        move_left()
                else:
                    run_left = 0
                    if(robot_position[0] >4):
                        move_right()
                        move_right()
                    elif(robot_position[1] <4):
                        move_front()
                        move_front()
                    elif(robot_position[1] >4):
                        move_back()
                        move_back()
    #BACK-------------------------------------------------------------------------------------------------------
            if(back_object != 0):
                if(run_back == 0):
                    if(back_object == 1):
                        color = color_sensor.color()
                        if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                            robot.turn(-180)
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            random_attack()
                            run_back = 1
                            robot.turn(180)
                        else:
                            move_back()
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                    elif(back_object == 2):
                        color = color_sensor.color()
                        if(color == Color.BLUE):
                            wait(1000)
                            move_back()
                            color = color_sensor.color()
                            if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                                robot.turn(-180)
                                robot.straight(DRIVE_DISTANCE/2)
                                color = color_sensor.color()
                                if(color == Color.RED):
                                    print('Recon ' + str(color))                                
                                    ev3.speaker.say('Zombie very close')
                                    wait(2000)
                                    robot.straight(-DRIVE_DISTANCE/2)
                                    wait(1000)
                                    random_attack()
                                    run_back = 1
                                    robot.turn(180)
                                else:
                                    wait(1000)
                                    detect_motorcycle_part()
                                    detect_bullet()
                                    wait(1000)
                                    robot.straight(DRIVE_DISTANCE/2)
                                    robot.turn(180)
                            else:
                                robot.turn(-180)
                                robot.straight(DRIVE_DISTANCE/2)
                                wait(1000)
                                detect_motorcycle_part()
                                detect_bullet()
                                wait(1000)
                                robot.straight(DRIVE_DISTANCE/2)
                                robot.turn(180)
                        else:
                            secure_movement()
                    elif (back_object ==3):
                        secure_movement()
                    else:
                        move_back()
                        move_back()
                else:
                    run_back = 0
                    if(robot_position[0] <4):
                        move_left()
                        move_left()
                    elif(robot_position[0] >4):
                        move_right()
                        move_right()
                    elif(robot_position[1] <4):
                        move_front()
                        move_front()      
    #RIGHT-----------------------------------------------------------------------------------------------------
            if(right_object != 0):
                if (run_right == 0):
                    if(right_object == 1):
                        color = color_sensor.color()
                        if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                            robot.turn(128)
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            random_attack()
                            run_right = 1
                            robot.turn(-128)
                        else:
                            move_right()
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                    elif(right_object == 2):
                        color = color_sensor.color()
                        if(color == Color.BLUE):
                            wait(1000)
                            move_right()
                            color = color_sensor.color()
                            if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                                robot.turn(128)
                                robot.straight(DRIVE_DISTANCE/2)
                                color = color_sensor.color()
                                if(color == Color.RED):
                                    print('Recon ' + str(color))                                
                                    ev3.speaker.say('Zombie very close')
                                    wait(2000)
                                    robot.straight(-DRIVE_DISTANCE/2)
                                    wait(1000)
                                    random_attack()
                                    robot.turn(-128)
                                else:
                                    wait(1000)
                                    detect_motorcycle_part()
                                    detect_bullet()
                                    wait(1000)
                                    robot.straight(DRIVE_DISTANCE/2)
                                    robot.turn(-128)
                            else:
                                robot.turn(128)
                                robot.straight(DRIVE_DISTANCE/2)
                                wait(1000)
                                detect_motorcycle_part()
                                detect_bullet()
                                wait(1000)
                                robot.straight(DRIVE_DISTANCE/2)
                                robot.turn(-128)
                        else:
                            secure_movement()
                    elif (right_object ==3):
                        secure_movement()
                    else:
                        move_right()
                        move_right()
                else:
                    run_right = 0
                    if (robot_position[0] <4):
                        move_left()
                        move_left()
                    elif(robot_position[1] <4):
                        move_front()
                        move_front()
                    elif(robot_position[1] >4):
                        move_back()
                        move_back()
                
        if (aux >= 2):
            calc_heu()
        
        elif(aux == 0):
            color = color_sensor.color()
            if(color == Color.BLUE):
                if(parts_counter !=0 ):
                    if(robot_position[0] <4):
                        move_left()
                        move_left()
                    elif(robot_position[0] >4):
                        move_right()
                        move_right()
                    elif(robot_position[1] <4):
                        move_front()
                        move_front()
                    elif(robot_position[1] >4):
                        move_back()
                        move_back()
                else:
                    return 0
            else:
                print('I am going to move')
                ev3.speaker.say('ON MY WAY')
                moveTowardsGoal(robot_position,goal)
                print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1]))

    if(parts_counter != 0):
        if (aux == 1):
            if(front_object == 1):
                color = color_sensor.color()
                if(color == Color.BLUE):
                    if(robot_position[0] <5):
                        move_left()
                    elif(robot_position[0] >5):
                        move_right()
                    elif(robot_position[1] >5):
                        move_back()
                elif(color == Color.RED):
                    if(robot_position[0] <5):
                        move_left()
                    elif(robot_position[0] >5):
                        move_right()
                    elif(robot_position[1] >5):
                        move_back()
            elif(right_object == 1):
                color = color_sensor.color()
                if(color == Color.BLUE):
                    if(robot_position[0] >5):
                        move_front()
                    elif(robot_position[0] <5):
                        move_left()
                    elif(robot_position[1] >5):
                        move_back()
                elif(color == Color.RED):
                    if(robot_position[0] >5):
                        move_front()
                    elif(robot_position[0] <5):
                        move_left()
                    elif(robot_position[1] >5):
                        move_back()
            elif(back_object == 1):
                color = color_sensor.color()
                if(color == Color.BLUE):
                    if(robot_position[1] <5):
                        move_front()
                    elif(robot_position[0] <5):
                        move_left()
                    elif(robot_position[0] >5):
                        move_right()
                elif(color == Color.RED):
                    if(robot_position[1] <5):
                        move_front()
                    elif(robot_position[0] <5):
                        move_left()
                    elif(robot_position[0] >5):
                        move_right()
            elif(left_object == 1):
                color = color_sensor.color()
                if(color == Color.BLUE):
                    if(robot_position[1] <5):
                        move_front()
                    elif(robot_position[0] >5):
                        move_right()
                    elif(robot_position[1] >5):
                        move_back()
                elif(color == Color.RED):
                    if(robot_position[1] <5):
                        move_front()
                    elif(robot_position[0] >5):
                        move_right()
                    elif(robot_position[1] >5):
                        move_back()
            else:
                print('I am going to move')
                ev3.speaker.say('ON MY WAY')
                moveTowardsGoal(robot_position,goal)
                print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1]))

        elif (aux == 2):
            color = color_sensor.color()
            if(color == Color.BLUE):
                if (front_object == 2):
                    move_front()
                    color = color_sensor.color()
                    if (color == Color.RED):
                        robot.straight(DRIVE_DISTANCE/2)
                        color = color_sensor.color()
                        if(color == Color.RED):
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            robot.straight(-DRIVE_DISTANCE/2)
                            wait(1000)
                            random_attack()
                        else:
                            wait(1000)
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                            robot.straight(DRIVE_DISTANCE/2)
                    else:
                        robot.straight(DRIVE_DISTANCE/2)
                        wait(1000)
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        
                if (left_object == 2 ):
                    move_left()
                    color = color_sensor.color()
                    if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                        robot.turn(-128)
                        robot.straight(DRIVE_DISTANCE/2)
                        color = color_sensor.color()
                        if(color == Color.RED):
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            robot.straight(-DRIVE_DISTANCE/2)
                            wait(1000)
                            random_attack()
                            robot.turn(128)
                        else:
                            wait(1000)
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                            robot.straight(DRIVE_DISTANCE/2)
                            robot.turn(128)
                    else:
                        robot.turn(-128)
                        robot.straight(DRIVE_DISTANCE/2)
                        wait(1000)
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        robot.turn(128)
                    
                if (back_object == 2):
                    move_back()
                    color = color_sensor.color()
                    if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                        robot.turn(-180)
                        robot.straight(DRIVE_DISTANCE/2)
                        color = color_sensor.color()
                        if(color == Color.RED):
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            robot.straight(-DRIVE_DISTANCE/2)
                            wait(1000)
                            random_attack()
                            robot.turn(180)
                        else:
                            wait(1000)
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                            robot.straight(DRIVE_DISTANCE/2)
                            robot.turn(180)
                    else:
                        robot.turn(-180)
                        robot.straight(DRIVE_DISTANCE/2)
                        wait(1000)
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        robot.turn(180)
                        
                if (right_object == 2 ):
                    move_right()
                    color = color_sensor.color()
                    if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
                        robot.turn(128)
                        robot.straight(DRIVE_DISTANCE/2)
                        color = color_sensor.color()
                        if(color == Color.RED):
                            print('Recon ' + str(color))                                
                            ev3.speaker.say('Zombie very close')
                            wait(2000)
                            robot.straight(-DRIVE_DISTANCE/2)
                            wait(1000)
                            random_attack()
                            run_right = 1
                            robot.turn(-128)
                        else:
                            wait(1000)
                            detect_motorcycle_part()
                            detect_bullet()
                            wait(1000)
                            robot.straight(DRIVE_DISTANCE/2)
                            robot.turn(-128)
                    else:
                        robot.turn(128)
                        robot.straight(DRIVE_DISTANCE/2)
                        wait(1000)
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        robot.turn(-128)
                    
            else:
                print('I am going to move')
                ev3.speaker.say('ON MY WAY')
                moveTowardsGoal(robot_position,goal)
                print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1]))  

        else:
            print('I am going to move')
            ev3.speaker.say('ON MY WAY')
            moveTowardsGoal(robot_position,goal)
            print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1]))

    front_object = 0
    right_object = 0
    left_object = 0
    back_object = 0
    
def calc_heu():

    global front_object, right_object, left_object, back_object

    auxFO = front_object
    auxLO = left_object
    auxBO = back_object
    auxRO = right_object
    
    if (front_object == 0):
        auxFO = auxFO + 10
    if (right_object == 0):
        auxRO = auxRO + 10
    if (left_object == 0):
        auxLO = auxLO + 10
    if (back_object == 0):
        auxBO = auxBO + 10
    
    numbers = [auxFO, auxRO, auxLO, auxBO]
    perto = min(numbers)
#f,r,b,l
    if (front_object == perto):
        move(front_object,0,0,0)
    
    elif (left_object == perto):
        move(0,0,0,left_object)

    elif (right_object == perto):
        move(0,right_object,0,0)
    
    elif (back_object == perto):
        move(0,0,back_object,0)
        
def secure_movement():
    if(front_object >= 2 ):
        print("!! moving one block, because zombie might be nearby !!")
        ev3.speaker.say('BE CAREFUL')
        move_front()

    elif (back_object >= 2):
        print("!! moving one block, because zombie might be nearby !!")
        ev3.speaker.say('BE CAREFUL')
        move_back()

    elif (left_object >= 2):
        print("!! moving one block, because zombie might be nearby !!")
        ev3.speaker.say('BE CAREFUL')
        move_left()

    elif (right_object >= 2):
        print("!! moving one block, because zombie might be nearby !!")
        ev3.speaker.say('BE CAREFUL')
        move_right()

def random_recon():
    #Robot in column 0 (cant recon right)
    if (robot_position[0] == 0):
        #Robot in column 0 and line 0 (cant recon right or back)
        if(robot_position[1] == 0):
            wait(1500)
            #recon front
            print('Recon Front:')
            recon_front()
            #turn left
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Recon Left:')
            recon_left()
            wait(1500)
            #turn front
            robot.turn(130)

        #Robot in column 0 and line 5 (cant recon right or front)
        if(robot_position[1] == 5):
            #turn left
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Recon Left:')
            recon_left()
            wait(1500)
            #turn back
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Recon Back:')
            recon_back()
            wait(1500)
            #turn front
            robot.turn(-260)
            wait(1500)

        #Robot in column 0 but not in line 0 or 5 (cant recon right)
        if(robot_position[1] != 5 and robot_position[1] != 0):
            #recon fornt
            print('Recon Front:')
            recon_front()
            wait(1500)
            #turn left
            robot.turn(-130)
            wait(1500)
            #recon left
            print('Recon Left:')
            recon_left()
            wait(1500)
            #turn back
            robot.turn(-130)
            wait(1500)
            #recon back
            print('Recon Back:')
            recon_back()
            wait(1500)
            #turn front
            robot.turn(260)
            wait(1500)    

    #Robot in column 5 (cant recon left)
    if (robot_position[0] == 5):
        #Robot in column 5 and line 0 (cant recon left or back)
        if (robot_position[1] == 0):
            #recon front
            print('Recon Front:')
            recon_front()
            wait(1500)
            #turn right
            robot.turn(130)
            wait(1500)
            #recon right
            print('Recon Right:')
            recon_right()
            wait(1500)
            #turn front
            robot.turn(-130)
            wait(1500)

        #Robot in column 5 and line 5 (cant recon left or front)
        if (robot_position[1] == 5):
            #turn right
            robot.turn(130)
            wait(1500)
            #recon right
            print('Recon Right:')
            recon_right()
            wait(1500)
            #turn back
            robot.turn(130)
            wait(1500)
            #recon back
            print('Recon Back:')
            recon_back()
            wait(1500)
            #turn front
            robot.turn(-260)
            wait(1500)
            
        #Robot in column 5 and not in line 5 or 0 (cant recon left)
        if(robot_position[1] != 5 and robot_position[1] != 0):
            #recon front
            print('Recon Front:')
            recon_front()
            wait(1500)
            #turn right
            robot.turn(130)
            wait(1500)
            #recon right
            print('Recon Right:')
            recon_right()
            wait(1500)
            #turn back
            robot.turn(130)
            wait(1500)
            #recon back
            print('Recon Back:')
            recon_back()
            wait(1500)
            #turn front
            robot.turn(-260)
            wait(1500)

    if (robot_position[1] == 0 and robot_position[0] != 0 and robot_position[0] != 5):
        #recon front
        print('Recon Front:')
        recon_front()
        wait(1500)
        #turn right
        robot.turn(130)
        wait(1500)
        #recon right
        print('Recon Right:')
        recon_right()
        wait(1500)
        #turn left
        robot.turn(-260)
        wait(1500)
        #recon left
        print('Recon Left:')
        recon_left()
        wait(1500)
        #turn front
        robot.turn(130)
        wait(1500)
        
    if (robot_position[1] == 5 and robot_position[0] != 0 and robot_position[0] != 5):
        #turn right
        robot.turn(130)
        wait(1500)
        #recon right
        print('Recon Right:')
        recon_right()
        wait(1500)
        #turn back
        robot.turn(130)
        wait(1500)
        #recon back
        print('Recon Back:')
        recon_back()
        wait(1500)
        #turn left
        robot.turn(130)
        wait(1500)
        #recon left
        print('Recon Left:')
        recon_left()
        wait(1500)
        #turn front
        robot.turn(130)
        wait(1500)
        
    if (robot_position[1] != 5 and robot_position[1] != 0 and robot_position[0] != 0 and robot_position[0] != 5):
        #recon front
        print('Recon Front:')
        recon_front()
        wait(1500)
        #turn right
        robot.turn(130)
        wait(1500)
        #recon right
        print('Recon Right:')
        recon_right()
        wait(1500)
        #turn back
        robot.turn(130)
        wait(1500)
        #recon back
        print('Recon Back:')
        recon_back()
        wait(1500)
        #turn left
        robot.turn(130)
        wait(1500)
        #recon left
        print('Recon Left:')
        recon_left()
        wait(1500)
        #turn front
        robot.turn(130)
        wait(1500)


def move_front():
    global robot_position
    robot.straight(180)
    #atualiza a robot_position[1]
    robot_position[1] = robot_position[1] + 1
    print ('front')
    
def move_back():
    global robot_position
    robot.straight(-180)
    #atualiza a robot_position[1]
    robot_position[1] = robot_position[1] - 1
    print ('back')

def move_left():
    global robot_position
    robot.turn(-128)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(135)
    #atualiza a robot_position[0]
    robot_position[0] = robot_position[0] + 1
    print ('left')

def move_right():
    global robot_position
    robot.turn(128)
    robot.straight(DRIVE_DISTANCE)
    robot.turn(-135)
    #atualiza a robot_position[0]
    robot_position[0] = robot_position[0] - 1
    print ('right')

def move_double(destino):
    double = destino
    if double == 'random':
        double = choice(POSSIBLE_DOUBLE)

    global run_front,run_back ,run_left ,run_right

    if (double == 'FRONT-FRONT' and run_front == 0):
        #possible movement when line = 0,1,2,3 and column = 0,1,2,3,4,5
        if robot_position[1] < 4:
            move_front()
            move_front()
        else :
            return move_double('random')
    elif (double == 'FRONT-RIGHT' and run_front == 0):
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        if (robot_position[1] < 5 and robot_position[0] > 0 ):
            move_front()
            move_right()
        else:
            return move_double('random')
    elif (double == 'FRONT-LEFT' and run_front == 0):
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        if (robot_position[1] < 5 and robot_position[0] < 5) :
            move_front()
            move_left()
        else:
            return move_double('random')
    elif (double == 'BACK-BACK' and run_back == 0):
        #possible movement when line = 2,3,4,5 and column = 0,1,2,3,4,5
        if robot_position[1] > 1:
            move_back()
            move_back()
        else :
            return move_double('random')
    elif (double == 'BACK-RIGHT' and run_back == 0):
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        if (robot_position[1] > 0 and robot_position[0] > 0 ):
            move_back()
            move_right()
        else :
            return move_double('random')
    elif (double == 'BACK-LEFT' and run_back == 0):
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        if (robot_position[1] > 0 and robot_position[0] < 5):
            move_back()
            move_left()
        else :
            return move_double('random')
    elif (double == 'LEFT-LEFT' and run_left == 0):
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3
        if robot_position[0] < 4:
            move_left()
            move_left()
        else :
            return move_double('random')
    elif (double == 'LEFT-FRONT' and run_left == 0):
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        if (robot_position[1] < 5 and robot_position[0] < 5) :
            move_left()
            move_front()
        else : 
            return move_double('random')
    elif (double == 'LEFT-BACK' and run_left == 0):
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        if (robot_position[1] > 0 and robot_position[0] < 5) :
            move_left()
            move_back()
        else :
            return move_double('random')
    elif (double == 'RIGHT-RIGHT' and run_right == 0):
#possible movement when line = 0,1,2,3,4,5 and column = 2,3,4,5
        if robot_position[0] > 1:
            move_right()
            move_right()
        else :
            return move_double('random')
    elif (double == 'RIGHT-FRONT' and run_right == 0):
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        if (robot_position[1] < 5 and robot_position[0] > 0 ): 
            move_right()
            move_front()
        else: 
            return move_double('random')
    elif (double == 'RIGHT-BACK' and run_right == 0):
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        if (robot_position[1] > 0 and robot_position[0] > +0 ): 
            move_right()
            move_back()
        else:
            return move_double('random')


def moveTowardsGoal(atual,objetivo):
    move = [0,0]
    teste = A_starStep(atual,objetivo)
    move[0] = teste[0] - atual[0]
    move[1] = teste[1] - atual[1]
    print('Star: ' + str(teste))
    print('TESTE: ' + str(move))

    if(move[0] ==0  and move[1] == 0):
        move_double('LEFT-FRONT')
    elif(move[0] == 1 and move[1] == 0):
        move_left()
    elif(move[0] == 0 and move[1] == 1):
        move_front()
    elif(move[0] == 1 and move[1] == 1):
        move_double('LEFT-FRONT')
    elif(move[0] == 2 and move[1] == 0):
        move_double('RIGHT-RIGHT')
    elif(move[0] == 0 and move[1] == 2):
        move_double('FRONT-FRONT')
    elif(move[0] == -1 and move[1] == 0):
        move_right()
    elif(move[0] == 0 and move[1] == -1):
        move_back()
    elif(move[0] == -1 and move[1] == -1):
        move_double('RIGHT-BACK')
    elif(move[0] == -2 and move[1] == 0):
        move_double('LEFT-LEFT')
    elif(move[0] == 0 and move[1] == -2):
        move_double('BACK-BACK')


# Write your program here.
ev3.speaker.set_volume(100)
ev3.speaker.say("Ready")
while(True):

    color = color_sensor.color()

    if (parts_counter != 0):
        ev3.speaker.play_file(SoundFile.CHEERING)

    #se tiver duas cores na mesma casa    
    if left_shoulder.pressed():
        detect_bullet()
        detect_motorcycle_part()

    if(parts_counter == 1):
        if(robot_position[0] == 5 and robot_position[1] == 5):
            parts_moto = parts_moto + 1
            parts_counter = parts_counter - 1
            ev3.speaker.say('Added motor part in the motorcycle')
            goal = [0,0]
            print('Chegou a moto. Colocou peça')
    if(parts_moto == 2):
        if(robot_position[0] == 5 and robot_position[1] == 5):
             ev3.speaker.say('I  WON  THE  GAME')

    if right_shoulder.pressed():
        plays_counter = plays_counter + 1
        print('--------------------------------------')
        print('Starting play - Right Shoulder pressed') # DELETE LATER
        if(robot_position[1] == 5 and robot_position[0] == 5):
            if(parts_counter == 2):
                ev3.speaker.say('Motorcycle fixed')

        random_recon()
        detect_bullet()
        detect_motorcycle_part()
        move(front_object,right_object,back_object,left_object)

        update_robot_position(robot_position[1],robot_position[0]) # updates the robot position in the matrix
        
        print('r:' + str(right_object) + ' l:' + str(left_object) + ' f:' + str(front_object) + ' b:' + str(back_object))
        print(str(map[0]) + "\n" + str(map[1]) + "\n" + str(map[2]) + "\n" + str(map[3]) + "\n" + str(map[4])+"\n" +str(map[4]) +"\n" )
        print('My position is: ' + str(robot_position[0]) + ', ' + str(robot_position[1]))
        print('My goial is:' + str(goal))
        print('Plays made: ' + str(plays_counter))

        reset_robot_position(robot_position[1],robot_position[0]) # resets the robot position in the matrix
