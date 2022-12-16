from header import *

robot = DriveBase(left_leg, right_leg, 25, 105)

robot.settings(190, 100, 190, 100)


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
        if (line_counter > 0 and column_counter >0 ): 
            move_right()
            move_back()
        else:
            return move_double()

def random_movement():
    movement = choice(POSSIBLE_MOVEMENTS)
    global run_front,run_back ,run_left ,run_right
    #print('R' + str(run_right) + ', L ' + str(run_left) + ', B' + str(run_back) + ', F' + str(run_front))

    if (movement == 'FRONT' and run_front == 0):
        if line_counter < 5:
            move_front()
        else:
            print ('Can not go front!')
            return random_movement()
            
    elif (movement == 'BACK' and run_back == 0):
        if line_counter > 0:
            move_back()
        else:
            print ('Can not go back!')
            return random_movement()
        
    elif (movement == 'RIGHT' and run_right == 0):
        if column_counter > 0:
            move_right()
        else:
            print ('Can not go right!')
            return random_movement()
        
    elif (movement == 'LEFT' and run_left == 0):
        if column_counter < 5:
            move_left()
        else:
            print ('Can not go left!')
            return random_movement()
    elif movement == 'DOUBLE':
        move_double()

