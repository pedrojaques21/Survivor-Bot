from common import *

def update_data_matrix (side):

    if (side == 'front'):
        if (front_object_1 == 1):
            dynamic_matrix[1][0] = 'object' 
        if (front_object_2 == 1):
            dynamic_matrix[2][0] = 'object' 
        if (front_object_3 == 1):
            dynamic_matrix[3][0] = 'object' 
        if (front_object_4 == 1):
            dynamic_matrix[4][0] = 'object' 

    if (side == 'right'):
        if (right_object_1 == 1):
            dynamic_matrix[0][1] = 'object' 
        if (right_object_2 == 1):
            dynamic_matrix[0][2] = 'object' 
        if (right_object_3 == 1):
            dynamic_matrix[0][3] = 'object' 
        if (right_object_4 == 1):
            dynamic_matrix[0][4] = 'object' 
    
    if (side == 'left'):
        if (left_object_1 == 1):
            dynamic_matrix[0][4] = 'object' 
        if (left_object_2 == 1):
            dynamic_matrix[0][3] = 'object' 
        if (left_object_3 == 1):
            dynamic_matrix[0][2] = 'object' 
        if (left_object_4 == 1):
            dynamic_matrix[0][1] = 'object' 
            
    if (side == 'back'):
        if (back_object_1 == 1):
            dynamic_matrix[4][0] = 'object' 
        if (back_object_2 == 1):
            dynamic_matrix[3][0] = 'object' 
        if (back_object_3 == 1):
            dynamic_matrix[2][0] = 'object' 
        if (back_object_4 == 1):
            dynamic_matrix[1][0] = 'object' 

    if (line_counter == 0 && column_counter == 0):
        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][4] = 'object' 

    if (line_counter == 1 && column_counter == 0):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][4] = 'object'
        
    if (line_counter == 2 && column_counter == 0):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][4] = 'object'

    if (line_counter == 3 && column_counter == 0):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][4] = 'object'

    if (line_counter == 4 && column_counter == 0):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][4] = 'object'

    if (line_counter == 5 && column_counter == 0):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter0][2] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][4] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 && column_counter == 1):
        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][0] = 'object'


    
    if (line_counter == 1 && column_counter == 1):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 && column_counter == 1):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 && column_counter == 1):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 4 && column_counter == 1):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 5 && column_counter == 1):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_4 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 && column_counter == 2):
        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][0] = 'object'
    
    if (line_counter == 1 && column_counter == 2):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 && column_counter == 2):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 && column_counter == 2):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][5] = 'object'
                
        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 4 && column_counter == 2):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 5 && column_counter == 2):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_3 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][1] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][0] = 'object' 


    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 && column_counter == 3):
        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][0] = 'object' 


    if (line_counter == 1 && column_counter == 3):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 && column_counter == 3):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 && column_counter == 3):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][5] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][0] = 'object'  

    if (line_counter == 4 && column_counter == 3):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 5 && column_counter == 3):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object' 
            if (left_object_2 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][2] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][1] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 && column_counter == 4):
        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][0] = 'object' 

    if (line_counter == 1 && column_counter == 4):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 2 && column_counter == 4):
                if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 3 && column_counter == 4):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][0] = 'object'

    if (line_counter == 4 && column_counter == 4):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][0] = 'object' 


    if (line_counter == 5 && column_counter == 4):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[1][column_counter] = 'object'
        
        if (side == 'left'):
            if (left_object_1 == 1):
                dynamic_matrix[line_counter][5] = 'object' 

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][3] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][2] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][1] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][0] = 'object'   

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (line_counter == 0 && column_counter == 5):
        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][1] = 'object'  

    if (line_counter == 1 && column_counter == 5):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[0][column_counter] = 'object' 

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_4 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][1] = 'object' 

    if (line_counter == 2 && column_counter == 5):
                if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[1][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_3 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][1] = 'object' 

    if (line_counter == 3 && column_counter == 5):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[2][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (front_object_2 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][1] = 'object' 

    if (line_counter == 4 && column_counter == 5):
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[3][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[1][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[0][column_counter] = 'object'

        if (side == 'front'):
            if (front_object_1 == 1):
                dynamic_matrix[5][column_counter] = 'object' 
        
        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][1] = 'object' 


    if (line_counter == 5 && column_counter == 5): 
        if (side == 'back'):
            if (back_object_1 == 1):
                dynamic_matrix[4][column_counter] = 'object' 
            if (back_object_2 == 1):
                dynamic_matrix[3][column_counter] = 'object'
            if (back_object_3 == 1):
                dynamic_matrix[2][column_counter] = 'object'
            if (back_object_4 == 1):
                dynamic_matrix[1][column_counter] = 'object'

        if (side == 'right'):
            if (right_object_1 == 1):
                dynamic_matrix[line_counter][4] = 'object'
            if (right_object_2 == 1):
                dynamic_matrix[line_counter][3] = 'object' 
            if (right_object_3 == 1):
                dynamic_matrix[line_counter][2] = 'object'    
            if (right_object_4 == 1):
                dynamic_matrix[line_counter][1] = 'object'      