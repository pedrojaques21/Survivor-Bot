#!/usr/bin/env pybricks-micropython
#from main import *

def CalculaHeuristica(atual,goal):
    distancia = abs(atual[0] - goal[0]) + abs(atual[1] - goal[1])
    return distancia

def A_starStep(atual,goal):
    heuristicaAtual = CalculaHeuristica(atual,goal)
    apontador = [0,0]
    apontadorAux = [0,0]
    if(atual[1] <= goal[1]):#Quer dizer que o objetivo está para cima
        if(atual[1] == goal[1]):
            for j in range(0,4):
                if(j == 0):
                    apontadorAux[0] = atual[0] + 1
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 1
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 1')
                            heuristicaAtual = aux
                elif(j == 1):
                    apontadorAux[0] = atual[0] + 2
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 2
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 2')
                            heuristicaAtual = aux
                elif(j==2):
                    apontadorAux[0] = atual[0] - 1
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 1
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 3')
                            heuristicaAtual = aux
                elif(j==3):
                    apontadorAux[0] = atual[0] - 2
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 2
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 4')
                            heuristicaAtual = aux
        elif (atual[0] == goal[0]):
            for j in range(0,2):
                if(j == 0):
                    
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] + 1
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        print('Entrei 1')
                        heuristicaAtual = aux
                elif(j == 1):
                    if(apontador[1] < goal[1]):
                        apontador[0] = atual[0] 
                        apontador[1] = atual[1] + 2
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux ):
                            print('Entrei 2')
                            heuristicaAtual = aux
        else:
            for i in range(0,5):
                if(i == 0):
                    apontador[0] = atual[0] + 1
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i == 1):
                    apontador[0] = atual[0] + 2
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==2):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] + 1
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==3):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] + 2
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==4):
                    apontador[0] = atual[0] + 1
                    apontador[1] = atual[1] + 1
                    aux = CalculaHeuristica(apontador,goal)
                    print('AUX POSITIVA: '+ str(aux))
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux

    elif(atual[1]>goal[1]):
        if(atual[1] == goal[1]):
            for j in range(0,4):
                if(j == 0):
                    apontadorAux[0] = atual[0] + 1
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 1
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 1')
                            heuristicaAtual = aux
                elif(j == 1):
                    apontadorAux[0] = atual[0] + 2
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] <= goal[0]):
                        apontador[0] = atual[0] + 2
                        apontador[1] = atual[1]
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 2')
                            heuristicaAtual = aux
                elif(j==2):
                    apontadorAux[0] = atual[0] - 1
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 1
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 3')
                            heuristicaAtual = aux
                elif(j==3):
                    apontadorAux[0] = atual[0] - 2
                    apontadorAux[1] = atual[1]
                    if(apontadorAux[0] >= goal[0]):
                        apontador[0] = atual[0] - 2
                        apontador[1] = atual[1] 
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 4')
                            heuristicaAtual = aux
        elif (atual[0] == goal[0]):
            for j in range(0,2): 
                if(j==0):
                    
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] - 1
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        print('Entrei 3')
                        heuristicaAtual = aux
                elif(j==1):
                    if(apontador[1] > goal[1]):
                        apontador[0] = atual[0] 
                        apontador[1] = atual[1] - 2
                        aux = CalculaHeuristica(apontador,goal)
                        if(heuristicaAtual > aux):
                            print('Entrei 4')
                            heuristicaAtual = aux
        else:                
            for i in range(0,5):
                if(i == 0):
                    apontador[0] = atual[0] - 1
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i == 1):
                    apontador[0] = atual[0] - 2
                    apontador[1] = atual[1]
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==2):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] - 1
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==3):
                    apontador[0] = atual[0] 
                    apontador[1] = atual[1] - 2
                    aux = CalculaHeuristica(apontador,goal)
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
                elif(i==4):
                    apontador[0] = atual[0] - 1
                    apontador[1] = atual[1] - 1
                    aux = CalculaHeuristica(apontador,goal)
                    print('AUX NEGATIVA' + str(aux))
                    if(heuristicaAtual > aux):
                        heuristicaAtual = aux
    return apontador
        
