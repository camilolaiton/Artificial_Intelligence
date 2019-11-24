class celda():
    
    def __init__(self, valor):
        self.__valor = valor
    
    @property
    def valor(self):
        'This method returns the cell\'s value'
        return self.__valor

    @valor.setter
    def name(self, valor):
        'This method changes the cell\'s value'
        self.__valor = valor

class matriz():

    def __init__(self, height, width, pos_unos):
        self.height = height
        self.width = width
        self.matriz = []
        self.__llenar_matriz(pos_unos)

    def __llenar_matriz(self, pos_unos):

        for y in range(self.width):
            for x in range(self.height):
                if (x,y) in pos_unos:
                    self.matriz.append(celda(1))
                else:
                    self.matriz.append(celda(0))
    
    def obtener_celda(self, x, y):
        return self.matriz[x * self.height + y] # Formula que se usa para conseguir una celda de una matriz en una lista

    def mostrar_matriz(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                #print("X: ", x , " Y: ", y)
                celda = self.obtener_celda(x,y)
                print('%d' % celda.valor, end=" ")
            print()