import numpy as np

class Pila:
    __items: np.ndarray
    __tope: int
    __cant: int

    def __init__(self, cant=20, tope=-1): #la dimension(cantidad) del arreglo debe ser estatico
        self.__items = np.empty(cant,dtype=int) #puede ser otro tipo de dato
        self.__cant = cant
        self.__tope = tope

    def vacia(self):
        retorno = True
        if self.__tope != -1:
            retorno = False
        return retorno
    
    def insertar(self, item):
        if self.__tope < self.__cant-1:
            self.__tope += 1
            self.__items[self.__tope] = item
        else:
            print("Arreglo lleno")

    def suprimir(self):
        if self.vacia():
            print("Pila vacia")
        else:
            item = self.__items[self.__tope]
            self.__tope -= 1
        return item

    def mostrar(self):
        if  self.vacia():
            print("pila vacia")
        else:
            for i in range(self.__cant-1):
                print("{}".format(self.__items[i]))
    
