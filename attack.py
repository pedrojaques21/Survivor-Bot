from common import *

def shot():

    global POSSIBLE_ATTACKS
    gun.run_time(700,3000)
    POSSIBLE_ATTACKS.pop(1)

def stun():
    gun.run_time(700,3000)

def random_attack():
    attack = choice(POSSIBLE_ATTACKS)
    print ('ATTACK: ' + str(attack))
    if attack == 'STUN':
        stun()
        wait(1500)
        ev3.speaker.play_file(SoundFile.KUNG_FU)
    else:
        shot()
        wait(1500)
        ev3.speaker.play_file(SoundFile.OUCH)
