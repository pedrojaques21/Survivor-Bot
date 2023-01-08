#!/usr/bin/env pybricks-micropython
from main import *


def update_data_matrix (side):

    if (robot_position[0] == 0 and robot_position[1] == 0):
        if (side == 'front'):
            if (front_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[4][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][1] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][4] = 'object' 

    if (robot_position[0] == 1 and robot_position[1] == 0):
        if (side == 'back'):
            if (back_object == 1):
                map[0][robot_position[1]] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][1] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][4] = 'object'
        
    if (robot_position[0] == 2 and robot_position[1] == 0):
        if (side == 'back'):
            if (back_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][1] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][4] = 'object'

    if (robot_position[0] == 3 and robot_position[1] == 0):
        if (side == 'back'):
            if (back_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[1][robot_position[1]] = 'object'
            if (back_object == 3):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][1] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][4] = 'object'

    if (robot_position[0] == 4 and robot_position[1] == 0):
        if (side == 'back'):
            if (back_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[2][robot_position[1]] = 'object'
            if (back_object == 3):
                map[1][robot_position[1]] = 'object'
            if (back_object == 4):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][1] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][4] = 'object'

    if (robot_position[0] == 5 and robot_position[1] == 0):
        if (side == 'back'):
            if (back_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[3][robot_position[1]] = 'object'
            if (back_object == 3):
                map[2][robot_position[1]] = 'object'
            if (back_object == 4):
                map[1][robot_position[1]] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][1] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][4] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (robot_position[0] == 0 and robot_position[1] == 1):
        if (side == 'front'):
            if (front_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[4][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][0] = 'object'


    
    if (robot_position[0] == 1 and robot_position[1] == 1):
        if (side == 'back'):
            if (back_object == 1):
                map[0][robot_position[1]] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 2 and robot_position[1] == 1):
        if (side == 'back'):
            if (back_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 3 and robot_position[1] == 1):
        if (side == 'back'):
            if (back_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[1][robot_position[1]] = 'object'
            if (back_object == 3):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 4 and robot_position[1] == 1):
        if (side == 'back'):
            if (back_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[2][robot_position[1]] = 'object'
            if (back_object == 3):
                map[1][robot_position[1]] = 'object'
            if (back_object == 4):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 5 and robot_position[1] == 1):
        if (side == 'back'):
            if (back_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[3][robot_position[1]] = 'object'
            if (back_object == 3):
                map[2][robot_position[1]] = 'object'
            if (back_object == 4):
                map[1][robot_position[1]] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][2] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 4):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][0] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (robot_position[0] == 0 and robot_position[1] == 2):
        if (side == 'front'):
            if (front_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[4][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][1] = 'object'
            if (right_object == 2):
                map[robot_position[0]][0] = 'object'
    
    if (robot_position[0] == 1 and robot_position[1] == 2):
        if (side == 'back'):
            if (back_object == 1):
                map[0][robot_position[1]] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][1] = 'object'
            if (right_object == 2):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 2 and robot_position[1] == 2):
        if (side == 'back'):
            if (back_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][1] = 'object'
            if (right_object == 2):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 3 and robot_position[1] == 2):
        if (side == 'back'):
            if (back_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[1][robot_position[1]] = 'object'
            if (back_object == 3):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][5] = 'object'
                
        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][1] = 'object'
            if (right_object == 2):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 4 and robot_position[1] == 2):
        if (side == 'back'):
            if (back_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[2][robot_position[1]] = 'object'
            if (back_object == 3):
                map[1][robot_position[1]] = 'object'
            if (back_object == 4):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][1] = 'object'
            if (right_object == 2):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 5 and robot_position[1] == 2):
        if (side == 'back'):
            if (back_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[3][robot_position[1]] = 'object'
            if (back_object == 3):
                map[2][robot_position[1]] = 'object'
            if (back_object == 4):
                map[1][robot_position[1]] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][3] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 3):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][1] = 'object'
            if (right_object == 2):
                map[robot_position[0]][0] = 'object' 


    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (robot_position[0] == 0 and robot_position[1] == 3):
        if (side == 'front'):
            if (front_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[4][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][2] = 'object'
            if (right_object == 2):
                map[robot_position[0]][1] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][0] = 'object' 


    if (robot_position[0] == 1 and robot_position[1] == 3):
        if (side == 'back'):
            if (back_object == 1):
                map[0][robot_position[1]] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][2] = 'object'
            if (right_object == 2):
                map[robot_position[0]][1] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 2 and robot_position[1] == 3):
        if (side == 'back'):
            if (back_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][2] = 'object'
            if (right_object == 2):
                map[robot_position[0]][1] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 3 and robot_position[1] == 3):
        if (side == 'back'):
            if (back_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[1][robot_position[1]] = 'object'
            if (back_object == 3):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][5] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][2] = 'object'
            if (right_object == 2):
                map[robot_position[0]][1] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][0] = 'object'  

    if (robot_position[0] == 4 and robot_position[1] == 3):
        if (side == 'back'):
            if (back_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[2][robot_position[1]] = 'object'
            if (back_object == 3):
                map[1][robot_position[1]] = 'object'
            if (back_object == 4):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][2] = 'object'
            if (right_object == 2):
                map[robot_position[0]][1] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 5 and robot_position[1] == 3):
        if (side == 'back'):
            if (back_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[3][robot_position[1]] = 'object'
            if (back_object == 3):
                map[2][robot_position[1]] = 'object'
            if (back_object == 4):
                map[1][robot_position[1]] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][4] = 'object' 
            if (left_object == 2):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][2] = 'object'
            if (right_object == 2):
                map[robot_position[0]][1] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][0] = 'object'

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (robot_position[0] == 0 and robot_position[1] == 4):
        if (side == 'front'):
            if (front_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[4][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][3] = 'object'
            if (right_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][1] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][0] = 'object' 

    if (robot_position[0] == 1 and robot_position[1] == 4):
        if (side == 'back'):
            if (back_object == 1):
                map[0][robot_position[1]] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][3] = 'object'
            if (right_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][1] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 2 and robot_position[1] == 4):
        if (side == 'back'):
            if (back_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][3] = 'object'
            if (right_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][1] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 3 and robot_position[1] == 4):
        if (side == 'back'):
            if (back_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[1][robot_position[1]] = 'object'
            if (back_object == 3):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][3] = 'object'
            if (right_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][1] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][0] = 'object'

    if (robot_position[0] == 4 and robot_position[1] == 4):
        if (side == 'back'):
            if (back_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[2][robot_position[1]] = 'object'
            if (back_object == 3):
                map[1][robot_position[1]] = 'object'
            if (back_object == 4):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][3] = 'object'
            if (right_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][1] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][0] = 'object' 


    if (robot_position[0] == 5 and robot_position[1] == 4):
        if (side == 'back'):
            if (back_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[3][robot_position[1]] = 'object'
            if (back_object == 3):
                map[2][robot_position[1]] = 'object'
            if (back_object == 4):
                map[1][robot_position[1]] = 'object'
        
        if (side == 'left'):
            if (left_object == 1):
                map[robot_position[0]][5] = 'object' 

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][3] = 'object'
            if (right_object == 2):
                map[robot_position[0]][2] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][1] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][0] = 'object'   

    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    if (robot_position[0] == 0 and robot_position[1] == 5):
        if (side == 'front'):
            if (front_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[4][robot_position[1]] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][4] = 'object'
            if (right_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][2] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][1] = 'object'  

    if (robot_position[0] == 1 and robot_position[1] == 5):
        if (side == 'back'):
            if (back_object == 1):
                map[0][robot_position[1]] = 'object' 

        if (side == 'front'):
            if (front_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 4):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][4] = 'object'
            if (right_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][2] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][1] = 'object' 

    if (robot_position[0] == 2 and robot_position[1] == 5):
        if (side == 'back'):
            if (back_object == 1):
                map[1][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 3):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][4] = 'object'
            if (right_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][2] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][1] = 'object' 

    if (robot_position[0] == 3 and robot_position[1] == 5):
        if (side == 'back'):
            if (back_object == 1):
                map[2][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[1][robot_position[1]] = 'object'
            if (back_object == 3):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (front_object == 2):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][4] = 'object'
            if (right_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][2] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][1] = 'object' 

    if (robot_position[0] == 4 and robot_position[1] == 5):
        if (side == 'back'):
            if (back_object == 1):
                map[3][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[2][robot_position[1]] = 'object'
            if (back_object == 3):
                map[1][robot_position[1]] = 'object'
            if (back_object == 4):
                map[0][robot_position[1]] = 'object'

        if (side == 'front'):
            if (front_object == 1):
                map[5][robot_position[1]] = 'object' 
        
        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][4] = 'object'
            if (right_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][2] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][1] = 'object' 


    if (robot_position[0] == 5 and robot_position[1] == 5): 
        if (side == 'back'):
            if (back_object == 1):
                map[4][robot_position[1]] = 'object' 
            if (back_object == 2):
                map[3][robot_position[1]] = 'object'
            if (back_object == 3):
                map[2][robot_position[1]] = 'object'
            if (back_object == 4):
                map[1][robot_position[1]] = 'object'

        if (side == 'right'):
            if (right_object == 1):
                map[robot_position[0]][4] = 'object'
            if (right_object == 2):
                map[robot_position[0]][3] = 'object' 
            if (right_object == 3):
                map[robot_position[0]][2] = 'object'    
            if (right_object == 4):
                map[robot_position[0]][1] = 'object'      