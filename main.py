#!/usr/bin/env pybricks-micropython
from common import *
from movement import *
from attack import *
from smell import *
from matrix import *

POSSIBLE_PLAYS = ['MOVEMENT'] # Attack move only joins possible plays when zombie is dettected
POSSIBLE_MOVEMENTS_AFTER_STUN = ['']


dynamic_matrix = [
['x0y0','x0y1','x0y2','x0y3','x0y4','x0y5'],
['x1y0','x1y1','x1y2','x1y3','x1y4','x1y5'],
['x2y0','x2y1','x2y2','x2y3','x2y4','x2y5'],
['x3y0','x3y1','x3y2','x3y3','x3y4','x3y5'],
['x4y0','x4y1','x4y2','x4y3','x4y4','x4y5'],
['x5y0','x5y1','x5y2','x5y3','x5y4','x5y5']]

'''
x0y0 = robot
x5y0 = zombie
x0y5 = zombie


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

'''
def update_robot_position():
    matrix_map[0][0] = 0
    matrix_map[1][0] = 'Robot'
'''

def update_robot_position (lines,columns):
    dynamic_matrix[lines][columns] = 'robot'

    #print(str(dynamic_matrix[lines][columns]))


def recon_right():

    global right_object_1, right_object_2, right_object_3, right_object_4

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Right')
        change_dynamic
        right_object_1 = 1
        return True
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Right')
        right_object_2 = 1
        return True
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Right')
        right_object_3 = 1
        return True
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Right')  
        right_object_4 = 1
        return True

    return False

def recon_left():

    global left_object_1, left_object_2, left_object_3, left_object_4

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Left')
        left_object_1 = 1
        return True
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Left')
        left_object_2 = 1
        return True
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Left')
        left_object_3 = 1
        return True
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Left')  
        left_object_4 = 1
        return True

    return False

def recon_front():

    global front_object_1, front_object_2, front_object_3, front_object_4

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Front')
        front_object_1 = 1
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Front')
        front_object_2 = 1
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Front')
        front_object_3 = 1
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Front')  
        front_object_4 = 1

    return 0

def recon_back():

    global back_object_1, back_object_2, back_object_3, back_object_4

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Back')
        back_object_1 = 1
        return True
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Back')
        back_object_2 = 1
        return True
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Back')
        back_object_3 = 1
        return True
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Back')  
        back_object_4 = 1
        return True

    return False

def verifica_objeto():

    global front_object_1, right_object_1, left_object_1, back_object_1
    mov = 0
    global run_front,run_back ,run_left ,run_right

    color = color_sensor.color()

    if(color == Color.BLUE):     #Color Blue detected, Zombie is 2 blocks away
        print(color)
        ev3.speaker.say('Zombie close')
        wait(2000)
        
    if (front_object_1 == 1 and left_object_1 == 0 and back_object_1 == 0 and right_object_1 == 0 and run_front == 0):
        color = color_sensor.color()
        if(color == Color.RED):      # Color Red detected, Zombie is 1 blocks away
            print('Recon ' + str(color))                                
            ev3.speaker.say('Zombie very close')
            wait(2000)
        
            random_attack()
            print("A")
            run_front = 1
        else:
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
        mov=1

    if (front_object_1 == 0 and left_object_1 == 1 and back_object_1 == 0 and right_object_1 == 0 and run_left == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.turn(-125)
            wait(1000)
            random_attack()
            wait(1000)
            robot.turn(125)
            print("B")
            run_left = 1
        else:
            robot.turn(-125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
            robot.turn(125)
        mov=1

    if (front_object_1 == 0 and left_object_1 == 0 and back_object_1 == 1 and right_object_1 == 0 and run_back == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.turn(250)
            wait(1000)
            random_attack()
            wait(1000)
            robot.turn(-250)
            print("C")
            run_back = 1
        else:
            robot.turn(250)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
            robot.turn(-250)
        mov=1
    
    if (front_object_1 == 0 and left_object_1 == 0 and back_object_1 == 0 and right_object_1 == 1 and run_right == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.turn(125)
            wait(1000)
            random_attack()
            wait(1000)
            robot.turn(-125)
            print("D")
            run_right = 1
        else:
            robot.turn(125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
            robot.turn(-125)
        mov=1

    if (front_object_1 == 1 and right_object_1 == 1 and run_front == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.straight(DRIVE_DISTANCE/2)
            wait(1500)
            color = color_sensor.color()
            if color == color.RED:
                robot.straight(-DRIVE_DISTANCE/2)
                wait(1000)
                random_attack()
                run_front = 1
            else:
                detect_motorcycle_part()
                detect_bullet()
                wait(1000)
                robot.straight(DRIVE_DISTANCE/2)
            print("E")
        else:
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
        mov=1
        
    if (front_object_1 == 1 and left_object_1 == 1 and run_front == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.straight(DRIVE_DISTANCE/2)
            wait(1500)
            color = color_sensor.color()
            if color == color.RED:
                robot.straight(-DRIVE_DISTANCE/2)
                wait(1000)
                random_attack()
                run_front = 1
            else:
                detect_motorcycle_part()
                detect_bullet()
                wait(1000)
                robot.straight(DRIVE_DISTANCE/2)
            print("F")
        else:
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
        mov=1

    if (front_object_1 == 1 and back_object_1 == 1 and run_front == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.straight(DRIVE_DISTANCE/2)
            wait(1500)
            color = color_sensor.color()
            if color == color.RED:
                robot.straight(-DRIVE_DISTANCE/2)
                wait(1000)
                random_attack()
                run_front = 1
            else:
                detect_motorcycle_part()
                detect_bullet()
                wait(1000)
                robot.straight(DRIVE_DISTANCE/2)
            print("G")
        else:
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
        mov=1
            
    if (right_object_1 == 1 and left_object_1 == 1 and run_right == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.turn(125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1500)
            color = color_sensor.color()
            if color == color.RED:
                robot.straight(-DRIVE_DISTANCE/2)
                wait(1000)
                random_attack()
                robot.turn(-125)
                run_right = 1
            else:
                detect_motorcycle_part()
                detect_bullet()
                wait(1000)
                robot.straight(DRIVE_DISTANCE/2)
                robot.turn(-125)
            print("H")
        else:
            robot.turn(125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
            robot.turn(-125)
        mov=1
        
    if (right_object_1 == 1 and back_object_1 == 1 and run_right == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.turn(125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1500)
            color = color_sensor.color()
            if color == color.RED:
                robot.straight(-DRIVE_DISTANCE/2)
                wait(1000)
                random_attack()
                robot.turn(-125)
                run_right = 1
            else:
                detect_motorcycle_part()
                detect_bullet()
                wait(1000)
                robot.straight(DRIVE_DISTANCE/2)
                robot.turn(-125)
            print("I")
        else:
            robot.turn(125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
            robot.turn(-125)
        mov=1

    if (left_object_1 == 1 and back_object_1 == 1 and run_left == 0):
        color = color_sensor.color()
        if(color == Color.RED):
            robot.turn(-125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1500)
            color = color_sensor.color()
            if color == color.RED:
                robot.straight(-DRIVE_DISTANCE/2)
                wait(1000)
                random_attack()
                robot.turn(125)
                run_left = 1
            else:
                detect_motorcycle_part()
                detect_bullet()
                wait(1000)
                robot.straight(DRIVE_DISTANCE/2)
                robot.turn(125)
            print("J")
        else:
            robot.turn(-125)
            robot.straight(DRIVE_DISTANCE/2)
            wait(1000)
            detect_motorcycle_part()
            detect_bullet()
            wait(1000)
            robot.straight(DRIVE_DISTANCE/2)
            robot.turn(125)
        mov=1
    print ("")
    if (mov == 0):
        if (run_front == 1 or run_left == 1 or run_right == 1 or run_back == 1):
            print('I am going to move')
            ev3.speaker.say('ON MY WAY AFTER STUN')
            random_movement()
            print('My position is: ' + str(line_counter) + ', ' + str(column_counter))
            run_front = 0
            run_right = 0
            run_left = 0
            run_back = 0
        else:
            print('I am going to move')
            ev3.speaker.say('ON MY WAY')
            random_movement()
            print('My position is: ' + str(line_counter) + ', ' + str(column_counter))

    front_object_1 = 0
    right_object_1 = 0
    left_object_1 = 0
    back_object_1 = 0

def random_recon():
    #print(eyes.distance())
    #Robot in column 0 (cant recon right)
    if (column_counter == 0):
        #Robot in column 0 and line 0 (cant recon right or back)
        if(line_counter == 0):
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
        if(line_counter == 5):
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
        if(line_counter != 5 and line_counter != 0):
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
    if (column_counter == 5):
        #Robot in column 5 and line 0 (cant recon left or back)
        if (line_counter == 0):
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
        if (line_counter == 5):
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
        if(line_counter != 5 and line_counter != 0):
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

    if (line_counter == 0 and column_counter != 0 and column_counter != 5):
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
        
    if (line_counter == 5 and column_counter != 0 and column_counter != 5):
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
        
    if (line_counter != 5 and line_counter != 0 and column_counter != 0 and column_counter != 5):
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



# Write your program here.
while(True):

    color = color_sensor.color()

    #if (parts_counter != 0):
        #ev3.speaker.play_file(SoundFile.CHEERING)
        
    if left_shoulder.pressed():
        ev3.speaker.play_file(SoundFile.GAME_OVER)

    if right_shoulder.pressed():

        print('--------------------------------------')
        print('Starting play - Right Shoulder pressed') # DELETE LATER
        if(line_counter == 5 and column_counter == 5):
            if(parts_counter == 2):
                ev3.speaker.say('Motorcycle fixed')


        random_recon()
        detect_bullet()
        detect_motorcycle_part()
        verifica_objeto()

        print('r:' + str(right_object_1) + ' l:' + str(left_object_1) + ' f:' + str(front_object_1) + ' b:' + str(back_object_1))

        update_robot_position(line_counter,column_counter)
        update_data_matrix (right, 1):
        print('My position is: ' + str(line_counter) + ', ' + str(column_counter))
        print('Plays made: ' + str(plays_counter))

        '''     
        elif play == 'ATTACK':
            ev3.speaker.say('ATTACKING')
            random_attack()
        elif play == 'MOVEMENT':
            ev3.speaker.say('ON MY WAY')
            random_movement()
            print('My position is: ' + str(line_counter) + ', ' + str(column_counter))

        '''
        
