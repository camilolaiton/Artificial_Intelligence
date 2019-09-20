#!/usr/bin/python

"""
    Made by:
        - Camilo Laiton
        University of Magdalena, Colombia
        2019-2
        Artificial Intelligence
        Topic: Local searchs
        GitHub: https://github.com/kmilo9713/
"""

import argparse, random

class oveja:

    def __init__(self, numero, peso, valor):
        self.__n_oveja = numero
        self.__peso = peso
        self.__valor = valor

    def __str__(self):
        print("Oveja: ", self.__n_oveja)

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

class hill_climbing():

    def __init__(self, num_reinicios, estado_actual, capacidad, verbosity):
        self.__num_reinicios = num_reinicios    #Numero de reinicios del algoritmo
        self.__verbosity = verbosity    #Boolean para mostrar info
        self.__num_pasos = 0    #Para saber pasos que demoro
        self.__capacidad = capacidad
        self.__inicial = estado_actual
        self.__actual = estado_actual
        self.__soluciones = []

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

    def implementacion(self):

        self.__soluciones = []

        for reinicio in range(0, self.__num_reinicios):
            print("Reinicio: ", reinicio)
            self.logica()
            self.__soluciones.append(self.__actual)
            self.__actual = self.__inicial

        print("\nSoluciones encontradas: ")
        print(mostrar_equipaje_interno(self.__soluciones))

        print("\n\nEscogemos la mejor: ")
        self.__actual = self.escoger_mejor(self.__soluciones)
        mostrar_equipaje(self.__actual)

    def logica(self):
        
        # Estado actual en la variable self.__camion.equipaje 
        
        print("Estado inicial: ")
        mostrar_equipaje(self.__actual)

        while True:
            
            estados_objetivo = self.funcion_transicion(self.__actual)
            estados_objetivo = self.eliminar_peores(estados_objetivo)
            self.__num_pasos += 1

            if ( len(estados_objetivo) != 0):
                self.__actual = self.escoger_mejor(estados_objetivo)  #Asigno el mejor al equipaje

                if(self.__verbosity):
                    print("Cambio estado actual a")
                    mostrar_equipaje(self.__actual)

                self.mostrar_info(False)

            else:
                print("\n\n*************************")
                print("*************************", end="")
                self.mostrar_info(True)
                print("*************************")
                print("*************************")
                break

    def mostrar_info(self, solucion):
        print("\nINFORMACION:")
        print("Numero de reinicios:", self.__num_reinicios)
        print("Numero de pasos: ", self.__num_pasos)
        print("Estado actual: ")
        mostrar_equipaje(self.__actual)

        if(solucion):
            print("Solucion encontrada")
        else:
            print("Solucion NO encontrada")

    def funcion_transicion(self, origen):

        estados_objetivo = []   #Vecindario de estado objetivo
        peso_origen = self.__calcular_peso(origen)
        
        for i in ovejas_disponibles:

            estado_generado = origen

            if i not in estado_generado:

                peso_generado = peso_origen + i.peso   #Peso generado

                if( peso_generado <= self.__capacidad):   #Calculo capacidad maxima, si se puede añadir
                    estado_generado = origen + [i]   #Añado a la oveja
                    estados_objetivo.append(estado_generado)    #Añado al vecindario
                    
                    estado_generado = origen

                    if(self.__verbosity):
                        #print("Capacidad camion: ", self.__camion.capacidad, " peso generado: ", peso_generado, " con oveja ", i.n_oveja)
                        print("Agrego oveja ", i.n_oveja, " Estados: ", mostrar_equipaje_interno(estados_objetivo), " NO REEMPLAZO")

                num_random = random.randint(0, len(origen)-1)   #Random entre ovejas

                quitar = estado_generado[num_random]

                estado_generado = list(set(estado_generado) - set([quitar]))        #estado_generado.remove(quitar)  #Quito la oveja aleatoreamente
                
                """
                Me toco hacer este gancho aca porque usando el remove se usaba la direccion de memoria de la otra variable
                entonces modificaba el valor original encapsulado en self.__actual y tambien el estado origen y generado
                """
                
                estado_generado.append(i)   #Agrego la oveja nueva

                if(self.__calcular_peso(estado_generado) <= self.__capacidad):     #Verifico la capacidad del camion
                    
                    estados_objetivo.append(estado_generado)    #Agrego al vecindario
                    
                    if(self.__verbosity):
                        
                        print("\nAgrego oveja ", i.n_oveja, " Estados: ", mostrar_equipaje_interno(estados_objetivo), " REEMPLAZO")
                        print("Estado original: ")
                        mostrar_equipaje(origen)

        if(self.__verbosity):
            print("\nEstados generados al finalizar transicion:")
            mostrar_equipaje_interno(estados_objetivo)

        return estados_objetivo
    
    def eliminar_peores(self, estados_objetivo):
        
        eliminar = []   #Lista usada para guardar elementos a eliminar
        valor_actual = self.__calcular_valor(self.__actual)

        if(self.__verbosity):
            print("VALOR ACTUAL ENCONTRADO: ", valor_actual)
            print("Estados: ")
            mostrar_equipaje(self.__actual)

        for estado_objetivo in estados_objetivo:    #Recorro la lista de estados objetivo

            valor_objetivo = self.__calcular_valor(estado_objetivo)

            if(valor_objetivo < valor_actual):    #Si el estado objetivo tiene menor valor, lo sacamos
                eliminar.append(estado_objetivo)

                if(self.__verbosity):
                    print("Elimino valor objetivo: ", valor_objetivo, " valor camion: ", valor_actual)

        for i in eliminar:
            estados_objetivo.remove(i)

        return estados_objetivo

    def escoger_mejor(self, estados_objetivo):
        
        mejor = self.__actual

        for estado_objetivo in estados_objetivo:    #Recorremos la lista de estados objetivo
            
            valor_actual = self.__calcular_valor(mejor)
            valor_objetivo = self.__calcular_valor(estado_objetivo)  #Calculamos el valor de un estado

            if(valor_objetivo > valor_actual):    #Si el valor objetivo es mayor, cambiamos la configuracion
                mejor = estado_objetivo

        return mejor    #Lo puedo hacer directamente al camion pero lo hago así para mantener fragmentado el codigo

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-n", "--runs", default=1, help="Cantidad de reinicios del algoritmo", type=int)
    ap.add_argument("-v", "--verb", default=0, help="Mostrar mas información", type=int)

    args = vars(ap.parse_args())

    ovejas_disponibles = [
        oveja(0, 10, 100),
        oveja(1, 8, 95),
        oveja(2, 9, 80),
        oveja(3, 10, 80),
        oveja(4, 9, 70),
        oveja(5, 8, 90),
    ]

    hill1 = hill_climbing(args["runs"], [ovejas_disponibles[5], ovejas_disponibles[4] ], 20, args["verb"])
    hill1.implementacion()