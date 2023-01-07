from common import *

def detect_bullet():

    global POSSIBLE_ATTACKS
    color = color_sensor.color()
    if(color == Color.BROWN or color == Color.YELLOW): # Color detected, BROWN OR YELLOW because of the lightning
        print("Color detected: " + str(color))
        ev3.speaker.say('Bullet found!')
        POSSIBLE_ATTACKS.append('SHOT')
        wait(2000)

def detect_motorcycle_part(): 

    global motorcycle_parts_counter
    color = color_sensor.color()
    if(color == Color.GREEN):     #Color green detected, motorcycle part
        print(color)
        ev3.speaker.say('Motorcycle part found!')
        ev3.speaker.play_file(SoundFile.CHEERING)
        motorcycle_parts_counter = motorcycle_parts_counter + 1
        print('Parts found: ' + str(parts_counter))
        wait(2000)
