#!/usr/bin/env python

"""
    Made by:
        - Camilo Laiton

        University of Magdalena, Colombia
        2019-2

        Artificial Intelligence

        Topic: Tree Searchs
        GitHub: https://github.com/kmilo9713/

        Algorithms bfs and dfs taken from: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        # a sample graph
"""

try:
    import Queue as queue
except ImportError:
    # Python 3
    import queue

import math
from clase_matriz import matriz

#matriz1 = matriz(5,5, [ (1,1), (0,0), (3,3), (3,1), (1,4)] )
#matriz1.mostrar_matriz()

class tree_searchs():

    def __init__(self, name):
        'Constructer of the class'
        self.__name = name

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

    def bfs_paths(self, graph, start, goal):
        queue = [(start, [start])]
        while queue:
            #print("Cola antes: ", queue, "\n")
            (vertex, path) = queue.pop(0)
            #print("Vertex: ", vertex)
            #print("Cola despues: ", queue, "\n")

            #print("Camino: ", path)

            l = list(set(graph[vertex]) - set(path))    #Quedan nodos a los que puedo viajar

            for next in sorted(l):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))
    
    def dfs_paths(self, graph, start, goal):
        
        stack = [(start, [start])]

        while stack:
            (vertex, path) = stack.pop()
                
            l = list(set(graph[vertex]) - set(path))

            print(path)

            for next in sorted(l, reverse=True):
                            
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def __dfs_paths_b(self, graph, start, goal, depth_limit, outer_limit):    #Parte b primero en profundidad - madified by Camilo Laiton

        stack = [ (start, [start], 0) ] #Inico
        camino_niveles = [] #Array para guardar el recorrido por niveles cuando no se encuentra solucion

        while stack:
            (actual, camino, nivel_nodo) = stack.pop()

            if actual not in camino_niveles:
                camino_niveles.append(actual)   #Para guardar el recorrido por niveles [No es necesario para funcionamiento]
            #print("Saco de pila: ", actual, " llevo camino: ", camino, " nivel: ", nivel_nodo)
            
            l = None

            if nivel_nodo+1 <= depth_limit: #Para saber si necesito buscar en el otro nivel
                l = list( set(graph[actual]) - set(camino) )

            if l:
                for next in sorted(l, reverse=True):

                    if next == goal:
                        return (camino + [next], 1)

                    else:
                        if nivel_nodo+1 <= depth_limit:
                            #print("Entro hijos de ", actual, " nivel ", nivel_nodo+1)
                            stack.append((next, camino + [next], nivel_nodo+1)) #meto nodos del nivel y aumento el nivel en 1

        if depth_limit == outer_limit:  #salgo por limite general
            return (camino, -1)

        return (camino_niveles, 0)  #Retorno que no encontre solucion pero puedo seguir iterando

    def dfs_paths_limit(self, graph, start, goal, limite_general):  #Parte A primero en profundidad - modified by Camilo Laiton

    	depth_limit = 0

    	while(True):
            result = self.__dfs_paths_b(graph, start, goal, depth_limit, limite_general)

            print("\n[+] Cantidad iterada: ", depth_limit)

            if result[1] == -1: #Solution wasn't found
                print("La solucion no fue encontrada, nivel total: ", depth_limit)
                break
            
            elif result[1] == 1:
                print("Solucion encontrada en el nivel: ", depth_limit)
                print("Solucion: ", result[0])
                break
            
            else:
                print("Solucion no encontrada aún en nivel ", depth_limit, "aumentamos el nivel maximo")
                print("Camino recorrido: ", result[0])

            depth_limit = depth_limit + 1

    def costo_uniforme(self, graph, start, end):

        if start not in graph:
            raise TypeError(str(start) + ' no fue encontrado en el grafo!')
            return

        if end not in graph:
            raise TypeError(str(end) + ' no fue encontrado en el grafo!')
            return
        
        queue_a = queue.PriorityQueue()
        queue_a.put((0, [start]))
        #print("Start: ", start)
        
        while not queue_a.empty():
            node = queue_a.get()
            current = node[1][len(node[1]) - 1]
            #print('node: ', node)
            #print('len node: ', len(node[1]))
            #print('current: ', current)
            
            if end in node[1]:
                print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
                break
            
            cost = node[0]
            for neighbor in graph[current]:
                temp = node[1][:]

                #print("TEMP: ", temp)
                #print("neig: ", neighbor)
                temp.append(neighbor)
                queue_a.put((cost + graph[current][neighbor], temp))
    
    def get_heuristic(self, graph, ciudad):
        return graph[ciudad]

    def get_heuristic_2(self, graph, ciudad_origen, ciudad_destino):
        
        x1 = graph[ciudad_origen]['x']
        y1 = graph[ciudad_origen]['y']

        x2 = graph[ciudad_destino]['x']
        y2 = graph[ciudad_destino]['y']

        #print("x1: ", x1, " x2: ", x2, " y1: ", y1, " y2: ", y2)

        return format(math.sqrt((x2-x1)**2 + (y2-y1)**2), '.1f') 

    def A_asterisco(self, graph, graph2, start, end):   #Grafo 1 -> Pesos | Grafo 2 -> Heuristica

        if start not in graph or start not in graph2:
            raise TypeError(str(start) + ' no fue encontrado en el grafo!')
            return

        if end not in graph or start not in graph2:
            raise TypeError(str(end) + ' no fue encontrado en el grafo!')
            return
        
        queue_a = queue.PriorityQueue()
        
        queue_a.put([ 0 + self.get_heuristic(graph2, start), [start], 0])    # [peso_acu + self.get_heuristic(ciudad), [lista_visitados], peso_acu]
        
        while not queue_a.empty():
            node = queue_a.get()
            current = node[1][len(node[1]) - 1]
            #print('node: ', node)
            #print('len node: ', len(node[1]))
            #print('current: ', current)
            
            if end in node[1]:
                print("Path found: " + str(node[1]) + ", Cost = " + str(node[2]))
                break

            cost = node[2]

            for neighbor in graph[current]:
                temp = node[1][:]

                if neighbor not in temp:
                    queue_a.put([ cost + graph[current][neighbor] + self.get_heuristic(graph2, neighbor) , temp + [neighbor], cost + graph[current][neighbor] ])

    def primero_el_mejor(self, graph, graph2, start, end):   #Grafo 1 -> Pesos | Grafo 2 -> Heuristica

        if start not in graph or start not in graph2:
            raise TypeError(str(start) + ' no fue encontrado en el grafo!')
            return

        if end not in graph or start not in graph2:
            raise TypeError(str(end) + ' no fue encontrado en el grafo!')
            return
        
        queue_a = queue.PriorityQueue()
        
        #queue_a.put([self.get_heuristic_2(graph2, start, start), [start], 0])

        queue_a.put([self.get_heuristic(graph2, start), [start], 0])    # [peso_acu + self.get_heuristic(ciudad), [lista_visitados], peso_acu]
        #count = 0

        while not queue_a.empty():
            node = queue_a.get()
            current = node[1][len(node[1]) - 1]
            #print('node: ', node)
            #print('len node: ', len(node[1]))
            #print('current: ', current)
            
            if end in node[1]:
                print("Path found: " + str(node[1]) + ", Cost = " + str(node[2]))
                break

            cost = node[2]
            #print("Current: ", current, " count: ", count)
            #count = count + 1

            for neighbor in graph[current]:
                temp = node[1][:]

                #print("temp ", temp)
                #print("neighbor: ", neighbor)

                if neighbor not in temp:
                    #queue_a.put([self.get_heuristic_2(graph2, current, neighbor) , temp + [neighbor], cost + graph[current][neighbor]])
                    #print("Ingreso a neighbor: ", neighbor, " con heuristica: ", self.get_heuristic_2(graph2, current, neighbor))
                    
                    queue_a.put([self.get_heuristic(graph2, neighbor) , temp + [neighbor], cost + graph[current][neighbor]])

