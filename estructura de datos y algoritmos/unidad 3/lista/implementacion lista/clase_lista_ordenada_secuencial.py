import numpy as np


class ListaOrdenada:
    def __init__(self, maximo):
      self.__ultimo = maximo
      self.__lista = np.empty(maximo, dtype=int)
      self.__cantidad = 0
      
    def suprimir(self, pos):
        if 1 <= pos <= self.__cantidad:
            pos_final = self.__cantidad
            while pos_final != pos-1:
                self.__lista[pos-1] = self.__lista[pos]
                pos += 1
            self.__cantidad -= 1
        else:
            raise ValueError("Ingreso de posición inválida")
         
    def insertar(self, elem):
        
        if not self.llena():

            i = self.__cantidad - 1
            while i >= 0 and self.__lista[i] > elem:
                self.__lista[i + 1] = self.__lista[i]
                i -= 1
            self.__lista[i + 1] = elem
            
            self.__cantidad += 1
                
    def recuperar(self, pos):
        if pos <= self.__cantidad and 1 < pos and pos <= self.__ultimo:
            return self.__lista[pos-1]
        
        else:
            raise ValueError("No se encontro elemento en la posicion")
            
        
    def buscar(self, elem):
        i = 0
        while i < self.__ultimo-1 and self.__lista[i] != elem:
            i += 1
        
        if not i < self.__ultimo-1:
            i = -1
        else:
            i += 1
            
        return i        
        
    def primer_elemento(self):
        if self.__cantidad > 0:
            return self.__lista[0]
        else:
            raise ValueError("El arreglo está vacío")
    
    def ultimo_elemento(self):
        if self.__cantidad > 0:
            return self.__lista[self.__ultimo-1]
        else:
            raise ValueError("El arreglo está vacío")
        
    def recorrer(self):
        for i in range(0, self.__cantidad):
            print(self.__lista[i])
            
    def siguiente(self, pos):
        if 1 <= pos < self.__ultimo:
            aux = self.__cab
            while aux.getSiguiente():
                
                aux = aux.getSiguiente()
        else:
            raise ValueError("No se puede buscar posicion siguiente")
        
    def anterior(self, pos):
        if 1 < pos <= self.__ultimo:
            return pos - 1
        else:
            raise ValueError("No se puede buscar posicion anterior")
        
    def vacia(self):
        return self.__cantidad == 0
        
    def llena(self):
        return self.__cantidad == self.__ultimo
    
    def __str__(self):
        print(self.__lista)
        return ""