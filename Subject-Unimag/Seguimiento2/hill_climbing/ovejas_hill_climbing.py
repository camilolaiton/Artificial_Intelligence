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
from oveja import oveja
from time import time

def mostrar_equipaje(equipaje):
    
    valor_total = 0
    peso_total = 0
    
    print("N°oveja    Peso    Valor")
    for oveja in equipaje:
        print(oveja.n_oveja, "         ", oveja.peso, "     ", oveja.valor)
        peso_total += oveja.peso
        valor_total += oveja.valor
        
    print("Peso total: ", peso_total)
    print("Valor total: ", valor_total)

def mostrar_equipaje_interno(estados):

    externo = []
    interno = []

    for estado in estados:
        interno = []
        for oveja in estado:
            interno.append(oveja.n_oveja)
        externo.append(interno)

    return externo

def calcular_peso(ovejas):
    
    if type(ovejas).__name__ == "oveja":
        
        return ovejas.peso
        
    else:
        peso = float(0)

        for i in ovejas:
            peso += i.peso

        return peso

def calcular_valor(ovejas):

    if type(ovejas).__name__ == "oveja":
        
        return ovejas.valor
        
    else:
        valor = float(0)

        for i in ovejas:
            valor += i.valor

        return valor

class hill_climbing():

    def __init__(self, num_reinicios, estado_actual, capacidad, verbosity):
        self.__num_reinicios = num_reinicios    #Numero de reinicios del algoritmo
        self.__verbosity = verbosity    #Boolean para mostrar info
        self.__num_pasos = 0    #Para saber pasos que demoro
        self.__capacidad = capacidad
        self.__actual = estado_actual
        self.__soluciones = []
        self.__iteraciones_corridas = []    #Variable para conocer el numero de iteraciones hechas por un reinicio del algoritmo

    ######### NUEVA FUNCIONALIDAD ############
    @staticmethod
    def escoger_ovejas_inicial(lista_ovejas, peso_limite):  # Escoger ovejas iniciales teniendo en cuenta el peso
    
        escogidos = []
        peso = 0
        n_max_ovejas = random.randint(0, len(lista_ovejas)-1)  #random entre 0 y numero max ovejas para escoger X cantidad ovejas
        c = 0  # Contador para la cnatidad de veces sin cambiar el while -> Lo uso para salir del while si el espacio de ovejas no cambia durante X veces

        while(1):   #[NOTA: La variable C verla detenidamente o mirar si hay una estrategia mejor]
            
            if( len(escogidos) >= n_max_ovejas or c == 0.5*len(lista_ovejas)): #Si el tamaño de ovejas escogidas es igual al n_max salgo, o si c ya ha recorrido 50% del espacio de busqueda aleatoreamente se sale 
                break       #Se puede cambiar C para que recorra todo el espacio de busqueda para salirse

            oveja_escogida = lista_ovejas[random.randint(0, len(lista_ovejas)-1)]   #Escojo oveja al azar dentro de las ovejas
            c += 1  # Aumento la cantidad de veces pues se intento escoger una oveja

            if(oveja_escogida not in escogidos):    #Si la oveja escogida no se encuentra en la lista
                peso = calcular_peso(escogidos)  #Calculo el peso del estado inicial

                if(float(peso + oveja_escogida.peso) < peso_limite):   #Si el peso original mas la nueva posible oveja son menores al limite
                    escogidos.append(oveja_escogida)    #Agrego oveja
                    c = 0   # Si agrego entonces reinicio contador pues si se pudo agregar una oveja
                    
        return escogidos
    ######### -------------- ##################

    def implementacion(self):

        self.__soluciones = []

        for reinicio in range(0, self.__num_reinicios):
            print("Reinicio: ", reinicio)
            self.__num_pasos = 0
            self.logica()
            self.__soluciones.append(self.__actual)
            self.__actual = hill_climbing.escoger_ovejas_inicial(ovejas_disponibles, self.__capacidad)  #Reinicio con ovejas aleatoreo

        if(len(self.__soluciones) > 1):

            print("\nSoluciones encontradas: ")
            print(mostrar_equipaje_interno(self.__soluciones))

            print("\n\nEscogemos la mejor: ")
            solucion = self.escoger_mejor(self.__soluciones)
            print("TODAS ITERACIONES: ", self.__iteraciones_corridas)
            print("Numero de iteraciones: ", self.__iteraciones_corridas[self.__soluciones.index(solucion)] )
            mostrar_equipaje(solucion)
        else:

            print("Solucion encontrada: ")
            mostrar_equipaje_interno(self.__soluciones)

    def logica(self):

        while True:
            
            estados_objetivo = self.funcion_transicion_2(self.__actual)
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
                self.__iteraciones_corridas.append(self.__num_pasos)
                print("*************************")
                print("*************************")
                break

    def mostrar_info(self, solucion):
        #print("\nINFORMACION:")
        #print("Numero de reinicios:", self.__num_reinicios)
        #print("Numero de pasos: ", self.__num_pasos)
        #print("Estado actual: ")
        #mostrar_equipaje(self.__actual)

        if(solucion):
            print("Solucion encontrada")
        else:
            pass
            #print("Solucion NO encontrada")

    def funcion_transicion_2(self, origen):

        estados_objetivo = []
        peso_origen = calcular_peso(origen)

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

                if(calcular_peso(estado_generado_2) <= float(self.__capacidad)):
                    estados_objetivo.append(estado_generado_2) 

        return estados_objetivo                   
    
    def eliminar_peores(self, estados_objetivo):
        
        mejores = []
        valor_actual = calcular_valor(self.__actual)

        if(self.__verbosity):
            print("VALOR ACTUAL ENCONTRADO: ", valor_actual)
            print("Estados: ")
            mostrar_equipaje(self.__actual)

        for estado_objetivo in estados_objetivo:    #Recorro la lista de estados objetivo

            valor_objetivo = calcular_valor(estado_objetivo)

            if(valor_objetivo > valor_actual):    #Si el estado objetivo tiene menor valor, lo sacamos
                mejores.append(estado_objetivo)

        return mejores

    def escoger_mejor(self, estados_objetivo):
        
        mejor = self.__actual

        for estado_objetivo in estados_objetivo:    #Recorremos la lista de estados objetivo
            
            valor_mejor = calcular_valor(mejor)
            valor_objetivo = calcular_valor(estado_objetivo)  #Calculamos el valor de un estado

            if(valor_objetivo > valor_mejor):    #Si el valor objetivo es mayor, cambiamos la configuracion
                mejor = estado_objetivo

        return mejor    #Lo puedo hacer directamente al camion pero lo hago así para mantener fragmentado el codigo

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-n", "--runs", default=10, help="Cantidad de reinicios del algoritmo", type=int)
    ap.add_argument("-v", "--verb", default=0, help="Mostrar mas información", type=int)
    ap.add_argument("-d", "--doc", default="../sheep_list_range1_500_arc5a.txt", help="Nombre archivo de texto")
    ap.add_argument("-p", "--peso", default="100", help="Peso para el limite", type=float)

    args = vars(ap.parse_args())

    oveja.generar_ovejas(10000, args["doc"])
    ovejas_disponibles = oveja.obtener_ovejas(args["doc"])

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
    
    ovejas_iniciales = hill_climbing.escoger_ovejas_inicial(ovejas_disponibles, args["peso"])
    #print(ovejas_iniciales)
    #print("OVEJAS_INICIALES")
    #mostrar_equipaje(ovejas_iniciales)
    #print("Peso MAX: ", args["peso"])
    

    hill1 = hill_climbing(args["runs"], [ovejas_disponibles[0]], args["peso"], args["verb"])

    tiempo_inicio = time()
    hill1.implementacion()
    tiempo_total = time() - tiempo_inicio

    print("Tiempo de ejecución: ", tiempo_total)
    #ovejas_disponibles[random.randint(0, len(ovejas_disponibles)-1)]
    #
