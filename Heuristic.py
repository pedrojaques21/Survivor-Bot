#!/usr/bin/env pybricks-micropython
#from main import *

def CalculaHeuristica(atual,goal):
    distancia = abs(atual[0] - goal[0]) + abs(atual[1] - goal[1]) #Calculo de Manhattam, calcula o valor absoluto entre a posicao atual e o objetivo
    return distancia

def A_starStep(atual,goal):
    heuristicaAtual = CalculaHeuristica(atual,goal) #Heuristica da posicao atual para o objetivo
    apontador = [0,0] #possiveis posicoes que o robo pode descolar
    apontadorAux = [0,0] #apontador auxiliar para nao modificar o valor que será exportado
    if(atual[1] <= goal[1]):#Quer dizer que as coordenadas y do objetico sao maiores do que as atuais do robo, logo o robo nao necessita de se deslocar para tras
        if(atual[1] == goal[1]): #Se o robô se encontra nas mesma linha y que o objetivo, logo so necessita de se deslocar para a esquerda e para a direita
            for j in range(0,4): #verifica todos os casos possiveis
                if(j == 0):
                    apontadorAux[0] = atual[0] + 1 #heuristica da posicao uma casa para a esquerda do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 1
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux): # Verifica se a nova heuristica e menor que a atual
                            print('Entrei 1')
                            heuristicaAtual = aux
                elif(j == 1):
                    apontadorAux[0] = atual[0] + 2 #heuristica da posicao 2 casas para a esquerda do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 2
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                            print('Entrei 2')
                            heuristicaAtual = aux
                elif(j==2):
                    apontadorAux[0] = atual[0] - 1 #heuristica da posicao uma casa para a direita do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 1
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                            print('Entrei 3')
                            heuristicaAtual = aux
                elif(j==3):
                    apontadorAux[0] = atual[0] - 2 #heuristica da posicao 2 casas para a direita do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 2
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                            print('Entrei 4')
                            heuristicaAtual = aux
        elif (atual[0] == goal[0]):  #Se o robô se encontra nas mesma linha x que o objetivo, logo so necessita de se deslocar para a frente 
            for j in range(0,2):
                if(j == 0):
                    
                        apontador[0] = atual[0] 
                        apontador[1] = atual[1] + 1 #heuristica da posicao 1 casa para a frente do robo
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                            print('Entrei 1')
                            heuristicaAtual = aux
                elif(j == 1):
                    if(apontador[1] < goal[1]): #Verifica se nao estamos a apontar para fora do tabuleiro
                        apontador[0] = atual[0] 
                        apontador[1] = atual[1] + 2 #heuristica da posicao 2 casas para a frente do robo
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux ):# Verifica se a nova heuristica e menor que a atual
                            print('Entrei 2')
                            heuristicaAtual = aux
        else:
            for i in range(0,5):
                if(i == 0):
                    apontador[0] = atual[0] + 1 #heuristica da posicao 1 casa para a esquerda do robo
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                        heuristicaAtual = aux
                elif(i == 1):
                    apontador[0] = atual[0] + 2 #heuristica da posicao 2 casas para a esquerda do robo
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==2):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] + 1 #heuristica da posicao 1 casa para a frente do robo
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                        heuristicaAtual = aux
                elif(i==3):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] + 2 #heuristica da posicao 2 casas para a frente do robo
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                        heuristicaAtual = aux
                elif(i==4):
                    apontador[0] = atual[0] + 1 #heuristica da posicao 1 casa para a esquerda do robo
                    apontador[1] = atual[1] + 1 #heuristica da posicao 1 casa para a frente do robo
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):# Verifica se a nova heuristica e menor que a atual
                        heuristicaAtual = aux

    elif(atual[1]>goal[1]):#Quer dizer que as coordenadas y do objetico sao menores do que as atuais do robo, logo o robo nao necessita de se deslocar para frente
        if(atual[1] == goal[1]):#Se o robô se encontra nas mesma linha y que o objetivo, logo so necessita de se deslocar para a esquerda e para a direita
            for j in range(0,4):
                if(j == 0):
                    apontadorAux[0] = atual[0] + 1 #heuristica da posicao 1 casa para a esquerda do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 1
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 1')
                            heuristicaAtual = aux
                elif(j == 1):
                    apontadorAux[0] = atual[0] + 2 #heuristica da posicao 2 casas para a esquerda do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 2
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 2')
                            heuristicaAtual = aux
                elif(j==2):
                    apontadorAux[0] = atual[0] - 1 #heuristica da posicao 1 casa para a direita do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 1
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 3')
                            heuristicaAtual = aux
                elif(j==3):
                    apontadorAux[0] = atual[0] - 2 #heuristica da posicao 2 casas para a direita do robo
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 2
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 4')
                            heuristicaAtual = aux
        elif (atual[0] == goal[0]): #Se o robô se encontra nas mesma linha x que o objetivo, logo so necessita de se deslocar para a frente 
            for j in range(0,2): 
                if(j==0):
                    
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] - 1 #heuristica da posicao 1 casa para tras do robo
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        print('Entrei 3')
                        heuristicaAtual = aux
                elif(j==1):
                    if(apontador[1] > goal[1]):
                        apontador[0] = atual[0] 
                        apontador[1] = atual[1] - 2 #heuristica da posicao 2 casas para tras do robo
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 4')
                            heuristicaAtual = aux
        else:                
            for i in range(0,5):
                if(i == 0):
                    apontador[0] = atual[0] - 1 #heuristica da posicao 1 casa para direita do robo
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i == 1):
                    apontador[0] = atual[0] - 2 #heuristica da posicao 2 casas para direita do robo
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==2):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] - 1 #heuristica da posicao 1 casa para tras do robo
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==3):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] - 2 #heuristica da posicao 2 casas para tras do robo
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==4):
                    apontador[0] = atual[0] - 1 #heuristica da posicao 1 casa para direita do robo
                    apontador[1] = atual[1] - 1 #heuristica da posicao 1 casa para tras do robo
                    aux = CalculaHeuristica(apontador,goal)
                    print('AUX NEGATIVA' + str(aux))
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
    return apontador
        
