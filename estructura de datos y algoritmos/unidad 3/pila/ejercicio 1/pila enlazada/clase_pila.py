from clase_celda import Celda

class Pila:
    __cant: int
    __tope: Celda

    def __init__(self):
        self.__tope = None
        self.__cant = 0
    
    def vacia(self):
        return (self.__cant == 0)
    
    def insertar(self, item):
        celda = Celda()
        celda.cargaItem(item)
        celda.cargaSig(self.__tope)
        self.__tope = celda
        self.__cant += 1
        print("item agregado")

    def suprimir(self):
        if self.vacia():
            print("Pila vacia")
        else:
            aux = self.__tope
            item = self.__tope.obtenerItem()
            self.__tope = self.__tope.obtenerSig()
            self.__cant -= 1
            del(aux)
            return item