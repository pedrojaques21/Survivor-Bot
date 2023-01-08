#!/usr/bin/env pybricks-micropython
from common import *
from attack import *
from smell import *
from matrix import *

robot = DriveBase(left_leg, right_leg, 25, 105)

robot.settings(190, 100, 190, 100)



line_counter = 0
column_counter = 0


dynamic_matrix = [
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0'],
['0','0','0','0','0','0']]

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

def reset_robot_position (lines, columns):
    dynamic_matrix[lines][columns] = '0'

def recon_right():

    global right_object

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Right')
        right_object = 1
        update_data_matrix('right')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Right')
        right_object = 2
        update_data_matrix('right')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Right')
        right_object = 3
        update_data_matrix('right')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Right')  
        right_object = 4
        update_data_matrix('right')

    return 0

def recon_left():

    global left_object

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Left')
        left_object = 1
        update_data_matrix('left')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Left')
        left_object = 2
        update_data_matrix('left')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Left')
        left_object = 3
        update_data_matrix('left')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Left')  
        left_object = 4
        update_data_matrix('left')

    return 0

def recon_front():

    global front_object

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Front')
        front_object = 1
        update_data_matrix('front')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Front')
        front_object = 2
        update_data_matrix('front')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Front')
        front_object = 3
        update_data_matrix('front')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Front')  
        front_object = 4
        update_data_matrix('front')
    return 0

def recon_back():

    global back_object

    if(eyes.distance() <= 370):
        print('Objeto - 1 casas - Back')
        back_object = 1
        update_data_matrix('back')
    if(eyes.distance()>=380 and eyes.distance()<=640):
        print('Objeto - 2 casas - Back')
        back_object = 2
        update_data_matrix('back')
    if(eyes.distance()>=650 and eyes.distance()<=890):
        print('Objeto - 3 casas - Back')
        back_object = 3
        update_data_matrix('back')
    if(eyes.distance()>=900 and eyes.distance()<=1060):
        print('Objeto - 4 casas - Back')  
        back_object = 4
        update_data_matrix('back')

    return False

