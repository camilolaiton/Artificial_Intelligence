#!/usr/bin/python

"""
    Made by:
        - Camilo Laiton

        University of Magdalena, Colombia
        2019-2
        Artificial Intelligence
        Topic: Genetic Algorithm
        GitHub: https://github.com/kmilo9713/
"""

import argparse, random, collections
from oveja import oveja
import pylab as plt
import numpy as np
from time import time

def mostrar_equipaje(equipaje):

    print("N°oveja    Peso    Valor")
    for oveja in equipaje:
        print(oveja.n_oveja, "         ", oveja.peso, "     ", oveja.valor)

def mostrar_equipaje_interno(estados):

    externo = []
    interno = []

    for estado in estados:
        interno = []
        for oveja in estado:
            interno.append(oveja.n_oveja)
        externo.append(interno)

    return externo

class genetic_algorithm():

    def __init__(self, poblacion_size, gen_max, mutation, capacity, porcentaje_parada=0.90):
        self.__poblacion_size = poblacion_size
        self.__poblacion = []
        self.__gen_max = gen_max
        self.__mutation = mutation
        self.__capacity = capacity
        self.__porcentaje_parada = 0.90
        self.__convergencia_estadistica = []
    
    def mostrar_estadisticas(self):
        plt.figure()
        plt.title("Porcentaje convergencia / Generaciones")
        plt.xlabel("Generaciones")
        plt.ylabel("Porcentaje convergencia poblacion")
        plt.xticks(np.arange(0, self.__gen_max, 10))
        plt.yticks(np.arange(0, 100, 10))
        plt.plot(self.__convergencia_estadistica, marker='o', linestyle='--', color='r', label = "Convergencia")
        plt.show()

    def implementacion(self):
        
        self.__poblacion = self.crear_poblacion()
        
        generacion = 0

        while(self.criterios_parada(generacion)):

            #print("Generacion [%d]" % generacion)

            self.__poblacion = sorted(self.__poblacion, key=lambda x: self.fitness(x), reverse=True)

            for cromosoma in self.__poblacion:
                if(args["verb"]):
                    #print(cromosoma, " - Valor: ", self.fitness(cromosoma))
                    pass
            
            self.__poblacion = self.evolucionar_poblacion()

            generacion += 1
        
        print("Solucion encontrada en la generacion [%d]" % generacion)
        
        mejor, valor = self.obtener_maximo()
        print(mejor)
        self.mostrar_oveja(mejor)
    
    def mostrar_oveja(self, cromosoma):

        print("\nOvejas seleccionadas\n")
        peso_total = 0
        valor_total = 0

        for pos in range(0, len(cromosoma)):
            if(cromosoma[pos] == 1):
                print("Oveja: ", ovejas_disponibles[pos].n_oveja, " - Peso: ", ovejas_disponibles[pos].peso)
                peso_total += ovejas_disponibles[pos].peso
                valor_total += ovejas_disponibles[pos].valor
        
        print("Peso total: ", peso_total)
        print("Valor total: ", valor_total)

    def obtener_maximo(self):

        mayor = self.crear_cromosoma(True)
        valor_mayor = 0

        for cromosoma in self.__poblacion:

            valor_mayor = self.fitness(mayor)
            valor_cromosoma = self.fitness(cromosoma)

            if(valor_mayor < valor_cromosoma):
                mayor = cromosoma
                valor_mayor = valor_cromosoma
        
        return mayor, valor_mayor

    def criterios_parada(self, generacion):
        
        if(generacion >= self.__gen_max):
            return False

        cantidad_parada = (self.__poblacion_size)*(self.__porcentaje_parada)
        cromosoma_0 = self.crear_cromosoma(True)

        for cromosoma_1 in self.__poblacion:

            contador = 0

            for cromosoma_2 in self.__poblacion:
                
                if( (cromosoma_1 == cromosoma_2) and cromosoma_1 != cromosoma_0 ):
                    contador += 1

            contador -= 1

            if(contador == cantidad_parada):
                self.__convergencia_estadistica.append( (contador/self.__poblacion_size)*100 )
                return False
        
        self.__convergencia_estadistica.append( (contador/self.__poblacion_size)*100 )
        return True

    def evolucionar_poblacion(self):
        
        porcentaje_padres = 0.2
        loteria_padres = 0.05

        hijos = []
        espacio_padres = int(porcentaje_padres*self.__poblacion_size)
        padres = self.__poblacion[:espacio_padres]

        resto_pob = self.__poblacion[espacio_padres:]

        for resto in resto_pob:

            if(loteria_padres > random.random()):
                padres.append(resto)

        espacio_sobrante = self.__poblacion_size - len(padres)

        while(len(hijos) < espacio_sobrante):
            
            padre1 = padres[random.randint(0, len(padres)-1)]
            padre2 = padres[random.randint(0, len(padres)-1)]

            #Cruzamiento 1 punto

            mitad = int(len(padre1)/2)

            hijo = padre1[:mitad] + padre2[mitad:]

            if(random.random() < self.__mutation):
                self.mutacion(hijo)
            
            hijos.append(hijo)

        #Mutacion de los padres
        for padre in padres:
            
            if(random.random() < self.__mutation):
                self.mutacion(padre)

        padres.extend(hijos)

        return padres
        

    def crear_poblacion(self):
        return [self.crear_cromosoma(False) for cromosoma in range(0, self.__poblacion_size)]
        
    def crear_cromosoma(self, ceros):
        rango = len(ovejas_disponibles)
        if(ceros):
            return [0 for cromosoma in range(0, rango)]
        else:
            """
            return [random.randint(0,1) for cromosoma in range(0, rango)]
            """
            probabilidad_escogencia = 0.70
            peso_acu = 0

            cromosoma_resultante = []
            gen = 0

            for cromosoma in range(0, rango):
                gen = random.randint(0,1)

                if(gen == 1 and  random.random() <= probabilidad_escogencia ):
                    if(peso_acu + ovejas_disponibles[cromosoma].peso <= self.__capacity):
                        cromosoma_resultante.append(gen)
                        peso_acu += ovejas_disponibles[cromosoma].peso
                else:
                    cromosoma_resultante.append(0)

            return cromosoma_resultante
            

    def mutacion(self, cromosoma):

        rand = random.randint(0, len(cromosoma)-1)

        if(cromosoma[rand] == 0):
            cromosoma[rand] = 1
        else:
            cromosoma[rand] = 0

    def fitness(self, cromosoma):
        
        valor = 0
        peso = 0

        indice = 0

        for i in cromosoma:
            if(indice >= len(ovejas_disponibles)):
                break
            
            if(i == 1):
                valor += ovejas_disponibles[indice].valor
                peso += ovejas_disponibles[indice].peso
            
            indice += 1

        if(peso <= self.__capacity):
            return valor
        
        return 0

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    #ap.add_argument("-n", "--runs", default=1, help="Cantidad de reinicios del algoritmo", type=int)
    ap.add_argument("-v", "--verb", default=0, help="Mostrar mas información", type=int)
    ap.add_argument("-d", "--doc", default="../sheep_list_range1_500_arc5a.txt", help="Nombre archivo de texto")
    ap.add_argument("-g", "--gens", default=50, help="Numero de generaciones", type=int)
    ap.add_argument("-w", "--peso", default=20, help="Peso maximo", type=int)
    ap.add_argument("-p", "--pob", default=200, help="Tamaño poblacion", type=int)

    args = vars(ap.parse_args())

    oveja.generar_ovejas(20, args["doc"])
    ovejas_disponibles = oveja.obtener_ovejas(args["doc"])

    genetico = genetic_algorithm(args["pob"], args["gens"], 0.1, float(args["peso"])) #poblacion_size, gen_max, mutation, capacity, porcentaje_parada
    
    tiempo_inicio = time()
    genetico.implementacion()
    tiempo_total = time() - tiempo_inicio

    print("Tiempo de ejecución: ", tiempo_total)
    genetico.mostrar_estadisticas()

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