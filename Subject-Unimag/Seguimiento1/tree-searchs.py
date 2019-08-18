#!/usr/bin/env python

"""
    Made by:
        - Camilo Laiton

        University of Magdalena, Colombia
        2019-2

        Artificial Intelligence

        Topic: Tree Searchs
        GitHub: https://github.com/kmilo9713/
"""

try:
    import Queue as queue
except ImportError:
    # Python 3
    import queue

class tree_searchs():

    def __init__(self, name, grafo):
        'Constructer of the class'
        self.__name = name
        self.__grafo = grafo
        self.__visitados = []   #Lista de visitados
        self.__pila = []    #Para recorrido en anchura
        self.__cola = []    #Para recorrido en profundidad

    @property
    def name(self):
        'This method returns the trees\'s name'
        return self.__name
    
    @name.setter
    def name(self, name):
        'This method changes the trees\'s name'
        self.__name = name
        
    @name.deleter
    def name(self):
        'This method resets the name for the tree'
        self.__name = None

    @property
    def grafo(self):
        'This method returns the trees\'s graph'
        return self.__grafo
    
    @grafo.setter
    def grafo(self, grafo):
        'This method changes the trees\'s graph'
        self.__grafo = grafo
    
    @grafo.deleter
    def grafo(self):
        'This method resets the trees\'s graph'
        self.__grafo = None
    
    def anchura(self, start, end=None):
        'This method makes a breadth search in the graph'

        print("+ [INFO] Busqueda en anchura -> COMIENZO")

        if end in self.__grafo:
            print("+ [INFO] Buscando objetivo ", end)
        elif end:
            print("+ [INFO] Objetivo no se encuentra en el grafo")

        if start not in self.__grafo:
            print("No existe ese nodo en el grafo!")
            return
        
        self.__visitados = []
        self.__cola = []

        #print("Ingreso origen a cola: ", start)
        self.__cola.insert(0, start)

        while len(self.__cola) != 0:    #podria tambien while self.__cola
            
            actual = self.__cola.pop()
            
            if actual not in self.__visitados:
                self.__visitados.extend(actual)

            if actual == end:
                print("+ [INFO] Objetivo encontrado")
                break;
            
            try:
                for key, _ in self.__grafo[actual]:
                    if key not in self.__visitados:
                        self.__cola.insert(0, key)
            
            except KeyError:
                print("+ [WARNING] Nodo ", actual, " no tiene nodos adyacentes")

        print("+ [INFO] Busqueda en anchura -> TERMINADO")
        print("+ [INFO] Resultado ANCHURA: ", self.__visitados, "\n")
    
    def profundidad(self, start, end=None):
        'This method makes a deep search in the graph'

        print("+ [INFO] Busqueda en profundidad -> COMIENZO")

        if end in self.__grafo:
            print("+ [INFO] Buscando objetivo ", end)
        elif end:
            print("+ [INFO] Objetivo no se encuentra en el grafo")

        if start not in self.__grafo:
            print("No existe ese nodo en el grafo!")
            return
        
        self.__visitados = []
        self.__pila = []

        #print("Ingreso origen a pila: ", start)
        self.__pila.append(start)

        while len(self.__pila) != 0:    #podria tambien while self.__pila
            
            actual = self.__pila.pop()

            #print("Saco nodo de pila: ", actual)
            #print("Pila: ", self.__pila)

            if actual not in self.__visitados:
                self.__visitados.extend(actual)
                #print("Agrego a lista de visitados: ", actual)
                #print("Lista de visitados: ", self.__visitados)

            if actual == end:
                print("+ [INFO] Objetivo encontrado")
                break;

            try:

                for key, _ in self.__grafo[actual]:
                    if key not in self.__visitados:
                        self.__pila.append(key)
                        #print("1. Ingreso en pila: ", key)
                        #print("2. Lista de visitados: ", self.__visitados)
                        #print("3. Pila: ", self.__pila)

            except KeyError:
                print("+ [WARNING] Nodo ", actual, " no tiene nodos adyacentes")

        print("+ [INFO] Busqueda en profundidad -> TERMINADO")
        print("+ [INFO] Resultado PROFUNDIDAD: ", self.__visitados, "\n")
    
    def anchura_costo_uniforme(self, start, end=None):
        'This method makes a breadth search with uniform cost in the graph'
        #REVISAR CON LA PROFESORA
        
        print("+ [INFO] Busqueda de costo uniforme -> COMIENZO")

        if end in self.__grafo:
            print("+ [INFO] Buscando objetivo ", end)
        elif end:
            print("+ [INFO] Objetivo no se encuentra en el grafo")

        if start not in self.__grafo:
            print("No existe ese nodo en el grafo!")
            return
        
        self.__visitados = []
        self.__cola = queue.PriorityQueue(len(self.__grafo))    #Creo cola de prioridad

        #print("Ingreso origen a cola: ", start)
        self.__cola.put((0, start))

        while self.__cola.qsize() != 0:    #podria tambien while self.__cola ó !self.__cola.Empty()
            
            #print("Cola: ", self.__cola.qsize())
            #print("Visitados: ", self.__visitados)

            actual = self.__cola.get()  #Sacamos el de menor costo
            #print("+ [INFO] Saco de la cola: ", actual)

            if actual[1] not in self.__visitados:
                self.__visitados.extend(actual[1])
                print("+ [INFO] Añado nodo a visitados: ", actual[1])

            if actual[1] == end:
                print("+ [INFO] Objetivo encontrado")
                break
            
            try:
                for key, value in self.__grafo[actual[1]]:
                    if key not in self.__visitados:
                        #print("+ [INFO] Añado nodo a cola: ", key)
                        self.__cola.put((value, key)) #Introducimos con la cola organizada descendentemente
            
            except KeyError:
                print("+ [WARNING] Nodo ", actual[1], " no tiene nodos adyacentes")

        print("+ [INFO] Busqueda de costo uniforme -> TERMINADO")
        print("+ [INFO] Resultado COSTO UNIFORME: ", self.__visitados, "\n")

    def __profundidad_iterativo(self):
        pass
    