def verify_object():

    mov = 0
    global front_object, right_object, left_object, back_object

    global run_front,run_back ,run_left ,run_right

    color = color_sensor.color()

    if(color == Color.BLUE):     #Color Blue detected, Zombie is 2 blocks away
        print(color)
        ev3.speaker.say('Zombie close')
        wait(2000)
        
    if (front_object == 1 and left_object == 0 and back_object == 0 and right_object == 0 and run_front == 0):
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

    if (front_object == 0 and left_object == 1 and back_object == 0 and right_object == 0 and run_left == 0):
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

    if (front_object == 0 and left_object == 0 and back_object == 1 and right_object == 0 and run_back == 0):
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
    
    if (front_object == 0 and left_object == 0 and back_object == 0 and right_object == 1 and run_right == 0):
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

    if (front_object == 1 and right_object == 1 and run_front == 0):
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
        
    if (front_object == 1 and left_object == 1 and run_front == 0):
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

    if (front_object == 1 and back_object == 1 and run_front == 0):
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
            
    if (right_object == 1 and left_object == 1 and run_right == 0):
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
        
    if (right_object == 1 and back_object == 1 and run_right == 0):
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

    if (left_object == 1 and back_object == 1 and run_left == 0):
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
        elif (front_object == 2 and right_object == 0 and left_object == 0 and back_object == 0):
            wait(1000)
            color = color_sensor.color()
            if color == color.BLUE:
                ev3.speaker.say('CHECKING AREA')
                move_front()
                wait(1000)
                color = color_sensor.color()
                if color == color.RED:
                    robot.straight(DRIVE_DISTANCE/2)
                    wait(1000)
                    color = color_sensor.color()
                    if color == color.RED:
                        print("COLOR: RED -> ZOMBIE")
                        robot.straight(-DRIVE_DISTANCE/2)
                        wait(1000)
                        ev3.speaker.say('DIE ZOMBIE')
                        random_attack()
                        run_front = 1
                    else:
                        print("ZOMBIE IS NOT HERE, IM SAFE")
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
            else:
                move_front()
                move_front()
        
        elif (front_object == 0 and right_object == 2 and left_object == 0 and back_object == 0):
            wait(1000)
            color1 = color_sensor.color()
            if color1 == color1.BLUE:
                ev3.speaker.say('CHECKING AREA')
                move_right()
                wait(1000)
                color2 = color_sensor.color()
                if color == color.RED:
                    robot.turn(125)
                    robot.straight(DRIVE_DISTANCE/2)
                    wait(1000)
                    color = color_sensor.color()
                    if color == color.RED:
                        print("COLOR: RED -> ZOMBIE")
                        robot.straight(-DRIVE_DISTANCE/2)
                        wait(1000)
                        ev3.speaker.say('DIE ZOMBIE')
                        random_attack()
                        robot.turn(-125)
                        run_right = 1
                    else:
                        print("ZOMBIE IS NOT HERE, IM SAFE")
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        robot.turn(-125)
            else:
                move_right()
                move_right()

        elif (front_object == 0 and right_object == 0 and left_object == 2 and back_object == 0):
            wait(1000)
            color1 = color_sensor.color()
            if color1 == color1.BLUE:
                ev3.speaker.say('CHECKING AREA')
                move_left()
                wait(1000)
                color2 = color_sensor.color()
                if color == color.RED:
                    robot.turn(-125)
                    robot.straight(DRIVE_DISTANCE/2)
                    wait(1000)
                    color = color_sensor.color()
                    if color == color.RED:
                        print("COLOR: RED -> ZOMBIE")
                        robot.straight(-DRIVE_DISTANCE/2)
                        wait(1000)
                        ev3.speaker.say('DIE ZOMBIE')
                        random_attack()
                        robot.turn(125)
                        run_left = 1
                    else:
                        print("ZOMBIE IS NOT HERE, IM SAFE")
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        robot.turn(125)
            else:
                move_left()
                move_left()

        elif (front_object == 0 and right_object == 0 and left_object == 0 and back_object == 2):
            wait(1000)
            color1 = color_sensor.color()
            if color1 == color1.BLUE:
                ev3.speaker.say('CHECKING AREA')
                move_back()
                wait(1000)
                color2 = color_sensor.color()
                if color == color.RED:
                    robot.turn(250)
                    robot.straight(DRIVE_DISTANCE/2)
                    wait(1000)
                    color = color_sensor.color()
                    if color == color.RED:
                        print("COLOR: RED -> ZOMBIE")
                        robot.straight(-DRIVE_DISTANCE/2)
                        wait(1000)
                        ev3.speaker.say('DIE ZOMBIE')
                        random_attack()
                        robot.turn(-250)
                        run_right = 1
                    else:
                        print("ZOMBIE IS NOT HERE, IM SAFE")
                        detect_motorcycle_part()
                        detect_bullet()
                        wait(1000)
                        robot.straight(DRIVE_DISTANCE/2)
                        robot.turn(-250)
            else:
                move_back()
                move_back()


        elif (front_object == 3):
            print("!! moving one block, because zombie might be nearby !!")
            ev3.speaker.say('BE CAREFUL')
            move_front()

        elif (back_object == 3):
            print("!! moving one block, because zombie might be nearby !!")
            ev3.speaker.say('BE CAREFUL')
            move_back()

        elif (left_object == 3):
            print("!! moving one block, because zombie might be nearby !!")
            ev3.speaker.say('BE CAREFUL')
            move_left()

        elif (right_object == 3):
            print("!! moving one block, because zombie might be nearby !!")
            ev3.speaker.say('BE CAREFUL')
            move_right()
        else:
            print('I am going to move')
            ev3.speaker.say('ON MY WAY')
            random_movement()
            print('My position is: ' + str(line_counter) + ', ' + str(column_counter))

    


    front_object = 0
    right_object = 0
    left_object = 0
    back_object = 0

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
    global run_front,run_back ,run_left ,run_right
    #print('R' + str(run_right) + ', L ' + str(run_left) + ', B' + str(run_back) + ', F' + str(run_front))

    if (double == 'FRONT-FRONT' and run_front == 0):
        #possible movement when line = 0,1,2,3 and column = 0,1,2,3,4,5
        if line_counter < 4:
            move_front()
            move_front()
        else :
            return move_double()
    elif (double == 'FRONT-RIGHT' and run_front == 0):
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        if (line_counter < 5 and column_counter > 0 ):
            move_front()
            move_right()
        else:
            return move_double()
    elif (double == 'FRONT-LEFT' and run_front == 0):
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        if (line_counter < 5 and column_counter < 5) :
            move_front()
            move_left()
        else:
            return move_double()
    elif (double == 'BACK-BACK' and run_back == 0):
        #possible movement when line = 2,3,4,5 and column = 0,1,2,3,4,5
        if line_counter > 1:
            move_back()
            move_back()
        else :
            return move_double()
    elif (double == 'BACK-RIGHT' and run_back == 0):
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        if (line_counter > 0 and column_counter > 0 ):
            move_back()
            move_right()
        else :
            return move_double()
    elif (double == 'BACK-LEFT' and run_back == 0):
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        if (line_counter > 0 and column_counter < 5):
            move_back()
            move_left()
        else :
            return move_double()
    elif (double == 'LEFT-LEFT' and run_left == 0):
        #possible movement when line = 0,1,2,3,4,5 and column = 0,1,2,3
        if column_counter < 4:
            move_left()
            move_left()
        else :
            return move_double()
    elif (double == 'LEFT-FRONT' and run_left == 0):
        #possible movement when line = 0,1,2,3,4 and column = 0,1,2,3,4
        if (line_counter < 5 and column_counter < 5) :
            move_left()
            move_front()
        else : 
            return move_double()
    elif (double == 'LEFT-BACK' and run_left == 0):
        #possible movement when line = 1,2,3,4,5 and column = 0,1,2,3,4
        if (line_counter > 0 and column_counter < 5) :
            move_left()
            move_back()
        else :
            return move_double()
    elif (double == 'RIGHT-RIGHT' and run_right == 0):
        #possible movement when line = 0,1,2,3,4,5 and column = 2,3,4,5
        if column_counter > 1:
            move_right()
            move_right()
        else :
            return move_double()
    elif (double == 'RIGHT-FRONT' and run_right == 0):
        #possible movement when line = 0,1,2,3,4 and column = 1,2,3,4,5
        if (line_counter < 5 and column_counter > 0 ): 
            move_right()
            move_front()
        else: 
            return move_double()
    elif (double == 'RIGHT-BACK' and run_right == 0):
        #possible movement when line = 1,2,3,4,5 and column = 1,2,3,4,5
        if (line_counter > 0 and column_counter > +0 ): 
            move_right()
            move_back()
        else:
            return move_double()

