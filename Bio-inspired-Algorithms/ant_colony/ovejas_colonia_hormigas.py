#!/usr/bin/python

"""
    Made by:
        - Camilo Laiton
        
        University of Magdalena, Colombia
        2019-2
        Artificial Intelligence
        Topic: Ant Colony
        GitHub: https://github.com/kmilo9713/
"""

from oveja import oveja
import random
import sys, math, argparse
from time import time

class ACO():
    def __init__(self, peso, matriz_inicial, hormigas=4000):
        self.n_hormigas = hormigas
        self.peso = peso
        self.matriz_inicial = matriz_inicial
        self.matriz_pesos = []
        self.matriz_valores_pesos = []
        self.delta_feromona = args["dFero"]

    def calcular_pesos_o_valores_matriz(self, tamanio, peso, valor):

        pesos_valores_matriz=[0]

        for i in range(len(tamanio)):

            if(peso == 1):
                pesos_valores_matriz.append(tamanio[i][1])
            else:
                pesos_valores_matriz.append((tamanio[i][1])/(tamanio[i][2]))

        matriz_pesadas_valores = [[0 for i in range(len(tamanio)+1)] for j in range (len(tamanio)+1)]

        for i in range(len(tamanio)+1):
            for j in range(len(matriz_pesadas_valores)):
                matriz_pesadas_valores[i][j]=pesos_valores_matriz[j]
                     
        for i in range(len(matriz_pesadas_valores)):
            for j in range(len(matriz_pesadas_valores)):
                if(j==i):
                    
                    matriz_pesadas_valores[i][j] = 0
            
        return matriz_pesadas_valores

    def elegir_nodo_siguiente(self, values, feromones, visitated, solutions):
        
        valores_listados  = []
        availables = []
        actual      = solutions[-1]
    
        alfa = args["alpha"]
        beta = args["beta"]
    
        for i in range(len(values)):
            if i not in visitated: 
                fer  = math.pow((1.0 + feromones[actual][i]), alfa)
                peso = math.pow(1.0/values[actual][i], beta) * fer
                availables.append(i)
                valores_listados.append(peso)

        valor = random.random() * sum(valores_listados)
        acu = 0.0
        iterator = -1

        while valor > acu:
            iterator += 1
            acu += valores_listados[iterator]
    
        return availables[iterator]
    
    def hormigas(self, matriz, matrizPesos, iteraciones, pesoMochila):
        
        n = len(matriz)
        feromonas = [[0 for i in range(n)] for j in range(n)]
    
        mejorCamino     = []
        longMejorCamino = sys.maxsize
    
        hormiga = 1
        for iter in range(iteraciones):
            controlHormiga = hormiga % 100
            if controlHormiga == 000:
                pass
                # print ("Hormigas: ", hormiga)
                
            hormiga = hormiga + 1
            (camino,longCamino) = self.eligeCamino(matriz, matrizPesos, feromonas, pesoMochila)

            if longCamino <= longMejorCamino:
                mejorCamino     = camino
                longMejorCamino = longCamino

            dosis = (pesoMochila/longCamino)
            self.rastroFeromonas(feromonas, camino, dosis)
            
            self.evaporaFeromonas(feromonas)
            
            
        peso = 0
        for x in range(len(mejorCamino)):
                peso = peso + matrizPesos[0][mejorCamino[x]]
        return (mejorCamino, longMejorCamino, peso)

    def eligeCamino(self, matriz, matrizPesos, feromonas, pesoMochila):
        
        camino     = [0]
        visitados  = [0]
        longCamino = 0
    
        while len(visitados) < len(matriz):
            nodo      = self.elegir_nodo_siguiente(matriz, feromonas, visitados, camino)
                    
            camino.append(nodo)
        
            valorActual = 0
            for x in range(len(camino)):
                
                    if x != 0:
                        valorActual = valorActual + self.matriz_inicial[camino[x]-1][2]
        
            pesoActual = 0
            for x in range(len(camino)):
                    pesoActual = pesoActual + matrizPesos[0][camino[x]]
                    
        
            if (pesoActual > self.peso):
                camino.remove(nodo)
            
            else:
                longCamino = pesoActual / valorActual
            
            visitados.append(nodo)
    
    
        return (camino, longCamino)

    def rastroFeromonas(self, feromonas, camino, dosis):
        for i in range (len(camino) - 1):
            feromonas[camino[i]][camino[i+1]] += dosis
    
    def evaporaFeromonas(self, feromonas):    
        for lista in feromonas:
                for i in range(len(lista)):
                    lista[i] *= self.delta_feromona

    def implementacion(self):
        self.matriz_pesos = self.calcular_pesos_o_valores_matriz(self.matriz_inicial, 1, 0)
        self.matriz_valores_pesos = self.calcular_pesos_o_valores_matriz(self.matriz_inicial, 0, 1)

        (camino, longCamino, peso) = self.hormigas(self.matriz_valores_pesos, self.matriz_pesos, self.n_hormigas, self.peso)
        camino.remove(0)

        print("Peso Maximo: ", self.peso)
        print("Ovejas utiizadas ", camino)
        print("Peso Total: ", peso)
        valorTotal = 0
        for x in range(len(camino)):
                    valorTotal = valorTotal + self.matriz_inicial[camino[x]-1][2]
        print("Valor Maximo: ", valorTotal)
        print("Numero de hormigas: ", self.n_hormigas)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-v", "--verb", default=0, help="Mostrar mas información", type=int)
    ap.add_argument("-d", "--doc", default="../sheep_list_range1_500_arc5a.txt", help="Nombre archivo de texto")
    ap.add_argument("-p", "--peso", default="20", help="Peso para el limite", type=float)
    ap.add_argument("-a", "--alpha", default=1.0, help="Cantidad de alpha", type=float)
    ap.add_argument("-b", "--beta", default=0.5, help="Cantidad de beta", type=float)
    ap.add_argument("-dF", "--dFero", default=0.9, help="Delta de feromona", type=float)

    args = vars(ap.parse_args())

    oveja.generar_ovejas(10000, args["doc"])
    ovejas_disponibles = oveja.obtener_ovejas(args["doc"])

    matriz_inicial = [[int(oveja_1.n_oveja), float(oveja_1.peso), float(oveja_1.valor)] for oveja_1 in ovejas_disponibles]
    
    hormigas = 300

    aco_1 = ACO(args["peso"], matriz_inicial, hormigas)
    tiempo_inicio = time()
    aco_1.implementacion()
    tiempo_total = time() - tiempo_inicio

    print("Tiempo de ejecución: ", tiempo_total)

    """
    ovejas_disponibles_2 = [
        oveja(0, 10, 100),
        oveja(1, 8, 95),
        oveja(2, 9, 80),
        oveja(3, 10, 80),
        oveja(4, 9, 70),
        oveja(5, 8, 90),
    ]
    """