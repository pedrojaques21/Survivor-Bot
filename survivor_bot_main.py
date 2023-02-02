#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from urandom import choice
from array import *

from heuristica import *

#   Definição do EV3 Brick
ev3 = EV3Brick()

#   Definição dos motores e das suas devidas portas
gun = Motor(Port.A) 
left_leg = Motor(Port.B)
right_leg = Motor(Port.C)

color_sensor = ColorSensor(Port.S1)
left_shoulder = TouchSensor(Port.S2)
right_shoulder = TouchSensor(Port.S3)
eyes = UltrasonicSensor(Port.S4)

#   Definição da base de movimentação do robot
robot = DriveBase(left_leg, right_leg, 25, 105)
robot.settings(190, 100, 190, 100)

#   Distancias dos quadrados da matriz para o robot se movimentar
BACK_DISTANCE = -200
DRIVE_DISTANCE = 200

#   Listas com diferentes movimentos.
POSSIBLE_MOVEMENTS = ['FRONT', 'BACK', 'RIGHT', 'LEFT', 'DOUBLE']
POSSIBLE_DOUBLE = ['FRONT-FRONT','FRONT-RIGHT','FRONT-LEFT','BACK-BACK','BACK-RIGHT','BACK-LEFT','LEFT-LEFT',
    'LEFT-FRONT','LEFT-BACK','RIGHT-RIGHT','RIGHT-FRONT','RIGHT-BACK']
POSSIBLE_ATTACKS = ['STUN'] # SHOT only joins array when the bullet is found!

#   Definição da posição inicial e do objetivo inicial do robot
goal = [5,5]
robot_position = [4,5]  # Contém sempre a posição do robot ao longo do jogo

#   Variaveis
plays_counter = 0   #   Variavel que contabiliza o número de jogadas do robot até à vitória
parts_counter = 0   #   Variavel que contabiliza o número de peças que tem na sua posse
parts_moto = 0      #   Variavel que contabiliza o número de peças já montadas na moto

#   Variaveis que indicam a quantas casas de distância e a direção a que se encontra um objeto
left_object = 0
right_object = 0
front_object = 0
back_object = 0

#   Variaveis que indicam a direção em que o robot atacou um zombie
run_left = 0 
run_front = 0
run_back = 0
run_right = 0
bullet = 0

#   Mantem uma matriz visual para saber a posição dos agentes do ambiente
#   As nossas coordenadas são: x - colunas; y - linhas
map = [
    ['0','0','0','0','0','0'],
    ['0','0','0','0','0','0'],
    ['0','0','0','0','0','0'],
    ['0','0','0','0','0','0'],
    ['0','0','0','0','0','0'],
    ['0','0','0','0','0','0']
]

def detect_bullet():    #   Função que permite ao robot detectar a bala, lendo a cor da casa onde se encontra

    global POSSIBLE_ATTACKS
    global bullet
    color = color_sensor.color()
    if(color == Color.BROWN or color == Color.YELLOW):  #   Se detectar a cor amarela (ou castanha devido à luminosidade)
        ev3.speaker.say('Bullet found!')                #   Diz que encontrou uma bala
        bullet = bullet + 1
        POSSIBLE_ATTACKS.append('SHOT')                 #   Adiciona à lista de ataques possiveis a opção tiro
        wait(2000)

def detect_motorcycle_part():   #   Função que permite ao robot detectar uma peça da mota, lendo a cor da casa onde se encontra

    global parts_counter
    if(parts_counter == 0):     #   Se não tiver nenhuma peça nas mãos
        color = color_sensor.color()
        if(color == Color.GREEN):     # E detectar a cor verde, indicando que o objeto é uma peça da mota
            ev3.speaker.say('Motorcycle part found!')
            ev3.speaker.play_file(SoundFile.CHEERING)
            parts_counter = parts_counter + 1   #   Incrementa o contador das peças que tem em mãos
            print('Parts found: ' + str(parts_counter))
            wait(2000)
            goal = [5,5]    #   Sempre que apanha uma peça atualiza o objetivo atual para a posição da mota
    else:
        ev3.speaker.say('Already have motorcycle part') # Caso já tenha uma peça da mota em mãos ignora a peça encontrada

#   Função que dispara a bala
def shot():
    gun.run_time(700,3000)
    return 0

#   Função que usa a machete
def stun():
    gun.run_time(700,4000)
    return 0

#   Função que permite efetuar um ataque
def random_attack():
    global bullet
    attack = choice(POSSIBLE_ATTACKS)   #   Escolhe uma opção da lista de ataques possiveis
    if bullet == 1:                # Verifica se tem a bala para poder usar o shot para matar o zombi
        ev3.speaker.play_file("Gun_Shot_Sound.wav")  # Se for shot, faz um som de tiro e executa a função shot
        shot()
        bullet = 0
        wait(1000) #espera
    else:                               # Se não tem a bala o robô ataca com a machete, deixando o zombie com "stun"
        ev3.speaker.play_file(SoundFile.KUNG_FU) #   Se for stun, faz um som de stun e executa a função do stun
        stun()
        wait(1000) #espera

#--- funções que atualizam a posição do robot na matriz visual interna -----
def update_robot_position (lines,columns):
    map[lines][columns] = 'robot'

def reset_robot_position (lines, columns):
    map[lines][columns] = '0'

#--------------------------------------------------------------------------
#funcao que coloca os objetos reconhecidos na matriz visual interna
def update_matrix_info(x,y):
    map[y][x]='object'