def random_movement():
    movement = choice(POSSIBLE_MOVEMENTS)
    global run_front, run_back, run_left, run_right
    #print('R' + str(run_right) + ', L ' + str(run_left) + ', B' + str(run_back) + ', F' + str(run_front))
    if (line_counter == 0 and column_counter == 0 and left_object == 0 and front_object == 0):
        ev3.speaker.say("didnt find nothing moving out")
        wait(500)
        move_front()
        move_left()
    else:
        if (movement == 'FRONT' and run_front == 0):
            if line_counter < 5:
                move_front()
            else:
                #print ('Can not go front!')
                return random_movement()
                
        elif (movement == 'BACK' and run_back == 0):
            if line_counter > 0:
                move_back()
            else:
                #print ('Can not go back!')
                return random_movement()
            
        elif (movement == 'RIGHT' and run_right == 0):
            if column_counter > 0:
                move_right()
            else:
                #print ('Can not go right!')
                return random_movement()
            
        elif (movement == 'LEFT' and run_left == 0):
            if column_counter < 5:
                move_left()
            else:
                #print ('Can not go left!')
                return random_movement()
        elif movement == 'DOUBLE':
            move_double()


def secure_movement():
    movement = choice(POSSIBLE_MOVEMENTS)
    global run_front, run_back, run_left, run_right

    if (movement == 'FRONT' and run_front == 0):
        if line_counter < 5:
            move_front()
        else:
            print ('Can not go front!')
            return secure_movement()
            
    elif (movement == 'BACK' and run_back == 0):
        if line_counter > 0:
            move_back()
        else:
            print ('Can not go back!')
            return secure_movement()
        
    elif (movement == 'RIGHT' and run_right == 0):
        if column_counter > 0:
            move_right()
        else:
            print ('Can not go right!')
            return secure_movement()
        
    elif (movement == 'LEFT' and run_left == 0):
        if column_counter < 5:
            move_left()
        else:
            print ('Can not go left!')
            return secure_movement()


# Write your program here.
ev3.speaker.set_volume(100)
ev3.speaker.say("I'm ready motherfuckers")
while(True):

    color = color_sensor.color()

    #if (parts_counter != 0):
        #ev3.speaker.play_file(SoundFile.CHEERING)
        
    if left_shoulder.pressed():
        ev3.speaker.play_file(SoundFile.GAME_OVER)

    if right_shoulder.pressed():
        plays_counter = plays_counter + 1
        print('--------------------------------------')
        print('Starting play - Right Shoulder pressed') # DELETE LATER
        if(line_counter == 5 and column_counter == 5):
            if(parts_counter == 2):
                ev3.speaker.say('Motorcycle fixed')

        random_recon()
        detect_bullet()
        detect_motorcycle_part()
        verify_object()

        update_robot_position(line_counter,column_counter) # updates the robot position in the matrix
        
        print('r:' + str(right_object) + ' l:' + str(left_object) + ' f:' + str(front_object) + ' b:' + str(back_object))
        print(str(dynamic_matrix[0]) + "\n" + str(dynamic_matrix[1]) + "\n" + str(dynamic_matrix[2]) + "\n" + str(dynamic_matrix[3]) + "\n" + str(dynamic_matrix[4]) + "\n" )
        print('My position is: ' + str(line_counter) + ', ' + str(column_counter))
        print('Plays made: ' + str(plays_counter))

        reset_robot_position(line_counter,column_counter) # resets the robot position in the matrix