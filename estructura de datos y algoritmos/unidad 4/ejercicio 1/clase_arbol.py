from clase_nodo import Nodo

class Arbol:
    __raiz: Nodo

    def __init__(self) -> None:
        self.__raiz = None
    
    def vacio(self):
        return (self.__raiz == None)
    
    def obtenerRaiz(self):
        return self.__raiz

    def mostrarRaiz(self):
        return(self.__raiz.obtenerItem())
    
    def insertarRaiz(self, x):
        aux = Nodo()
        aux.cargaItem(x)
        aux.cargaDer(None)
        aux.cargaIzq(None)
        self.__raiz = aux

    # def insertar(self, xraiz, item):
    #     if xraiz == None:
    #         nodo = Nodo()
    #         nodo.cargaItem(item)
    #         nodo.cargaDer(None)
    #         nodo.cargaIzq(None)
    #         return 
    #     elif item > xraiz.obtenerItem():
    #         self.insertar(xraiz.obtenerDer(), item)

    #     elif item < xraiz.obtenerItem():
    #         self.insertar(xraiz.obtenerIzq(), item)

    def insertar(self, xraiz, item):
        if xraiz is None:
            return Nodo(item)
        
        if item <= xraiz.obtenerItem():
            xraiz.cargaIzq(self.insertar(xraiz.obtenerIzq(), item))
        else:
            xraiz.cargaDer(self.insertar(xraiz.obtenerDer(), item))
        
        return xraiz

    def mostrar_inorden(self):
        def imprimir_nodo(nodo):
            if nodo:
                imprimir_nodo(nodo.obtenerIzq())
                print(f"{nodo.obtenerItem()}", end=" ")
                imprimir_nodo(nodo.obtenerDer())

        imprimir_nodo(self.__raiz)
        print()  # Imprime una nueva línea al final
    