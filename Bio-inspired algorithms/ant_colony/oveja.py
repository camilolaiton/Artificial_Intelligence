#!/usr/bin/python

"""
    Made by:
        - Camilo Laiton
        
        University of Magdalena, Colombia
        2019-2
        Artificial Intelligence
        GitHub: https://github.com/kmilo9713/
"""

import os
import random

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

    @staticmethod
    def generar_ovejas(cant_ovejas, ruta):

        if(os.path.isfile(ruta)):
            print("Ya existe el archivo de texto")
        else:

            with open(ruta, "w") as archivo:

                for i in range(0, cant_ovejas):
                    archivo.writelines("%i %i %i\n" % (i, random.randint(2, 20), random.randint(60, 100)))

            print("El archivo de texto se ha creado")
                
    @staticmethod
    def obtener_ovejas(ruta):

        ovejas = []
        i = 0

        with open(ruta, "r") as archivo:

            for linea in archivo.readlines():
                if(i != 0):
                    lista = linea.replace("\n", "").split(" ")
                    ovejas.append(oveja( int(lista[0]), float(lista[1]), float(lista[2]) ))
                i += 1
        return ovejas

                