def crear_grafo_rumania_g():
    graph = {}
    
    graph['Arad'] = {}
    graph['Arad']['Zerind'] = 75
    graph['Arad']['Timisoara'] = 118
    graph['Arad']['Sibiu'] = 140

    graph['Zerind'] = {}
    graph['Zerind']['Oradea'] = 71
    graph['Zerind']['Arad'] = 75

    graph['Timisoara'] = {}
    graph['Timisoara']['Lugoj'] = 111
    graph['Timisoara']['Arad'] = 118

    graph['Sibiu'] = {}
    graph['Sibiu']['Arad'] = 140
    graph['Sibiu']['Oradea'] = 151
    graph['Sibiu']['Fagaras'] = 99
    graph['Sibiu']['RimnicuVilcea'] = 80

    graph['Oradea'] = {}    
    graph['Oradea']['Zerind'] = 71
    graph['Oradea']['Sibiu'] = 151

    graph['Lugoj'] = {}    
    graph['Lugoj']['Timisoara'] = 111
    graph['Lugoj']['Mehadia'] = 70

    graph['RimnicuVilcea'] = {}    
    graph['RimnicuVilcea']['Sibiu'] = 80
    graph['RimnicuVilcea']['Pitesti'] = 97
    graph['RimnicuVilcea']['Craiova'] = 146

    graph['Mehadia'] = {} 
    graph['Mehadia']['Lugoj'] = 70
    graph['Mehadia']['Dobreta'] = 75

    graph['Craiova'] = {} 
    graph['Craiova']['Dobreta'] = 120
    graph['Craiova']['Pitesti'] = 138
    graph['Craiova']['RimnicuVilcea'] = 146

    graph['Pitesti'] = {} 
    graph['Pitesti']['Craiova'] = 138
    graph['Pitesti']['Bucharest'] = 101
    graph['Pitesti']['RimnicuVilcea'] = 97

    graph['Fagaras'] = {} 
    graph['Fagaras']['Sibiu'] = 99
    graph['Fagaras']['Bucharest'] = 211

    graph['Dobreta'] = {} 
    graph['Dobreta']['Mehadia'] = 75
    graph['Dobreta']['Craiova'] = 120

    graph['Bucharest'] = {} 
    graph['Bucharest']['Fagaras'] = 211
    graph['Bucharest']['Pitesti'] = 101
    graph['Bucharest']['Giurgiu'] = 90

    graph['Giurgiu'] = {} 
    graph['Giurgiu']['Bucharest'] = 90

    #print("Created graph: ", graph)

    graph2 = {
        'Arad':366,
        'Bucharest':0,
        'Craiova':160,
        'Dobreta':242,
        'Eforie':161,
        'Fagaras':178,
        'Giurgiu':77,
        'Hirsova':151,
        'Iasi':226,
        'Lugoj':244,
        'Mehadia':141,
        'Neamt':234,
        'Oradea':380,
        'Pitesti':98,
        'RimnicuVilcea':193,
        'Sibiu':253,
        'Timisoara':329,
        'Urziceni':80,
        'Vaslui':199,
        'Zerind':374
    }

    return graph, graph2

