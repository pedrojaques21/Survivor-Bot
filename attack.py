left_arm_motor = Motor(Port.A)

#Variables
POSSIBLE_ATTACKS = ['STUN','SHOT'] # SHOT only joins array when bullet is found


def shot():
    left_arm_motor.run_time(700,3000)
    bullet = bullet - 1
    print('Bullets available: ' + str(bullet))

def stun():
    left_arm_motor.run_time(700,3000)

def random_attack():

    attack = choice(POSSIBLE_ATTACKS)
    print ('ATTACK: ' + str(attack))
        
    if attack == 'STUN':
        if(bullet == 1):
            shot()
            wait(1500)
            ev3.speaker.play_file(SoundFile.OUCH)
        else:
            stun()
            wait(1500)
            ev3.speaker.play_file(SoundFile.KUNG_FU)
