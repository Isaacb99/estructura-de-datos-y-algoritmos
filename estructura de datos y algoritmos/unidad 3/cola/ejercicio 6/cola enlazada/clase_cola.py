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
    
    def insertar(self, ta, te):
        nuevo = Celda()
        nuevo.cargaTiempoAsociado(ta)
        nuevo.cargaTiempoEspera(te)
        nuevo.cargarSig(None)
        if self.__ul == None:
            self.__pr = nuevo
        else:
            self.__ul.cargarSig(nuevo)
        self.__ul = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("cola vacia") # Devuelve una tupla vacía en caso de que la cola esté vacía
        elif self.__pr is not None:
            aux = self.__pr
            x = self.__pr.obtenerTiempoAsociado()
            y = self.__pr.obtenerTiempoEspera()
            self.__pr = self.__pr.obtenerSig()
            self.__cant -= 1
            if self.__pr == None:
                self.__ul = None
            return x, y 
    
    def recuperarPr(self):
        return self.__pr
    
    def recorrer(self, aux:Celda):
        if aux != None:
            print("ta:",aux.obtenerTiempoAsociado())
            print("te:",aux.obtenerTiempoEspera())
            self.recorrer(aux.obtenerSig())
