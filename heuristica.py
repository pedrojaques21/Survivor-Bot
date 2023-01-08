from main import *

def CalculaHeuristica(atual,goal):
    distancia = abs(atual[0] - goal[0]) + abs(atual[1] - goal[1])
    return distancia

def A_starStep(atual,goal):
    heuristicaAtual = CalculaHeuristica(atual,goal)
    apontador = [0,0]
    if(atual[0] < goal[0]):#Quer dizer que o objetivo está para cima
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
                if(heuristicaAtual > aux):
                    heuristicaAtual = aux

    elif(atual[0]>goal[0]):
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
                if(heuristicaAtual > aux):
                    heuristicaAtual = aux
    return apontador
        