#função que efetua o reconhecimento de objetos para a direita
def recon_right():
    global right_object
    if(eyes.distance() <= 370): #se a distancia do objeto for inferior a 370, entao o objeto está a 1 casa de distancia
        if(robot_position[0]>=1): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 1 casas - Right') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            right_object = 1  #a variavel fica a 1, pois está um objeto a 1 casa de distancia
            update_matrix_info(robot_position[0]-1, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=380 and eyes.distance()<=640): #se a distancia do objeto for inferior a 640, entao o objeto está a 2 casas de distancia
        if(robot_position[0]>=2): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 2 casas - Right') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            right_object = 2  #a variavel fica a 2, pois está um objeto a 2 casas de distancia
            update_matrix_info(robot_position[0]-2, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=650 and eyes.distance()<=890): #se a distancia do objeto for inferior a 890, entao o objeto está a 3 casas de distancia
        if(robot_position[0]>=3): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 3 casas - Right') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            right_object = 3  #a variavel fica a 3, pois está um objeto a 3 casas de distancia
            update_matrix_info(robot_position[0]-3, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=900 and eyes.distance()<=1060): #se a distancia do objeto for inferior a 1060, entao o objeto está a 4 casas de distancia
        if(robot_position[0]>=4): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 4 casas - Right')  # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            right_object = 4 #a variavel fica a 4, pois está um objeto a 4 casas de distancia
            update_matrix_info(robot_position[0]-4, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    return 0

#funcao de reconhecimento para a esquerda
def recon_left():
    global left_object
    if(eyes.distance() <= 370): #se a distancia do objeto for inferior a 370, entao o objeto está a 1 casa de distancia
        if(robot_position[0]<=4): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 1 casas - Left') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            left_object = 1  #a variavel fica a 1, pois está um objeto a 1 casa de distancia
            update_matrix_info(robot_position[0]+1, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=380 and eyes.distance()<=640): #se a distancia do objeto for inferior a 640, entao o objeto está a 2 casas de distancia
        if(robot_position[0]<=3): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 2 casas - Left') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            left_object = 2 #a variavel fica a 2, pois está um objeto a 2 casas de distancia
            update_matrix_info(robot_position[0]+2, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=650 and eyes.distance()<=890): #se a distancia do objeto for inferior a 890, entao o objeto está a 3 casas de distancia
        if(robot_position[0]<=2): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 3 casas - Left') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            left_object = 3  #a variavel fica a 3, pois está um objeto a 3 casas de distancia
            update_matrix_info(robot_position[0]+3, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=900 and eyes.distance()<=1060): #se a distancia do objeto for inferior a 1060, entao o objeto está a 4 casas de distancia
        if(robot_position[0]<=1): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 4 casas - Left')  # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            left_object = 4 #a variavel fica a 4, pois está um objeto a 4 casas de distancia
            update_matrix_info(robot_position[0]+4, robot_position[1]) #coloca o objeto reconhecido na matriz interna
    return 0

#funcao de reconhecimento para a frente
def recon_front():
    global front_object
    if(eyes.distance() <= 370): #se a distancia do objeto for inferior a 370, entao o objeto está a 1 casa de distancia
        if(robot_position[1]<=4): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 1 casas - Front') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            front_object = 1  #a variavel fica a 1, pois está um objeto a 1 casa de distancia
            update_matrix_info(robot_position[0], robot_position[1]+1) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=380 and eyes.distance()<=640): #se a distancia do objeto for inferior a 640, entao o objeto está a 2 casas de distancia
        if(robot_position[1]<=3): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 2 casas - Front') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            front_object = 2 #a variavel fica a 2, pois está um objeto a 2 casas de distancia
            update_matrix_info(robot_position[0], robot_position[1]+2) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=650 and eyes.distance()<=890): #se a distancia do objeto for inferior a 890, entao o objeto está a 3 casas de distancia
        if(robot_position[1]<=2): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 3 casas - Front') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            front_object = 3  #a variavel fica a 3, pois está um objeto a 3 casas de distancia
            update_matrix_info(robot_position[0], robot_position[1]+3) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=900 and eyes.distance()<=1060): #se a distancia do objeto for inferior a 1060, entao o objeto está a 4 casas de distancia
        if(robot_position[1]<=1): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 4 casas - Front')  # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            front_object = 4 #a variavel fica a 4, pois está um objeto a 4 casas de distancia
            update_matrix_info(robot_position[0], robot_position[1]+4) #coloca o objeto reconhecido na matriz interna
    return 0

#funcao de reconhecimento para trás
def recon_back():
    global back_object

    if(eyes.distance() <= 370): #se a distancia do objeto for inferior a 370, entao o objeto está a 1 casa de distancia
        if(robot_position[1]>=1): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 1 casas - Back') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            back_object = 1  #a variavel fica a 1, pois está um objeto a 1 casa de distancia
            update_matrix_info(robot_position[0], robot_position[1]-1) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=380 and eyes.distance()<=640): #se a distancia do objeto for inferior a 640, entao o objeto está a 2 casas de distancia
        if(robot_position[1]>=2): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 2 casas - Back') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            back_object = 2 #a variavel fica a 2, pois está um objeto a 2 casas de distancia
            update_matrix_info(robot_position[0], robot_position[1]-2) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=650 and eyes.distance()<=890): #se a distancia do objeto for inferior a 890, entao o objeto está a 3 casas de distancia
        if(robot_position[1]>=3): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 3 casas - Back') # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            back_object = 3 #a variavel fica a 3, pois está um objeto a 3 casas de distancia
            update_matrix_info(robot_position[0], robot_position[1]-3) #coloca o objeto reconhecido na matriz interna
    if(eyes.distance()>=900 and eyes.distance()<=1060): #se a distancia do objeto for inferior a 1060, entao o objeto está a 4 casas de distancia
        if(robot_position[1]>=4): #verifica a posicao do robot, para nao haver reconhecimentos fora da matriz
            print('Objeto - 4 casas - Back')  # coloca o texto na consola para o utilizador saber que foi reconhecido um objeto
            back_object = 4 #a variavel fica a 4, pois está um objeto a 4 casas de distancia
            update_matrix_info(robot_position[0], robot_position[1]-4) #coloca o objeto reconhecido na matriz interna

    return False