grafo_rumania_pesos, grafo_rumania_heuristica = crear_grafo_rumania_g()

grafo_jarra = {
    '(0,0)': {'(4,0)':1, '(0,3)':1},
    '(4,0)': {'(4,3)':1, '(0,0)':1, '(1,3)':1},
    '(4,3)': {'(0,3)':1, '(4,0)':1},
    '(0,3)': {'(4,3)':1, '(0,0)':1, '(3,0)':1},
    '(1,3)': {'(4,3)':1, '(0,3)':1, '(1,0)':1, '(4,0)':1},
    '(1,0)': {'(4,0)':1, '(1,3)':1, '(0,0)':1, '(0,1)':1},
    '(0,1)': {'(4,1)':1, '(0,3)':1, '(0,0)':1, '(1,0)':1},
    '(4,1)': {'(4,3)':1, '(0,1)':1, '(4,0)':1, '(3,3)':1},
    '(3,0)': {'(3,3)':1, '(4,0)':1, '(0,0)':1, '(0,3)':1},
    '(3,3)': {'(4,3)':1, '(0,3)':1, '(3,0)':1, '(4,2)':1},
    '(4,2)': {'(4,3)':1, '(0,2)':1, '(4,0)':1, '(3,3)':1},
    '(0,2)': {'(4,2)':1, '(0,3)':1, '(0,0)':1, '(2,0)':1},
    '(2,0)': {'(2,3)':1, '(4,0)':1, '(0,0)':1, '(0,2)':1},
    '(2,3)': {'(4,3)':1, '(0,3)':1, '(2,0)':1, '(4,1)':1},
}

