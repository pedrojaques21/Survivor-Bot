from common import *

def shot():
    ev3.speaker.play_file("gun_shot.wav")
    gun.run_time(700,3000)
    return 0

def stun():
    gun.run_time(700,4000)

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
