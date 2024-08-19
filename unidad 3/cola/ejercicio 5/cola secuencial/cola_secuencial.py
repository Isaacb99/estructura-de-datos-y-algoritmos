import numpy as np

class Cola:
    __items:  np.ndarray
    __pr: int
    __ul: int
    __cant: int
    __max: int

    def __init__(self, cant=0, pr=0, ul=0, max=20):
        self.__items = np.empty(max, dtype=int)
        self.__cant = cant
        self.__pr = pr
        self.__ul = ul
        self.__max = max

    def vacia(self):
        return (self.__cant==0)
    
    def insertar(self, x):
        if(self.__cant < self.__max):
            self.__items[self.__ul] = x
            self.__ul = (self.__ul + 1) % self.__max
            self.__cant += 1
        else:
            print("cola llena")
    
    def suprimir(self):
        if self.vacia():
            print("cola vacia")
        else:
            x = self.__items[self.__pr]
            self.__pr = (self.__pr + 1) % self.__max
            self.__cant -= 1
            return x
        
    # def recorrer(self):
    #     if not self.vacia():
    #         i= self.__pr 
    #         j=0
    #         for i in range