#--------------------------------------------------------------------------
#funcao que define o movimento que o robot irá fazer, dependendo se já apanhou uma peça ou nao, e
#se houver objetos perto
def move(f,r,b,l):

    global parts_counter
    global front_object, right_object, left_object, back_object
    global run_left, run_front, run_back, run_right 

    #inicialização de variaveis auxiliares aos lados
    auxF = 0 #auxiliar frente
    auxL = 0 #auxiliar esquerda
    auxB = 0 #auxiliar atrás
    auxR = 0 #auxiliar direita
    aux = 0

    #atribuição dos valores recebidos pela funcao às variaveis locais
    front_object = f
    right_object = r
    left_object = l
    back_object = b

    #se o robot identificar algum objeto, seja o lado que for, a variavel auxiliar fica a 1
    if (front_object != 0):
        auxF = 1
    if (right_object != 0):
        auxL = 1
    if (left_object != 0):
        auxB = 1
    if (back_object != 0):
        auxR = 1

    #soma de todas as variaveis auxiliares, para termos o numero de objetos identificados
    aux = auxF + auxB + auxL + auxR

    if(parts_counter == 0): #se o numero de peças apanhadas for 0
        if (aux == 1): #se o numero de objetos identificados for 1
            if(front_object != 0): #e existir um objeto à frente do robot
                if(run_front == 0): # se não atacou um zombie
                    if(front_object == 1): #tem um objecto à frente a uma casa de distancia
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha e só tem um objeto à sua frente, é um zombie 
                            print('Recon ' + str(color)) # coloca na consola a cor detetada                                
                            ev3.speaker.say('Zombie very close') # o robô indica que sabe que tem um zombie que está perto 
                            wait(2000) #espera
                            random_attack() #realiza um ataque
                            run_front = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para a frente

                        else: #se a cor nao for vermelha, entao é um objeto
                            move_front() #move-se para a frente
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera
                    elif(front_object == 2): #tem um objecto à frente a duas casas de distancia
                        color = color_sensor.color()
                        if(color == Color.BLUE): #se a cor detetada é azul entao pode estar um zombie por perto
                            wait(1000) #espera
                            move_front() #move-se para a frente
                            color = color_sensor.color()
                            if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                                color = color_sensor.color()
                                if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                                    print('Recon ' + str(color)) # coloca na consola a cor detetada                                
                                    ev3.speaker.say('Zombie very close') # o robô indica que sabe que tem um zombie que está perto
                                    wait(2000) #espera
                                    robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                                    wait(1000) #espera
                                    random_attack() #realiza um ataque
                                    run_front = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para a frente

                                else: #se a cor nao for vermelha, entao é um objeto
                                    wait(1000) #espera
                                    detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                    detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                    wait(1000) #espera
                                    robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para completar o movimento
                            else:
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder apanhar o objeto
                                wait(1000) #espera
                                detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                wait(1000) #espera
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder completar o movimento
                        else:
                            secure_movement() #faz movimentos de 1 casa, por segurança

                    elif (front_object ==3): #tem um objecto à frente a tres casas de distancia
                        secure_movement() #faz movimentos de 1 casa, por segurança
                    else:
                        move_front() #o robô irá efetuar um movimento duplo pois o objeto nesta verificação está a 4 casas para poder aproximar-se o mais rapidamente possível
                        move_front() 
                else:
                    run_front = 0 #reseta a variavel porque o robot ja pode mover-se para a frente
                    if(robot_position[0] <4): #verifica se a sua posição x é inferior a 4, pois se fosse superior o robô poderia sair do tabuleiro 
                        move_left() #o robô irá efetuar um movimento duplo após ataque o robô para afastar-se do zombie
                        move_left() 
                    elif(robot_position[0] >4): #verifica se a sua posição x é superior a 4, pois se fosse inferior o robô poderia sair do tabuleiro
                        move_right()  #o robô irá efetuar um movimento duplo após ataque o robô para afastar-se do zombie
                        move_right() 
                    elif(robot_position[1] >4): #verifica se a sua posição y é superior a 4, pois se fosse inferior o robô poderia sair do tabuleiro
                        move_back() #o robô irá efetuar um movimento duplo após ataque o robô para afastar-se do zombie
                        move_back() 

    #LEFT---------------------------------------------------------------------------------------------

            if(left_object != 0): # se existir um objeto á sua esquerda 
                if(run_left == 0): # se não atacou um zombie 
                    if(left_object == 1): #tem um objecto à esquerda a um casa de distancia
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha e só tem um objeto à sua esquerda, é um zombie 
                            robot.turn(-128) #vira -128º, para a esquerda para poder ficar de frente para o zombie
                            print('Recon ' + str(color)) # coloca na consola a cor detetada                                 
                            ev3.speaker.say('Zombie very close') # o robô indica que sabe que tem um zombie que está perto
                            wait(2000) #espera
                            random_attack() #realiza um ataque
                            run_left = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para a esquerda
                            robot.turn(128) #vira 128º, para a posição inicial, para a frente
                        else: # se não detetou nenhuma cor significa que é um objeto
                            move_left() #move-se para a esquerda
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera
                             
                    elif(left_object == 2): #tem um objecto à esquerda a duas casas de distancia
                        color = color_sensor.color()
                        if(color == Color.BLUE): #se a cor detetada é azul entao tem um zombie por perto
                            wait(1000) #espera
                            move_left() #move-se para a esquerda
                            color = color_sensor.color()
                            if(color == Color.RED):  #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                                robot.turn(-128) #vira -128º, para a esquerda, para ir na direção do objeto 
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                                color = color_sensor.color()
                                if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                                    print('Recon ' + str(color)) # coloca na consola a cor detetada                               
                                    ev3.speaker.say('Zombie very close') # o robô indica que sabe que tem um zombie que está perto
                                    wait(2000) #espera
                                    robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                                    wait(1000) #espera
                                    random_attack() #realiza um ataque
                                    run_left = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para a esquerda
                                    robot.turn(128) #vira 128º, para a posição inicial, para a frente
                                else: #se a cor nao for vermelha, entao é um objeto
                                    wait(1000) #espera
                                    detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                    detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                    wait(1000) #espera
                                    robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para completar o movimento
                                    robot.turn(128) #vira 128º, para a posição inicial, para a frente
                            else:
                                robot.turn(-128)
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder apanhar o objecto
                                wait(1000) #espera
                                detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                wait(1000) #espera
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder completar o movimento
                                robot.turn(128) #vira 128º, para a posição inicial, para a frente
                        else:
                            secure_movement() #faz movimentos de 1 casa, por segurança

                    elif (left_object ==3): #tem um objecto à esquerda a tres casas de distancia
                        secure_movement() #faz movimentos de 1 casa, por segurança 
                    else:
                        move_left() #o robô irá efetuar um movimento duplo pois o objeto nesta verificação está a 4 casas para poder aproximar-se o mais rapidamente possível
                        move_left() 
                else:
                    run_left = 0 #reseta a variavel porque o robot ja pode mover-se para a esquerda
                    if(robot_position[0] >4): #verifica se a sua posição x é superior a 4, pois se fosse inferior o robô poderia sair do tabuleiro
                        move_right()  #o robô irá efetuar um movimento duplo após ataque o robô para afastar-se do zombie
                        move_right() 
                    elif(robot_position[1] <4): #verifica se a sua posição y é inferior a 4, pois se fosse superior o robô poderia sair do tabuleiro
                        move_front() #o robô irá efetuar um movimento duplo após ataque o robô para afastar-se do zombie
                        move_front() 
                    elif(robot_position[1] >4): #verifica se a sua posição y é superior a 4, pois se fosse inferior o robô poderia sair do tabuleiro
                        move_back() #o robô irá efetuar um movimento duplo após ataque o robô para afastar-se do zombie
                        move_back() 

    #BACK-------------------------------------------------------------------------------------------------------

            if(back_object != 0): #se existir um objeto atrás do robô
                if(run_back == 0): # se não atacou um zombie 
                    if(back_object == 1): #tem um objecto atrás a uma casa de distancia
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha e só tem um objeto atrás, é um zombie 
                            robot.turn(-180) #vira -180º, para atrás, para ficar de frente para o objeto
                            print('Recon ' + str(color)) # coloca na consola a cor detetada                                 
                            ev3.speaker.say('Zombie very close') # o robô indica que sabe que tem um zombie que está perto
                            wait(2000) #espera
                            random_attack() #realiza um ataque
                            run_back = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para trás
                            robot.turn(180) #vira 180º, para a posição inicial, para a frente
                        else:#se não tem cor,significa que é um objeto
                            move_back() #move-se para trás
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera

                    elif(back_object == 2): #tem um objecto atrás a duas casas de distancia
                        color = color_sensor.color()
                        if(color == Color.BLUE): #se a cor detetada é azul entao pode estar um zombie por perto
                            wait(1000) #espera
                            move_back() #move-se para atrás
                            color = color_sensor.color()
                            if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                                robot.turn(-180) #vira -180º, para atrás
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                                color = color_sensor.color()
                                if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                                    print('Recon ' + str(color)) #coloca na consola a cor detetada                               
                                    ev3.speaker.say('Zombie very close') #o robô indica que sabe que tem um zombie perto
                                    wait(2000) #espera
                                    robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                                    wait(1000) #espera
                                    random_attack() #realiza o ataque
                                    run_back = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para atrás
                                    robot.turn(180) #vira 180º, para a posição inicial, para a frente
                                else:#se ao avançar meia casa não detetar vermelho, significa que não é o zombie que está nas suas costas
                                    wait(1000) #espera
                                    detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                    detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                    wait(1000) #espera
                                    robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para completar o movimento
                                    robot.turn(180) #vira 180º, para a posição inicial, para a frente
                            else: # se não deteta cor é um objeto
                                robot.turn(-180)
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder apanhar o objecto
                                wait(1000) #espera
                                detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                wait(1000) #espera
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder completar o movimento
                                robot.turn(180) #vira 180º, para a posição inicial, para a frente
                        else:
                            secure_movement() #faz movimentos de 1 casa, por segurança

                    elif (back_object ==3): #tem um objecto à frente a três casas de distancia
                        secure_movement() #faz movimentos de 1 casa, por segurança
                    else:
                        move_back() #faz um movimento duplo para chegar o mais rapidamente possível do objeto
                        move_back() 
                else:
                    run_back = 0 #reseta a variavel porque o robot ja pode mover-se para atras
                    if(robot_position[0] <4): #verifica se a posicao x do robô é inferior a 4, pois se fosse superior o robô podia sair do tabuleiro
                        move_left() #realiza um movimento duplo para afastar-se do zombie
                        move_left()
                    elif(robot_position[0] >4):
                        move_right() #realiza um movimento duplo para afastar-se do zombie
                        move_right() 
                    elif(robot_position[1] <4):
                        move_front() #realiza um movimento duplo para afastar-se do zombie
                        move_front()      

    #RIGHT-----------------------------------------------------------------------------------------------------

            if(right_object != 0): #se existir um objeto à direita do robô
                if (run_right == 0): #se a variavel é igual a zero, significa que o robot pode mover-se para qualquer direção
                    if(right_object == 1): #tem um objecto à frente a uma casa de distancia
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha e tem um objeto à direita,é um zombie
                            robot.turn(128) #vira 128º, para a direita, para ficar de frente para o objeto
                            print('Recon ' + str(color)) #coloca na consola a cor detetada
                            ev3.speaker.say('Zombie very close') #o robô indica que sabe que tem um zombie perto
                            wait(2000) #espera
                            random_attack() #realiza um ataque
                            run_right = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para a direita
                            robot.turn(-128) #vira -128º, para a posição inicial, para a frente
                        else: # se não detetar cor é um objeto
                            move_right() #move-se para a direita
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera

                    elif(right_object == 2): #tem um objecto à direita a duas casas de distancia
                        color = color_sensor.color()
                        if(color == Color.BLUE): #se a cor detetada é azul entao pode estar um zombie por perto
                            wait(1000) #espera
                            move_right()  #move-se para a direita
                            color = color_sensor.color()
                            if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                                robot.turn(128) #vira 128º, para a direita
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                                color = color_sensor.color()
                                if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                                    print('Recon ' + str(color)) # coloca na consola a cor detetada
                                    ev3.speaker.say('Zombie very close') # o robô indica que sabe que tem um zombie perto
                                    wait(2000) #espera
                                    robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                                    wait(1000) #espera
                                    random_attack() #realiza um ataque
                                    robot.turn(-128) #vira -128º, para a posição inicial, para a frente
                                else:#se não deteta a cor vermelha significa que o zombie não está no seu campo de visão e vai pegar o objeto
                                    wait(1000) #espera
                                    detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                    detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                    wait(1000) #espera
                                    robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para completar o movimento
                                    robot.turn(-128) #vira -128º, para a posição inicial, para a frente
                            else: # se não deteta cor significa que é um objeto
                                robot.turn(128) #vira 128º, para a direita
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder apanhar o objeto
                                wait(1000) #espera
                                detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                                detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                                wait(1000) #espera
                                robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder completar o movimento
                                robot.turn(-128) #vira -128º, para a posição inicial, para a frente
                        else:
                            secure_movement() #faz movimentos de 1 casa, por segurança

                    elif (right_object == 3):
                        secure_movement() #faz movimentos de 1 casa, por segurança
                    else:
                        move_right() #faz um movimento duplo para poder se aproximar o mais rapidamente possível do objeto
                        move_right() 
                else:
                    run_right = 0 #reseta a variavel porque o robot ja pode mover-se para a direita
                    if (robot_position[0] <4): # verifica se a posição x do robô é inferior a 4, pois se fosse superior a 4 o robô podia sair do tabuleiro
                        move_left() #faz um movimento duplo para afastar-se do zombie
                        move_left() 
                    elif(robot_position[1] <4): # verifica se a posição y do robô é inferior a 4, pois se fosse superior a 4 o robô podia sair do tabuleiro
                        move_front() #faz um movimento duplo para afastar-se do zombie
                        move_front() 
                    elif(robot_position[1] >4): # verifica se a posição y do robô é superior a 4, pois se fosse inferior a 4 o robô podia sair do tabuleiro
                        move_back() #faz um movimento duplo para afastar-se do zombie
                        move_back() 
                
        if (aux >= 2): #quando o numero de objectos identificados é maior que dois
            calculate_closest_object() #calcula o objeto mais perto do robot
        
        elif(aux == 0): #quando o numero de objectos identificados é zero
            color = color_sensor.color()
            if(color == Color.BLUE): #se a cor detetada é azul significa que tem um zombie perto, mas como não deteta nenhum objeto significa que o zombie está na diagonal do robô
                if(parts_counter !=0 ): #o robot já apanhou uma peça, entao ele vai fugir
                    if(robot_position[0] <4): # verifica se a posição x do robô é inferior a 4, pois se fosse superior a 4 o robô podia sair do tabuleiro
                        move_left() #faz um movimento duplo pois o robô não sabe onde o zombie está e um movimento duplo é mais seguro pois ao fazer um movimento de uma casa o zombie pode estar á sua espera
                        move_left() 
                    elif(robot_position[0] >4): # verifica se a posição x do robô é superior a 4, pois se fosse inferior a 4 o robô podia sair do tabuleiro
                        move_right() #faz um movimento duplo pois o robô não sabe onde o zombie está e um movimento duplo é mais seguro pois ao fazer um movimento de uma casa o zombie pode estar á sua espera
                        move_right() 
                    elif(robot_position[1] <4): # verifica se a posição y do robô é inferior a 4, pois se fosse superior a 4 o robô podia sair do tabuleiro
                        move_front() #faz um movimento duplo pois o robô não sabe onde o zombie está e um movimento duplo é mais seguro pois ao fazer um movimento de uma casa o zombie pode estar á sua espera
                        move_front() #
                    elif(robot_position[1] >4): # verifica se a posição y do robô é superior a 4, pois se fosse inferior a 4 o robô podia sair do tabuleiro
                        move_back() #faz um movimento duplo pois o robô não sabe onde o zombie está e um movimento duplo é mais seguro pois ao fazer um movimento de uma casa o zombie pode estar á sua espera
                        move_back() 
                else:
                    return 0

            else: #se nao detetar cor azul, entao ele continua para o objetivo [5,5]
                print('I am going to move') #coloca na consola o texto para demonstrar ao utilizador que vai andar
                ev3.speaker.say('ON MY WAY') #o robô indica que vai começar o movimento
                moveTowardsGoal(robot_position,goal) #se não forem realizadas as verificações anteriores o movimento passa a usar a heuristica
                print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1])) #coloca na consola a matriz atualizada para demonstrar ao utilizador onde o robô deveria estar

    #quando o robot já apanhou uma peça, ele vai agir de forma a dar prioridade a colocar a peça na mota
    if(parts_counter != 0):
        if (aux == 1): #quando o numero de objectos identificados é um
            if(front_object == 1): #se a variavel é igual 1, significa que tem um objeto à frente a 1 casa de distancia
                color = color_sensor.color()
                if(color == Color.BLUE): # se a cor é azul tem um zombie perto o robo irá fazer movimentos pequenos porque não quer ariscar morrer já que tem a peça
                    if(robot_position[0] <5): # verifica se a posição x do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_left() #move-se para esquerda
                    elif(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_right() #move-se para a direita
                    elif(robot_position[1] == 5): # verifica se a posição y do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_back() #move-se para trás
                elif(color == Color.RED): # se a cor é vermelha o robô irá tentar fugir do zombie porque tem a peça e é ariscado se aproximar
                    if(robot_position[0] <5):  # verifica se a posição x do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_left() #move-se para esquerda
                    elif(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_right() #move-se para a direita
                    elif(robot_position[1] == 5): # verifica se a posição y do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_back() #move-se para trás

            elif(right_object == 1): #se a variavel é igual 1, significa que tem um objeto à direita a 1 casa de distancia
                color = color_sensor.color()
                if(color == Color.BLUE): # se a cor é azul tem um zombie perto o robo irá fazer movimentos pequenos porque não quer ariscar morrer já que tem a peça
                    if(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_front() #move-se para frente
                    elif(robot_position[0] <5):  # verifica se a posição x do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_left() #move-se para esquerda
                    elif(robot_position[1] == 5): # verifica se a posição y do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_back() #move-se para trás
                elif(color == Color.RED): # se a cor é vermelha o robô irá tentar fugir do zombie porque tem a peça e é ariscado se aproximar
                    if(robot_position[0] == 5):  # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_front() #move-se para frente
                    elif(robot_position[0] <5):  # verifica se a posição x do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_left() #move-se para esquerda
                    elif(robot_position[1] == 5):  # verifica se a posição y do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_back() #move-se para trás

            elif(back_object == 1): #se a variavel é igual 1, significa que tem um objeto atrás a 1 casa de distancia
                color = color_sensor.color()
                if(color == Color.BLUE): # se a cor é azul tem um zombie perto o robo irá fazer movimentos pequenos porque não quer ariscar morrer já que tem a peça
                    if(robot_position[1] <5): # verifica se a posição y do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_front() #move-se para frente
                    elif(robot_position[0] <5): # verifica se a posição x do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_left() #move-se para esquerda
                    elif(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_right() #move-se para a direita
                elif(color == Color.RED): # se a cor é vermelha o robô irá tentar fugir do zombie porque tem a peça e é ariscado se aproximar
                    if(robot_position[1] <5): # verifica se a posição y do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_front() #move-se para frente
                    elif(robot_position[0] <5): # verifica se a posição x do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_left() #move-se para esquerda
                    elif(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_right() #move-se para a direita

            elif(left_object == 1): #se a variavel é igual 1, significa que tem um objeto à esquerda a 1 casa de distancia
                color = color_sensor.color()
                if(color == Color.BLUE): # se a cor é azul tem um zombie perto o robo irá fazer movimentos pequenos porque não quer ariscar morrer já que tem a peça
                    if(robot_position[1] <5): # verifica se a posição y do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_front() #move-se para frente
                    elif(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_right() #move-se para a direita
                    elif(robot_position[1] == 5): # verifica se a posição y do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_back() #move-se para trás

                elif(color == Color.RED): # se a cor é vermelha o robô irá tentar fugir do zombie porque tem a peça e é ariscado se aproximar
                    if(robot_position[1] <5): # verifica se a posição y do robô é inferior a 5, pois se fosse superior a 5 o robô podia sair do tabuleiro
                        move_front() #move-se para frente
                    elif(robot_position[0] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_right() #move-se para a direita
                    elif(robot_position[1] == 5): # verifica se a posição x do robô é igual a 5 , para que o robô não saia do tabuleiro
                        move_back() #move-se para trás

            else: #se nao tiver objeto nenhum, ele continua para o seu objetivo [5,5]
                print('I am going to move') #coloca na consola o texto para o utilizador saber que o robô irá iniciar o movimento
                ev3.speaker.say('ON MY WAY') #o robô indica que vai começar o movimento
                moveTowardsGoal(robot_position,goal) #se não forem realizadas as verificações anteriores o movimento passa a usar a heuristica
                print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1])) #coloca na consola a matriz atualizada com a posição do robô e os objetos detetados

        elif (aux == 2): #quando o numero de objectos identificados é dois
            color = color_sensor.color()
            if(color == Color.BLUE): #se a cor detetada é azul entao pode estar um zombie por perto
                if (front_object == 2): #tem um objecto à frente a duas casas de distancia
                    move_front() #move-se para a frente
                    color = color_sensor.color()
                    if (color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                        robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                            print('Recon ' + str(color)) #coloca na consola a cor detetada                             
                            ev3.speaker.say('Zombie very close') #o robô indica que sabe que tem um zombie perto
                            wait(2000) #espera
                            robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                            wait(1000) #espera
                            random_attack() #realiza um ataque
                        else: # se a cor não é vermelha então é um objeto
                            wait(1000) #espera
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera
                            robot.straight(DRIVE_DISTANCE/2) #ja apanhou o objeto, agora move-se para completar o movimento 

                    else: #se a cor detetada não é vermelha, o robot sabe que esta seguro
                        robot.straight(DRIVE_DISTANCE/2) #move-se em linha reta 100mm para a frente, metado do movimento
                        wait(1000) #espera
                        detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                        detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                        wait(1000) #espera
                        robot.straight(DRIVE_DISTANCE/2) #move-se em linha reta 100mm para a frente, para completar o movimento
                        
                if (left_object == 2 ): #tem um objecto à esquerda a duas casas de distancia
                    move_left() #move-se para a esquerda
                    color = color_sensor.color()
                    if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                        robot.turn(-128) #vira -128º, para a esquerda
                        robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                            print('Recon ' + str(color)) #coloca na consola a cor detetada                                
                            ev3.speaker.say('Zombie very close') #o robô indica que sabe que tem um zombie perto
                            wait(2000) #espera
                            robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                            wait(1000) #espera
                            random_attack() #realiza um ataque
                            robot.turn(128) #vira 128º, para a posiçao inicial, para a frente
                        else: #se a cor detetada não é vermelho, é um objeto
                            wait(1000) #espera
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera
                            robot.straight(DRIVE_DISTANCE/2) #ja apanhou o objeto, agora move-se para completar o movimento 
                            robot.turn(128) #vira 128º, para a posiçao inicial, para a frente

                    else: #se a cor detetada não é vermelha, o robot sabe que esta seguro
                        robot.turn(-128) #vira -128º, para a esquerda
                        robot.straight(DRIVE_DISTANCE/2) #move-se em linha reta 100mm para a frente, metado do movimento
                        wait(1000) #espera
                        detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                        detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                        wait(1000) #espera
                        robot.straight(DRIVE_DISTANCE/2) #move-se em linha reta 100mm para a frente, para completar o movimento
                        robot.turn(128) #vira 128º, para a posiçao inicial, para a frente
                    
                if (back_object == 2): #tem um objecto atrás a duas casas de distancia
                    move_back() #move-se para atrás
                    color = color_sensor.color()
                    if(color == Color.RED):  #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                        robot.turn(-180) #vira -180º, para atras
                        robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para poder verificar a cor
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                            print('Recon ' + str(color)) #coloca na consola a cor detetada                               
                            ev3.speaker.say('Zombie very close') #o robô indica que sabe que tem um zombie perto
                            wait(2000) #espera
                            robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                            wait(1000) #espera
                            random_attack() #realiza um ataque
                            robot.turn(180) #vira 180º, para a posiçao inicial, para a frente
                        else:
                            wait(1000) #espera
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera
                            robot.straight(DRIVE_DISTANCE/2) #ja apanhou o objeto, agora move-se para completar o movimento
                            robot.turn(180) #vira 180º, para a posiçao inicial, para a frente

                    else: #se a cor detetada não é vermelha, o robot sabe que esta seguro
                        robot.turn(-180) #vira -180º, para atras
                        robot.straight(DRIVE_DISTANCE/2) #move-se em linha reta 100mm para a frente, metado do movimento
                        wait(1000) #espera
                        detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                        detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                        wait(1000) #espera
                        robot.straight(DRIVE_DISTANCE/2) #move-se em linha reta 100mm para a frente, para completar o movimento
                        robot.turn(180) #vira 180º, para a posiçao inicial, para a frente
                        
                if (right_object == 2 ): #tem um objecto à direita a duas casas de distancia
                    move_right() #move-se para a direita
                    color = color_sensor.color()
                    if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está perto, mas o robot nao sabe se é a direita ou em outra posicao
                        robot.turn(128) #vira 128º, para a direita
                        robot.straight(DRIVE_DISTANCE/2)  #move-se 1/2 casa para poder verificar a cor
                        color = color_sensor.color()
                        if(color == Color.RED): #se a cor detetada é vermelha, significa que o zombie está nessa casa 
                            print('Recon ' + str(color)) #coloca na consola a cor detetada                                  
                            ev3.speaker.say('Zombie very close') #o robô indica que sabe que tem um zombie perto
                            wait(2000) #espera
                            robot.straight(-DRIVE_DISTANCE/2) #volta para trás, para poder atacar
                            wait(1000) #espera
                            random_attack() #realiza um ataque
                            run_right = 1 #coloca a variavel a 1 para que o robot saiba que nao pode mover-se para a direita
                            robot.turn(-128) #vira -128º, para a posiçao inicial, para a frente
                        else:
                            wait(1000) #espera
                            detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                            detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                            wait(1000) #espera
                            robot.straight(DRIVE_DISTANCE/2) #ja apanhou o objeto, agora move-se para completar o movimento
                            robot.turn(-128) #vira -128º, para a posiçao inicial, para a frente

                    else: #se a cor detetada não é vermelha, o robot sabe que esta seguro
                        robot.turn(128) #vira 128º, para a direita
                        robot.straight(DRIVE_DISTANCE/2) #move-se 1/2 casa para apanhar o objeto
                        wait(1000) #espera
                        detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
                        detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
                        wait(1000) #espera
                        robot.straight(DRIVE_DISTANCE/2)  #move-se em linha reta 100mm para a frente, para completar o movimento
                        robot.turn(-128) #vira -128º, para a posiçao inicial, para a frente
                    
            else: #se nao detetar cor azul, entao ele continua para o objetivo [5,5]
                print('I am going to move') #um print para o utilizador saber que o robô vai se movimentar 
                ev3.speaker.say('ON MY WAY') #o robô indica que vai começar o movimento
                moveTowardsGoal(robot_position,goal) #se não forem realizadas as verificações anteriores o movimento passa a usar a heuristica
                print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1])) #um print da matrix para saber a posição que o robô acaba o movimento 

        else: #quando o numero de objetos identificados é maior que 2, entao ele vai ignorar e vai para o objetivo [5,5]
            print('I am going to move') #um print para o utilizador saber que o robô vai se movimentar
            ev3.speaker.say('ON MY WAY') #o robô indica que vai começar o movimento
            moveTowardsGoal(robot_position,goal) #se não forem realizadas as verificações anteriores o movimento passa a usar a heuristica
            print('My position is: x=' + str(robot_position[0]) + ', y=' + str(robot_position[1])) #um print da matrix para saber a posição que o robô acaba o movimento 


    #reseta os valores das variaveis
    front_object = 0
    right_object = 0
    left_object = 0
    back_object = 0
    
#funcao que calcula o objeto mais perto
def calculate_closest_object():
    global front_object, right_object, left_object, back_object

    auxFO = front_object #atribuindo os valores de objetos detetados a variaveis auxiliares para não alterar as variaveis globais
    auxLO = left_object 
    auxBO = back_object 
    auxRO = right_object 
    #Nesta verificação verificamos se as variaveis que têm os objetos detetados é igual a 0 pois em baixo para decidir que objeto é priorizado é usada a função min()
    #do python para escolher o valor mais pequeno, mas se não existem objetos, a variavel terá o valor 0 e o robô iria dar prioridade a objetos que não existem, então
    #é incrementado nas variaveis o valor 10(foi escolhido aleatoriamente) para que a função min() escolha realmente o valor que está mais perto
    if (front_object == 0):
        auxFO = auxFO + 10 
    if (right_object == 0):
        auxRO = auxRO + 10 
    if (left_object == 0):
        auxLO = auxLO + 10 
    if (back_object == 0):
        auxBO = auxBO + 10 
    
    numbers = [auxFO, auxRO, auxLO, auxBO] #colocamos todas as variaveis dentro de uma lista
    perto = min(numbers) #comparamos todas as variaveis para determinar a mais pequena
    #Nestas verificações o código irá entrar novamente na função move() e dependendo do objeto detetado irá receber o objeto priorizado e irá esquecer o restos dos
    #objetos pois assim é como se tivesse detetado só um objeto e podemos reaproveitar o código usado anteriormente
    
    #se o objeto mais perto esta à frente, o robot vai focar apenas nesse objeto
    if (front_object == perto):
        move(front_object,0,0,0) 
    
    #se o objeto mais perto esta à esquerda, o robot vai focar apenas nesse objeto
    elif (left_object == perto):
        move(0,0,0,left_object)

    #se o objeto mais perto esta à direita, o robot vai focar apenas nesse objeto
    elif (right_object == perto):
        move(0,right_object,0,0)
    
    #se o objeto mais perto esta atras, o robot vai focar apenas nesse objeto
    elif (back_object == perto):
        move(0,0,back_object,0)
        
#funcao para que o robot faça apenas movimentos de 1 casa, por segurança
def secure_movement():
    #se o objeto está a 2 casas o robô poderá não detetar nenhuma cor e o zombie poderá estar ao lado do objeto e se for uma peça de uma mota o robô perde
    #se o objeto está a 3 casas o robô poderá não detetar nenhuma cor e o zombie poderá estar no meio do caminho e o robô poderá perder
    
    #se o bloco encontrado esta a mais de 2 blocos de distancia, ele avança 1 casa com cuidado
    if (front_object >= 2 ):
        print("!! moving one block, because zombie might be nearby !!") #coloca na consola o texto para o utilizador saber que o robô está usando a função secure_movement
        ev3.speaker.say('BE CAREFUL') #o robô indica que irá avançar 1 casa porque pode ser perigoso avançar 2
        move_front() #move-se para a frente

    #se o bloco encontrado esta a mais de 2 blocos de distancia, ele avança 1 casa com cuidado
    elif (back_object >= 2):
        print("!! moving one block, because zombie might be nearby !!") #coloca na consola o texto para o utilizador saber que o robô está usando a função secure_movement
        ev3.speaker.say('BE CAREFUL') #o robô indica que irá avançar 1 casa porque pode ser perigoso avançar 2
        move_back() #move-se para trás
    
    #se o bloco encontrado esta a mais de 2 blocos de distancia, ele avança 1 casa com cuidado
    elif (left_object >= 2):
        print("!! moving one block, because zombie might be nearby !!") #coloca na consola o texto para o utilizador saber que o robô está usando a função secure_movement
        ev3.speaker.say('BE CAREFUL') #o robô indica que irá avançar 1 casa porque pode ser perigoso avançar 2
        move_left() #move-se para a esquerda

    #se o bloco encontrado esta a mais de 2 blocos de distancia, ele avança 1 casa com cuidado
    elif (right_object >= 2):
        print("!! moving one block, because zombie might be nearby !!") #coloca na consola o texto para o utilizador saber que o robô está usando a função secure_movement
        ev3.speaker.say('BE CAREFUL') #o robô indica que irá avançar 1 casa porque pode ser perigoso avançar 2
        move_right() #move-se para a direita

#funcao que realiza os reconhecimentos, dependendo da posicao do robot na matrix
def random_recon():
    #robot esta na coluna 0 nao pode fazer reconhecimento para a direita.
    if (robot_position[0] == 0):

        #robot esta na coluna 0 e linha 5, ou seja, nao pode fazer reconhecimento para a direita e para
        #atras, apenas para a frente e para a esquerda
        if(robot_position[1] == 0):
            wait(1500) #espera
            print('Recon Front:')
            recon_front() #faz reconhecimento para a frente
            robot.turn(-130) #vira -130º, para a esquerda
            wait(1500) #espera
            print('Recon Left:')
            recon_left() #faz reconhecimento para a esquerda
            wait(1500) #espera
            robot.turn(130) #vira 130º, para voltar a posicao inicial, ou seja, para a frente
            wait(1500) #espera

        #robot esta na coluna 0 e linha 5, ou seja, nao pode fazer reconhecimento para a direita e para
        #a frente, apenas para a esquerda e para atras
        if(robot_position[1] == 5):
            robot.turn(-130) #vira -130º, para a esquerda
            wait(1500) #espera
            print('Recon Left:')
            recon_left() #faz reconhecimento para a esquerda
            wait(1500) #espera
            robot.turn(-130) #vira -130º, para atras
            wait(1500) #espera
            print('Recon Back:')
            recon_back() #faz reconhecimento para atras
            wait(1500) #espera
            robot.turn(-260) #vira 260º, para voltar a posicao inicial, ou seja, para a frente
            wait(1500) #espera

        #robot esta na coluna 0 e linha 5, ou seja, nao pode fazer reconhecimento para a direita.
        if(robot_position[1] != 5 and robot_position[1] != 0):
            print('Recon Front:')
            recon_front() #faz reconhecimento para a frente
            wait(1500) #espera
            robot.turn(-130) #vira -130º, para a esquerda
            wait(1500) #espera
            print('Recon Left:')
            recon_left() #faz reconhecimento para a esquerda
            wait(1500) #espera
            robot.turn(-130) #vira -130º, para atras
            wait(1500) #espera
            print('Recon Back:')
            recon_back() #faz reconhecimento para atras
            wait(1500) #espera
            robot.turn(260) #vira 260º, para voltar a posicao inicial, ou seja, para a frente
            wait(1500) #espera    

    #robot esta na coluna 5, ou seja, nao pode fazer reconhecimento para a esquerda.
    if (robot_position[0] == 5):

        #robot esta na coluna 5 e na linha 0, entao nao pode fazer reconhecimento para a
        # esquerda e para atras, apenas para a frente e para a direita.
        if (robot_position[1] == 0):
            print('Recon Front:')
            recon_front() #faz reconhecimento para a frente
            wait(1500) #espera
            robot.turn(130) #vira 130º, para a direita
            wait(1500) #espera
            print('Recon Right:')
            recon_right() #faz reconhecimento para a direita
            wait(1500) #espera
            robot.turn(-130) #vira -130º, para voltar a posicao inicial, ou seja, para a frente
            wait(1500) #espera

        #robot esta na linha 5 e coluna 5, ou seja, so pode fazer reconhecimento para a direita e para atras
        if (robot_position[1] == 5):
            robot.turn(130) #vira 130º, para a direita
            wait(1500) #espera
            print('Recon Right:')
            recon_right() #faz reconhecimento para a direita
            wait(1500) #espera
            robot.turn(130) #vira 130º, para atras
            wait(1500) #espera
            print('Recon Back:')
            recon_back() #faz reconhecimento para atras
            wait(1500) #espera
            robot.turn(-260) #vira -260º, para voltar a posicao inicial, ou seja, para a frente
            wait(1500) #espera
            
        #robot esta na coluna 5, ou seja, nao pode fazer reconhecimento para a esquerda, apenas para
        # os outros lados
        if(robot_position[1] != 5 and robot_position[1] != 0):
            print('Recon Front:')
            recon_front() #faz reconhecimento para a frente
            wait(1500) #espera
            robot.turn(130) #vira 130º, para a direita
            wait(1500) #espera
            print('Recon Right:')
            recon_right() #faz reconhecimento para a direita
            wait(1500) #espera
            robot.turn(130) #vira 130º, para atras
            wait(1500) #espera
            print('Recon Back:') 
            recon_back() #faz reconhecimento para atras
            wait(1500) #espera
            robot.turn(-260) #vira 260º, para voltar a posicao inicial, ou seja, para a frente
            wait(1500) #espera

    #o robot esta na linha 0, ou seja nao pode fazer o reconhecimento para atras, apenas para a frente,
    #para a direita e para a esquerda
    if (robot_position[1] == 0 and robot_position[0] != 0 and robot_position[0] != 5):
        print('Recon Front:')
        recon_front() #faz reconhecimento para a frente
        wait(1500) #espera
        robot.turn(130) #vira 130º, para a direita
        wait(1500) #espera
        print('Recon Right:')
        recon_right() #faz reconhecimento para a direita
        wait(1500) #espera
        robot.turn(-260) #vira 260º, para a esquerda
        wait(1500) #espera
        print('Recon Left:')
        recon_left() #faz reconhecimento para a esquerda
        wait(1500) #espera
        robot.turn(130) #vira 130º, para voltar a posicao inicial, ou seja, para a frente
        wait(1500) #espera
        
    #o robot esta na linha 5, ou seja nao pode fazer o reconhecimento para a frente, apenas para atras,
    #para a direita e para a esquerda
    if (robot_position[1] == 5 and robot_position[0] != 0 and robot_position[0] != 5):
        robot.turn(130) #vira 130º, para a direita
        wait(1500) #espera
        print('Recon Right:')
        recon_right() #faz reconhecimento para a direita
        wait(1500) #espera
        robot.turn(130) #vira 130º, para atras
        wait(1500) #espera
        print('Recon Back:')
        recon_back() #faz reconhecimento para atras
        wait(1500) #espera
        robot.turn(130) #vira 130º, para a esquerda
        wait(1500) #espera
        print('Recon Left:')
        recon_left() #faz reconhecimento para a esquerda
        wait(1500) #espera
        robot.turn(130) #vira 130º, para voltar a posicao inicial, ou seja, para a frente
        wait(1500) #espera
        
    #o robot nao esta nas bordas da matrix, ou seja, pode fazer reconhecimento para todos os lados.
    if (robot_position[1] != 5 and robot_position[1] != 0 and robot_position[0] != 0 and robot_position[0] != 5):
        print('Recon Front:')
        recon_front() #faz reconhecimento para a frente
        wait(1500) #espera
        robot.turn(130) #vira 130º, para a direita
        wait(1500) #espera
        print('Recon Right:')
        recon_right() #faz reconhecimento para a direita
        wait(1500) #espera
        robot.turn(130) #vira 130º, para atras
        wait(1500) #espera
        print('Recon Back:')
        recon_back() #faz reconhecimento para atras
        wait(1500) #espera
        robot.turn(130) #vira 130º, para a esquerda
        wait(1500) #espera
        print('Recon Left:')
        recon_left() #faz reconhecimento para a esquerda
        wait(1500) #espera
        robot.turn(130) #vira 130º, para voltar a posicao inicial, ou seja, para a frente
        wait(1500) #espera


#funcao de movimento de 1 casa para a frente
def move_front():
    global robot_position
    robot.straight(DRIVE_DISTANCE) #o robot anda em linha reta 200mm para a frente
    robot_position[1] = robot_position[1] + 1  #atualiza a robot_position[1]


#funcao de movimento de 1 casa para atras
def move_back():
    global robot_position
    robot.straight(-DRIVE_DISTANCE) #o robot anda em linha reta 200mm para atras
    robot_position[1] = robot_position[1] - 1 #atualiza a robot_position[1]


#funcao de movimento de 1 casa para a esquerda
def move_left():
    global robot_position
    robot.turn(-128) #vira -128º, para a esquerda
    robot.straight(DRIVE_DISTANCE) #o robot anda em linha reta 200mm para a frente
    robot.turn(135) #vira 135º, para a posicao inicial, para a frente
    robot_position[0] = robot_position[0] + 1 #atualiza a robot_position[0]


#funcao de movimento de 1 casa para a direita
def move_right():
    global robot_position
    robot.turn(128) #vira 128º, para a direita
    robot.straight(DRIVE_DISTANCE) #o robot anda em linha reta 200mm para a frente
    robot.turn(-135) #vira -135º, para a posicao inicial, para a frente
    robot_position[0] = robot_position[0] - 1 #atualiza a robot_position[0]


#funcao de movimento de 2 casas
def move_double(destino):

    #se o destino for double, entao o movimento de 2 casas vai ser escolhido de forma
    #random no array POSSIBLE_DOUBLE
    double = destino 
    if double == 'random':
        double = choice(POSSIBLE_DOUBLE)

    global run_front,run_back ,run_left ,run_right

    #se a variavel 'double' escolher um tipo de movimento duplo, entao estes sao os casos:
    if (double == 'FRONT-FRONT' and run_front == 0):
        if robot_position[1] < 4: #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_front() #move-se para a frente
            move_front() #move-se para a frente
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'FRONT-RIGHT' and run_front == 0):
        if (robot_position[1] < 5 and robot_position[0] > 0 ): #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_front() #move-se para a frente
            move_right() #move-se para a direita
        else:
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'FRONT-LEFT' and run_front == 0):
        if (robot_position[1] < 5 and robot_position[0] < 5) : #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_front() #move-se para a frente
            move_left() #move-se para a esquerda
        else:
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'BACK-BACK' and run_back == 0):
        if robot_position[1] > 1: #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_back() #move-se para trás
            move_back() #move-se para trás
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'BACK-RIGHT' and run_back == 0):
        if (robot_position[1] > 0 and robot_position[0] > 0 ): #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_back() #move-se para trás
            move_right() #move-se para a direita
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'BACK-LEFT' and run_back == 0):
        if (robot_position[1] > 0 and robot_position[0] < 5): #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_back() #move-se para trás
            move_left() #move-se para a esquerda
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'LEFT-LEFT' and run_left == 0):
        if robot_position[0] < 4: #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_left() #move-se para a esquerda
            move_left() #move-se para a esquerda
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'LEFT-FRONT' and run_left == 0):
        if (robot_position[1] < 5 and robot_position[0] < 5) : #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_left() #move-se para a esquerda
            move_front() #move-se para a frente
        else : 
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'LEFT-BACK' and run_left == 0):
        if (robot_position[1] > 0 and robot_position[0] < 5): #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_left() #move-se para a esquerda
            move_back() #move-se para trás
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'RIGHT-RIGHT' and run_right == 0):
        if robot_position[0] > 1: #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_right() #move-se para a direita
            move_right() #move-se para a direita
        else :
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'RIGHT-FRONT' and run_right == 0):
        if (robot_position[1] < 5 and robot_position[0] > 0 ): #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_right() #move-se para a direita
            move_front() #move-se para a frente
        else: 
            return move_double('random') #move-se de forma random, 2 casas
    elif (double == 'RIGHT-BACK' and run_right == 0):
        if (robot_position[1] > 0 and robot_position[0] > +0 ): #verifica a posicao do robot na matriz, para que nao se mova para fora dela
            move_right() #move-se para a direita
            move_back() #move-se para trás
        else:
            return move_double('random') #move-se de forma random, 2 casas

