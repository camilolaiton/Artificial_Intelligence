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
            (vertex, path) = queue.pop(0)
            print path
            l = list(set(graph[vertex]) - set(path))
            for next in sorted(l):
                print graph[vertex]
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))
    
    def dfs_paths(self, graph, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            print 'path: ' , path
            l = list(set(graph[vertex]) - set(path))
            for next in sorted(l, reverse=True):
                            
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))


grafo_jarra = {

    '(0,0)': ['(4,0)', '(0,3)'],
    '(4,0)': ['(4,3)', '(0,0)', '(1,3)'],
    '(4,3)': ['(0,3)', '(4,0)'],
    '(0,3)': ['(4,3)', '(0,0)', '(3,0)'],
    '(1,3)': ['(4,3)', '(0,3)', '(1,0)', '(4,0)'],
    '(1,0)': ['(4,0)', '(1,3)', '(0,0)', '(0,1)'],
    '(0,1)': ['(4,1)', '(0,3)', '(0,0)', '(1,0)'],
    '(4,1)': ['(4,3)', '(0,1)', '(4,0)', '(3,3)'],
    '(3,0)': ['(3,3)', '(4,0)', '(0,0)', '(0,3)'],
    '(3,3)': ['(4,3)', '(0,3)', '(3,0)', '(4,2)'],
    '(4,2)': ['(4,3)', '(0,2)', '(4,0)', '(3,3)'],
    '(0,2)': ['(4,2)', '(0,3)', '(0,0)', '(2,0)'],
    '(2,0)': ['(2,3)', '(4,0)', '(0,0)', '(0,2)'],
    '(2,3)': ['(4,3)', '(0,3)', '(2,0)', '(4,1)'],
}

grafo_granjero = {
    '(0,0,0,0)': ['(1,1,0,0)'],
    '(1,1,0,0)': ['(0,0,0,0)', '(0,1,0,0)'],
    '(0,1,0,0)': ['(1,1,0,0)', '(1,1,0,1)', '(1,1,1,0)'],
    '(1,1,0,1)': ['(0,0,0,1)', '(0,1,0,0)'],
    '(0,0,0,1)': ['(1,1,0,1)', '(1,0,1,1)'],
    '(1,1,1,0)': ['(0,1,0,0)', '(0,0,1,0)'],
    '(0,0,1,0)': ['(1,1,1,0)', '(1,0,1,1)'],
    '(1,0,1,1)': ['(0,0,0,1)', '(0,0,1,0)', '(0,0,1,1)'],
    '(0,0,1,1)': ['(1,0,1,1)', '(1,1,1,1)'],
    '(1,1,1,1)': ['(0,0,1,1)'],
}

graph3 = {
    # Origen : destinos = (destino, peso_arista)
    "S":[("A", 1), ("B", 5), ("C", 15)],
    "A":[("G", 10), ("S", 1)],
    "G":[("C", 5), ("A", 10)],
    "C":[("S", 15), ("G", 5)],
    "B":[("G", 5), ("S", 5)],
}

tree1 = tree_searchs("Arbol 1")

print next(tree1.dfs_paths(grafo_jarra, '(0,0)', '(2,0)')) 
print next(tree1.bfs_paths(grafo_jarra, '(0,0)', '(2,0)'))

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

grafo_jarra = {

    '(0,0)': [('(4,0)', 1), ('(0,3)', 1)],
    '(4,0)': [('(4,3)', 1), ('(0,0)', 1), ('(1,3)', 1)],
    '(4,3)': [('(0,3)', 1), ('(4,0)', 1)],
    '(0,3)': [('(4,3)', 1), ('(0,0)', 1), ('(3,0)', 1)],
    '(1,3)': [('(4,3)', 1), ('(0,3)', 1), ('(1,0)', 1), ('(4,0)', 1)],
    '(1,0)': [('(4,0)', 1), ('(1,3)', 1), ('(0,0)', 1), ('(0,1)', 1)],
    '(0,1)': [('(4,1)', 1), ('(0,3)', 1), ('(0,0)', 1), ('(1,0)', 1)],
    '(4,1)': [('(4,3)', 1), ('(0,1)', 1), ('(4,0)', 1), ('(3,3)', 1)],
    '(3,0)': [('(3,3)', 1), ('(4,0)', 1), ('(0,0)', 1), ('(0,3)', 1)],
    '(3,3)': [('(4,3)', 1), ('(0,3)', 1), ('(3,0)', 1), ('(4,2)', 1)],
    '(4,2)': [('(4,3)', 1), ('(0,2)', 1), ('(4,0)', 1), ('(3,3)', 1)],
    '(0,2)': [('(4,2)', 1), ('(0,3)', 1), ('(0,0)', 1), ('(2,0)', 1)],
    '(2,0)': [('(2,3)', 1), ('(4,0)', 1), ('(0,0)', 1), ('(0,2)', 1)],
    '(2,3)': [('(4,3)', 1), ('(0,3)', 1), ('(2,0)', 1), ('(4,1)', 1)],
}

"""