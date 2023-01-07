from common import *

def update_data_matrix (side):

    if (line_counter == 0 and column_counter == 0):
        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][4] = 'object' 

    if (line_counter == 1 and column_counter == 0):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][4] = 'object'
        
    if (line_counter == 2 and column_counter == 0):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][4] = 'object'

    if (line_counter == 3 and column_counter == 0):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][4] = 'object'

    if (line_counter == 4 and column_counter == 0):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][4] = 'object'

    if (line_counter == 5 and column_counter == 0):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][4] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 and column_counter == 1):
        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][0] = 'object'


    
    if (line_counter == 1 and column_counter == 1):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 and column_counter == 1):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 and column_counter == 1):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 4 and column_counter == 1):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 5 and column_counter == 1):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 4):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][0] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 and column_counter == 2):
        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][0] = 'object'
    
    if (line_counter == 1 and column_counter == 2):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 and column_counter == 2):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 and column_counter == 2):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][5] = 'object'
                
        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 4 and column_counter == 2):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 5 and column_counter == 2):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 3):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][0] = 'object' 


    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 and column_counter == 3):
        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][0] = 'object' 


    if (line_counter == 1 and column_counter == 3):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 and column_counter == 3):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 and column_counter == 3):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][0] = 'object'  

    if (line_counter == 4 and column_counter == 3):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 5 and column_counter == 3):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object == 2):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][0] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 and column_counter == 4):
        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][0] = 'object' 

    if (line_counter == 1 and column_counter == 4):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 and column_counter == 4):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 and column_counter == 4):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 4 and column_counter == 4):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][0] = 'object' 


    if (line_counter == 5 and column_counter == 4):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][0] = 'object'   

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 and column_counter == 5):
        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][1] = 'object'  

    if (line_counter == 1 and column_counter == 5):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 4):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][1] = 'object' 

    if (line_counter == 2 and column_counter == 5):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 3):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][1] = 'object' 

    if (line_counter == 3 and column_counter == 5):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object == 2):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][1] = 'object' 

    if (line_counter == 4 and column_counter == 5):
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][1] = 'object' 


    if (line_counter == 5 and column_counter == 5): 
        if (side == 'back'):
            if (back_object == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object == 2):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object == 3):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object == 4):
                dynamic_matrix[1][column_counter] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object == 2):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object == 3):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object == 4):
                dynamic_matrix[line_counter][1] = 'object'      