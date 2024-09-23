
class Nodo:
    __item: int
    __izq: None
    __der: None

    def __init__(self, item=None, izq=None, der=None) -> None:
        self.__item = item
        self.__izq = izq
        self.__der = der

    def obtenerItem(self):
        return self.__item
    
    def cargaItem(self, x):
        self.__item = x
    
    def cargaIzq(self, nodo):
        self.__izq = nodo

    def obtenerIzq(self):
        return self.__izq

    def cargaDer(self, nodo):
        self.__der = nodo

    def obtenerDer(self):
        return self.__der