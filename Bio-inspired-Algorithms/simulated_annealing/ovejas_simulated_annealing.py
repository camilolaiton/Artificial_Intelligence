#!/usr/bin/python

"""
    Made by:
        - Camilo Laiton

        University of Magdalena, Colombia
        2019-2
        Artificial Intelligence
        Topic: Local searchs
        
"""

import argparse, random
import math
from oveja import oveja
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

class simulated_annealing():
    
    def __init__(self, num_reinicios, estado_actual, capacidad, verbosity, temperatura, delta_temperatura):
        self.__num_reinicios = num_reinicios    #Numero de reinicios del algoritmo
        self.__verbosity = verbosity    #Boolean para mostrar info
        self.__num_pasos = 0    #Para saber pasos que demoro
        self.__capacidad = capacidad
        self.__actual = estado_actual
        self.__soluciones = []
        self.__temperatura = temperatura
        self.__delta_temperatura = delta_temperatura
        self.__mejor_sol = estado_actual
        self.__temp_sol = temperatura
        
    def __calcular_peso(self, ovejas):

        if ovejas:
            
            peso = 0

            for i in ovejas:
                peso += i.peso

            return peso
        
        return 0

    def __calcular_valor(self, ovejas):

        if ovejas:
            
            valor = 0

            for i in ovejas:
                valor += i.valor

            return valor
        
        return 0
    
    def logica(self):
        
        
        print("Temperatura inicial: ", self.__temperatura)

        cont = 0    #La variable contador utilizada aca solo indica el numero de ciclos general que realiza el algoritmo
                    # Más no indica la iteración en donde se encuentra la mejor solución brindada por el algoritmo
                    # Formula para la iteración de mejor solución ->  Iteracion = (Temp_Inicial - Temp_De_Mejor_Sol_Encontrada)/ Delta_Temp
        
        while self.__temperatura >= 1e-3:
            
            self.__num_pasos += 1
            estados_generados = self.funcion_transicion_2(self.__actual)
            #print(estados_generados)
            if(len(estados_generados) == 0):
                break

            generado = estados_generados[random.randint(0, len(estados_generados)-1)]

            funcion_costo = (self.__calcular_valor(self.__actual) - self.__calcular_valor(generado))

            try:
                exp = math.exp(-float(funcion_costo) / float(self.__temperatura))
            except OverflowError:
                exp = float('inf')

            if(funcion_costo < 0):
                self.__actual = generado

            elif random.uniform(0, 1) < exp:
                self.__actual = generado

            if(self.__calcular_valor(self.__mejor_sol) < self.__calcular_valor(self.__actual)):
                self.__mejor_sol = self.__actual
                self.__temp_sol = self.__temperatura

            self.__temperatura = self.__temperatura - self.__delta_temperatura

            if(self.__temperatura <= 1e-3):
                #print("\nMejor solucion encontrada con temperatura: ", self.__temperatura)
                pass
            else:
                #print("\nTemperatura actual: ", self.__temperatura)
                pass

            cont += 1   
        
        print()
        mostrar_equipaje(self.__mejor_sol)
        print("\nValor total: ", self.__calcular_valor(self.__mejor_sol))
        print("Peso total: ", self.__calcular_peso(self.__mejor_sol))
        print("Temperatura de mejor solución: ", self.__temp_sol)

        print("\nCantidad máxima iteraciones: ", self.__num_pasos)
        print("Iteración hasta la mejor solución: ", int( ( float(args["temp"]) - self.__temp_sol ) / self.__delta_temperatura ) )


    def funcion_transicion_2(self, origen):

        estados_objetivo = []
        peso_origen = self.__calcular_peso(origen)

        for i in ovejas_disponibles:
            
            estado_generado_1 = origen
            estado_generado_2 = origen

            if i not in estado_generado_1:
                peso_generado = peso_origen + i.peso

                if( peso_generado <= float(self.__capacidad) ):
                    estado_generado_1 = origen + [i]
                    estados_objetivo.append(estado_generado_1)

                if(len(origen) > 1):
                    
                    quitar = origen[random.randint(0, len(origen)-1)]
                    estado_generado_2 = list( set(origen) - set([quitar]))
                else:
                    estado_generado_2 = []

                estado_generado_2.append(i)

                if(self.__calcular_peso(estado_generado_2) <= float(self.__capacidad)):
                    estados_objetivo.append(estado_generado_2) 

        return estados_objetivo


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-t", "--temp", default=10, help="Cantidad inicial de temperatura del algoritmo", type=int)
    ap.add_argument("-v", "--verb", default=0, help="Mostrar mas información", type=int)
    ap.add_argument("-dt", "--delta", default=0.01, help="Cantidad de decremento", type=float)
    ap.add_argument("-d", "--doc", default="../sheep_list_range1_500_arc5a.txt", help="Nombre archivo de texto")
    ap.add_argument("-w", "--peso", default=100, help="Peso maximo", type=int)

    args = vars(ap.parse_args())

    oveja.generar_ovejas(10000, args["doc"])
    ovejas_disponibles = oveja.obtener_ovejas(args["doc"])

    """
    ovejas_disponibles = [
        oveja(0, 10, 100),
        oveja(1, 8, 95),
        oveja(2, 9, 80),
        oveja(3, 10, 80),
        oveja(4, 9, 70),
        oveja(5, 8, 90),
    ]
    """

    hill1 = simulated_annealing(0, [], float(args["peso"]), args["verb"], args["temp"] , args["delta"])
    
    tiempo_inicio = time()
    hill1.logica()
    tiempo_total = time() - tiempo_inicio

    print("Tiempo de ejecución: ", tiempo_total)

