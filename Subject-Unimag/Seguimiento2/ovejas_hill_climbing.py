#!/usr/bin/python

import argparse

class oveja:

    def __init__(self, numero, peso, valor):
        self.__n_oveja = numero
        self.__peso = peso
        self.__valor = valor

    @property
    def n_oveja(self):
        return self.__n_oveja

    @n_oveja.setter
    def n_oveja(self, n_oveja):
        self.__n_oveja = n_oveja

    @property
    def peso(self):
        'This function returns the sheeps\'s weight'
        return self.__peso

    @peso.setter
    def peso(self, peso):
        'This function sets the sheeps\'s weight'
        self.__peso = peso

    @property
    def valor(self):
        'This function returns the sheeps\'s value'
        return self.__valor

    @valor.setter
    def valor(self, valor):
        'This function sets the sheeps\'s value'
        self.__valor = valor

class camion():
    
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__equipaje = []
    
    @property
    def capacidad(self):
        'This function returns the truck\'s capacity'
        return self.__capacidad

    @capacidad.setter
    def peso(self, capacidad):
        'This function sets the truck\'s capacity'
        self.__capacidad = capacidad

    @property
    def equipaje(self):
        'This function returns the trucks\'s luggage'
        return self.__equipaje

    @equipaje.setter
    def equipaje(self, equipaje):
        'This function sets the truck\'s luggage'
        self.__equipaje = equipaje
    
    def mostrar_equipaje(self):

        print("N°oveja    Peso    Valor")
        for oveja in self.__equipaje:
            print(oveja.n_oveja, "         ", oveja.peso, "     ", oveja.valor)

class hill_climbing():

    def __init__(self, num_reinicios, estado_actual, verbosity):
        self.__num_reinicios = num_reinicios
        self.__estado_actual = estado_actual
        self.__verbosity = verbosity
        self.__num_pasos = 0

    def logica(self):
        
        # Estado actual en la variable self.__estado_actual 
        
        while True:
            
            estados_objetivo = self.__funcion_transicion()
            estados_objetivo = eliminar_peores(estados_objetivo, self.__estado_actual)
            
            if estados_objetivo:
                self.__estado_actual = self.escoger_mejor(estados_objetivo)
            else:
                break
        

    def mostrar_info(self):
        print("Numero de repeticiones:", self.__num_reinicios)
        print("Numero de pasos: ", self.__num_pasos)
        print("Estado actual: ", self.__estado_actual)

    def funcion_transicion(self):
        pass
    
    def eliminar_peores(self, estados_objetivo, actual):
        
        for i in estados_objetivo:
            
            if (estados_objetivo.valor < actual.valor):
                estados_objetivo.remove(i)
    
    def escoger_mejor(self, estados_objetivo):
        
        mejor = oveja(0, 0, 0)
        
        for i in estados_objetivo:
            
            if(mejor.valor < i.valor):
                mejor = i
                
        return mejor

    def funcion_evaluacion(self, estado_objetivo):
        
        suma_valor = 0
        
        for i in estado_objetivo:
            suma_valor += i.valor
            
        return suma_valor

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-n", "--numruns", default=1, help="Cantidad de reinicios del algoritmo", type=int)
    ap.add_argument("-v", "--verbosity", default=False, help="Mostrar mas información", type=bool)

    args = vars(ap.parse_args())
    
    ovejas_disponibles = {
        1 : oveja(1, 10, 100),
        2 : oveja(2, 8, 95),
        3 : oveja(3, 9, 80),
        4 : oveja(4, 10, 80),
        5 : oveja(5, 9, 70),
        6 : oveja(6, 8, 90),
    }
    
    camion1 = camion(20)
    camion1.equipaje = [ovejas_disponibles[6], ovejas_disponibles[2]]
    
    hill1 = hill_climbing(1, camion1.equipaje, True)
    