grafo_granjero = {
    '(0,0,0,0)': {'(1,1,0,0)':1},
    '(1,1,0,0)': {'(0,0,0,0)':1, '(0,1,0,0)':1},
    '(0,1,0,0)': {'(1,1,0,0)':1, '(1,1,0,1)':1, '(1,1,1,0)':1},
    '(1,1,0,1)': {'(0,0,0,1)':1, '(0,1,0,0)':1},
    '(0,0,0,1)': {'(1,1,0,1)':1, '(1,0,1,1)':1},
    '(1,1,1,0)': {'(0,1,0,0)':1, '(0,0,1,0)':1},
    '(0,0,1,0)': {'(1,1,1,0)':1, '(1,0,1,1)':1},
    '(1,0,1,1)': {'(0,0,0,1)':1, '(0,0,1,0)':1, '(0,0,1,1)':1},
    '(0,0,1,1)': {'(1,0,1,1)':1, '(1,1,1,1)':1},
    '(1,1,1,1)': {'(0,0,1,1)':1}
}

grafo_4_reinas = {
    '(x,y)':{'(0,0)':1, '(1,0)':1, '(2,0)':1, '(3,0)':1},
    '(0,0)':{'(2,1)':1, '(3,1)':1},
    '(1,0)':{'(3,1)':1},
    '(2,0)':{'(0,1)':1},
    '(3,0)':{'(0,1)':1, '(1,1)':1},
    '(3,1)':{'(1,2)':1, '(0,2)':1},
    '(0,1)':{'(3,2)':1, '(2,2)':1},
    '(0,2)':{'(2,3)':1},
    '(3,2)':{'(1,3)':1}
}

grafo_4_reinas_ = {
    matriz(4,4, []) : { matriz(4,4, [(0,0)]) : 1, matriz(4,4, [(1,0)]) : 1, matriz(4,4, [(2,0)]) : 1, matriz(4,4, [(3,0)]) : 1},
    matriz(4,4, [(0,0)]) : {matriz(4,4, [(2,1)]) : 1, matriz(4,4, [(3,1)]) : 1},
    matriz(4,4, [(1,0)]) : {matriz(4,4, [(3,1)]) : 1},
    matriz(4,4, [(2,0)]) : {matriz(4,4, [(0,1)]) : 1},
    matriz(4,4, [(3,0)]) : {matriz(4,4, [(0,1)]) : 1, matriz(4,4, [(1,1)]) : 1},
    matriz(4,4, [(3,1)]) : {matriz(4,4, [(1,2)]) : 1, matriz(4,4, [(0,2)]) : 1},
    #matriz(4,4, [(0,0)])
}

grafo_frankfurt_munchen = {
    'frankfurt':{'mannheim':85, 'wuzburg':217, 'kassel':173},
    'mannheim':{'frankfurt':85, 'karlsruhe':80},
    'wuzburg':{'frankfurt':217, 'erfurt':186, 'nurnberg':103},
    'kassel':{'frankfurt':173, 'munchen':502},
    'karlsruhe':{'mannheim':80, 'augsburg':250},
    'nurnberg':{'wuzburg':103, 'stuttgart':183, 'munchen':167},
    'erfurt':{'wuzburg':186},
    'stuttgart':{'nurnberg':183},
    'augsburg':{'karlsruhe':250, 'munchen':84},
    'munchen':{'augsburg':84, 'nurnberg':167, 'kassel':502}
}

grafo_sevilla_almeria_pesos = {
    'Sevilla':{'Cordoba':1, 'Malaga':1, 'Cadiz':1, 'Huelvas':1},
    'Huelvas':{'Cadiz':1, 'Sevilla':1},
    'Cadiz':{'Sevilla':1, 'Malaga':1},
    'Malaga':{'Sevilla':1, 'Cordoba':1, 'Granada':1},
    'Cordoba':{'Sevilla':1, 'Granada':1, 'Jaen':1},
    'Jaen':{'Cordoba':1, 'Granada':1, 'Almeria':1},
    'Granada':{'Malaga':1, 'Cordoba':1, 'Jaen':1, 'Almeria':1},
    'Almeria':{'Jaen':1, 'Granada':1}
}