#funcao que determina para onde o robot deve-se movimentar para chegar ao objetivo mais rapido.
def moveTowardsGoal(atual,objetivo):
    move = [0,0] #inicializacao da posicao para a qual o robo se ira mover
    teste = A_starStep(atual,objetivo) #utiliza o algoritmo A* para calcular o melhor trajeto para o objetivo
    move[0] = teste[0] - atual[0] #subtrai a coordenada x destino da coordenada atual de modo a obter o tipo de movimento que devera executar
    move[1] = teste[1] - atual[1] #subtrai a coordenada y destino da coordenada atual de modo a obter o tipo de movimento que devera executar
    print('Star: ' + str(teste))
    print('TESTE: ' + str(move))

    if (move[0] ==0  and move[1] == 0):
        move_double('LEFT-FRONT') #move-se para a esquerda e para a frente
    elif(move[0] == 1 and move[1] == 0):
        move_left() #move-se para a esquerda
    elif(move[0] == 0 and move[1] == 1):
        move_front() #move-se para a frente
    elif(move[0] == 1 and move[1] == 1):
        move_double('LEFT-FRONT') #move-se para a esquerda e para a frente
    elif(move[0] == 2 and move[1] == 0):
        move_double('LEFT-LEFT') #move-se para a esquerda e para a esquerda denovo
        
    elif(move[0] == 0 and move[1] == 2):
        move_double('FRONT-FRONT') #move-se para a frente e para a frente denovo
    elif(move[0] == -1 and move[1] == 0): 
        move_right() #move-se para a direita
    elif(move[0] == 0 and move[1] == -1):
        move_back() #move-se para trás
    elif(move[0] == -1 and move[1] == -1):
        move_double('RIGHT-BACK')  #move-se para a direita e para trás
    elif(move[0] == -2 and move[1] == 0):
        move_double('RIGHT-RIGHT') #move-se para a direita e para a direita denovo
    elif(move[0] == 0 and move[1] == -2):
        move_double('BACK-BACK') #move-se para trás e para trás denovo