graph1 = {
    "a":[("b", 1), ("c", 1), ("d", 1)], # Origen : destinos = (destino, peso_arista)
    "b":[("a", 1), ("e", 1)],
    "c":[("a", 1), ("g", 1)],
    "d":[("a", 1), ("h", 1)],
    "e":[("b", 1), ("i", 1)],
    "g":[("c", 1), ("j", 1)],
    "h":[("d", 1), ("k", 1)],
    "i":[("e", 1), ("f", 1)],
    "j":[("g", 1), ("k", 1)],
    "k":[("j", 1), ("h", 1)],
}

graph2 = {
    # Origen : destinos = (destino, peso_arista)
    "D":[("B", 1), ("C", 1)],
    "C":[("R", 1)],
    "R":[("H", 1)],
    "H":[("A", 1), ("T", 1), ("D", 1)],
    "B":[("H", 1)],
    "A":[],
    "T":[],
}

graph3 = {
    # Origen : destinos = (destino, peso_arista)
    "S":[("A", 1), ("B", 5), ("C", 15)],
    "A":[("G", 10), ("S", 1)],
    "G":[("C", 5), ("A", 10)],
    "C":[("S", 15), ("G", 5)],
    "B":[("G", 5), ("S", 5)],
}

graph4 = {
    # Origen : destinos = (destino, peso_arista)
    "S":[("A", 1), ("G", 12)],
    "A":[("B", 3), ("C", 1)],
    "G":[],
    "C":[("D", 1), ("G", 2)],
    "B":[("D", 3)],
    "D":[("G", 3)],
}

tree1 = tree_searchs("Arbol 1", graph2)
tree1.profundidad("D", "Z")
tree1.anchura("D", "Z")

tree1.grafo = graph4
tree1.anchura_costo_uniforme("S", "G")