grafo_sevilla_almeria_heuristica = {
    'Almeria':{'x':409.5, 'y':93},
    'Granada':{'x': 309, 'y': 127.5},
    'Malaga':{'x': 232.5, 'y': 75},
    'Cadiz':{'x': 63, 'y': 57},
    'Huelvas':{'x': 3, 'y': 139.5},
    'Sevilla':{'x': 90, 'y': 153},
    'Cordoba':{'x': 198, 'y': 207},
    'Jaen':{'x': 295.5, 'y': 192},
}

#print(grafo_sevilla_almeria_heuristica['Almeria']['x'])
#print(grafo_sevilla_almeria_heuristica['Almeria']['y'])


def main():

    tree1 = tree_searchs("Arbol 1")

    print("\n\nRecorrido en profundidad: ")
    print(next(tree1.dfs_paths(grafo_4_reinas, 'blanco', '(1,1,1,1)'))) 


    #print("\n\nRecorrido en profundidad con limite iterativo: ")
    #tree1.dfs_paths_limit(grafo_jarra, '(0,0)', '(2,0)', 8)


    #print("\n\nRecorrido en anchura: ")
    #print(next(tree1.bfs_paths(grafo_granjero, '(0,0,0,0)', '(1,1,1,1)')))


    #print("\n\nRecorrido costo uniforme: ")
    #tree1.costo_uniforme(grafo_frankfurt_munchen, 'frankfurt', 'munchen')

    print("\n\nRecorrido primero el mejor: ")
    tree1.primero_el_mejor(grafo_rumania_pesos, grafo_rumania_heuristica, 'Arad', 'Bucharest')

    print("\n\nRecorrido A*: ")
    tree1.A_asterisco(grafo_rumania_pesos, grafo_rumania_heuristica, 'Arad', 'Bucharest')

if __name__ == "__main__":
    main()

"""

graph = {'A': [('B', 1), ('C', 1)],
         'B': [('A', 1), ('D',1), ('E', 1)],
         'C': [('A', 1), ('F', 1)],
         'D': [('B', 1)],
         'E': [('B', 1), ('F', 1)],
         'F': [('C', 1), ('E', 1)]}

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

#https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Flizardorodriguez.files.wordpress.com%2F2012%2F06%2Fg-recorrido-4.png&f=1

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

#https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.slidesharecdn.com%2Frecorridodegrafos1raparte-140625160952-phpapp02%2F95%2Frecorrido-de-grafos-1ra-parte-5-638.jpg%3Fcb%3D1403712626&f=1
#https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.slidesharecdn.com%2Frecorridos-140625015636-phpapp02%2F95%2Frecorridos-3-638.jpg%3Fcb%3D1403661419&f=1

graph3 = {
    # Origen : destinos = (destino, peso_arista)
    "S":[("A", 1), ("B", 5), ("C", 15)],
    "A":[("G", 10), ("S", 1)],
    "G":[("C", 5), ("A", 10)],
    "C":[("S", 15), ("G", 5)],
    "B":[("G", 5), ("S", 5)],
}

#https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fslideplayer.es%2F92355%2F1%2Fimages%2F33%2FB%25C3%25BAsqueda%2Bde%2Bcosto%2Buniforme.jpg&f=1

graph4 = {
    # Origen : destinos = (destino, peso_arista)
    "S":[("A", 1), ("G", 12)],
    "A":[("B", 3), ("C", 1)],
    "G":[],
    "C":[("D", 1), ("G", 2)],
    "B":[("D", 3)],
    "D":[("G", 3)],
}

#https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fadvanceintelligence.files.wordpress.com%2F2015%2F02%2Fdat.png&f=1

graph_class = {
         'A': [('B', 1), ('C', 1), ('D', 1)],
         'B': [('A', 1), ('E', 1), ('F', 1)],
         'C': [('A', 1), ('G', 1), ('H', 1)],
         'D': [('A', 1), ('G', 1), ('H', 1)],
         'E': [('B', 1), ('I', 1)],
         'F': [('B', 1), ('I', 1), ('K', 1)],
         'G': [('C', 1), ('D', 1), ('K', 1)],
         'H': [('C', 1), ('D', 1), ('L', 1)],
         'I': [('E', 1),('F', 1), ('J', 1), ('L', 1)],
         'J': [('I', 1), ('K', 1), ('L', 1)],
         'K': [('F', 1), ('G', 1), ('J', 1), ('L', 1)],
         'L': [('H', 1), ('I', 1), ('K', 1)],
         }

"""