# Ele diz uma mensagem para nos sabermos que ja podemos clicar no ombro do robot
ev3.speaker.set_volume(100)
ev3.speaker.say("Ready")

while(True):

    #quando o robot apanha uma peca da moto, comeca a dar um alarme
    if (parts_counter != 0):
        ev3.speaker.play_file(SoundFile.CHEERING)

    #se tiver duas cores na mesma casa    
    if left_shoulder.pressed(): #se o ombro esquerdo for pressionado
        detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
        detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota

    #esta variavel serve para verificar quantas partes o robot ja apanhou
    if(parts_counter == 1):
        if(robot_position[0] == 5 and robot_position[1] == 5):
            parts_moto = parts_moto + 1
            parts_counter = parts_counter - 1
            ev3.speaker.say('Added motor part in the motorcycle')
            goal = [0,0]
            print('Chegou a moto. Colocou peça')

    #se o valor da variavel 'parts_moto' é igual a 2, quer dizer que o robot já apanhou todas as pecas
    # necessarias para ganhar o jogo
    if(parts_moto == 2): 
        if(robot_position[0] == 5 and robot_position[1] == 5):
             ev3.speaker.say('I  WON  THE  GAME')

    #se clicarmos no botao no ombro direito o robot começa a sua jogada
    if right_shoulder.pressed():
        plays_counter = plays_counter + 1       #incrementa o numero de jogadas feitas
        print('--------------------------------------')
        print('Starting play - Right Shoulder pressed') 
        if(robot_position[1] == 5 and robot_position[0] == 5): #se o robot está na posicao [5,5] significa que chegou à mota
            if(parts_counter == 2): #se o numero de peças encontradas for 2, o jogo acaba porque a moto já esta arranjada
                ev3.speaker.say('Motorcycle fixed')

        random_recon() #faz o reconhecimento aos seus eixos, dependo da posicao do robot na matriz
        detect_bullet() #verifica a cor, se a cor detetada for amarela, significa que apanhou uma bala
        detect_motorcycle_part() #verifica a cor, se a cor detetada for verde, significa que apanhou uma peca da mota
        move(front_object,right_object,back_object,left_object) #chama a funcao move() com as variaveis dos lados

        update_robot_position(robot_position[1],robot_position[0])  #atualiza a posicao do robot na matriz
        #estes prints colocam na consola a matriz atualizada com os objetos detetados e a posição do robô
        print('r:' + str(right_object) + ' l:' + str(left_object) + ' f:' + str(front_object) + ' b:' + str(back_object))
        print(str(map[0]) + "\n" + str(map[1]) + "\n" + str(map[2]) + "\n" + str(map[3]) + "\n" + str(map[4])+"\n" +str(map[4]) +"\n" )
        print('My position is: ' + str(robot_position[0]) + ', ' + str(robot_position[1]))
        print('My goal is:' + str(goal))
        print('Plays made: ' + str(plays_counter))

        reset_robot_position(robot_position[1],robot_position[0]) #reseta a posicao do robot na matrix
