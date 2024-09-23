from clase_celda import Celda

class Cola:
    __cant: int
    __pr: Celda
    __ul: Celda

    def __init__(self, pr=None, ul=None, cant=0):
        self.__pr = pr
        self.__ul = ul
        self.__cant = cant
    
    def vacia(self):
        return (self.__cant == 0)
    
    def insertar(self, x):
        nuevo = Celda()
        nuevo.cargaItem(x)
        nuevo.cargarSig(None)
        if self.__ul == None:
            self.__pr = nuevo
        else:
            self.__ul.cargarSig(nuevo)
        self.__ul = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("cola vacia")
        else:
            aux = self.__pr
            x = self.__pr.obtenerItem()
            self.__pr = self.__pr.obtenerSig()
            self.__cant -= 1
            del(aux)
            return x
    
    def recuperarPr(self):
        return self.__pr
    
    def recorrer(self, aux:Celda):
        if aux != None:
            print(aux.obtenerItem())
            self.recorrer(aux.obtenerSig())
            