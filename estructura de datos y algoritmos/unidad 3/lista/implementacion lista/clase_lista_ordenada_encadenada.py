import numpy as np
from clase_nodo import Nodo

class ListaOrdenada:
    def __init__(self):
      self.__cab = None
      self.__cantidad = 0
      
    def suprimir(self, pos):
        if 1 <= pos <= self.__cantidad:
            if pos == 1:
                aux = self.__cab.getSiguiente()
                del(self.__cab)
                self.__cab = aux   
                
            else:
                i = 0
                aux = self.__cab
                while i < pos-1:
                    ant = aux
                    aux = aux.getSiguiente()
                
                    i += 1
                ant.setSiguiente(aux.getSiguiente())
                del(aux)
            self.__cantidad -= 1
        else:
            raise ValueError("Posición inválida")
                
            
    def insertar(self, elem):
        if type(elem) == int:
            
            nodo = Nodo(elem)               
            if self.__cantidad == 0 or self.__cab.getDato() > elem:
                nodo.setSiguiente(self.__cab)
                self.__cab = nodo
            elif self.__cantidad == 1:
                self.__cab.setSiguiente(nodo)
            else:
                aux = self.__cab
                i = 0
                while i < self.__cantidad and aux.getDato() < elem:
                    ant = aux       
                    aux = aux.getSiguiente() 
                    i += 1   
                ant.setSiguiente(nodo)
                nodo.setSiguiente(aux)    
                
            self.__cantidad += 1
        else:
            raise ValueError("Tipo de dato no valido")
            
    def recuperar(self, pos):
        if pos <= self.__cantidad and 1 < pos and pos <= self.__cantidad + 1:
                i = 0
                aux = self.__cab
                while i < pos-1:
                    i += 1
                    aux = aux.getSiguiente()
                
                return aux.getDato()
        
        else:
            raise ValueError("No se encontro elemento en la posicion")
            
        
    def buscar(self, elem):
        i = 0
        aux = self.__cab
        while i < self.__cantidad and aux.getDato() != elem:
            i += 1
            aux = aux.getSiguiente()
            
        
        if i < self.__cantidad:
            i += 1
        else:
            i = -1
            
        return i        
        
    def primer_elemento(self):
        if self.__cantidad > 0:
            return self.__cab.getDato()
        else:
            raise ValueError("El arreglo está vacío")
    
    def ultimo_elemento(self):
        if self.__cantidad > 0:
            aux = self.__cab
            while aux.getSiguiente() != None:
                aux = aux.getSiguiente()
            return aux.getDato()
        else:
            raise ValueError("El arreglo está vacío")
        
    def recorrer(self):
        aux = self.__cab
        while aux.getSiguiente() != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
        print(aux.getDato())
            
    def siguiente(self, pos):
        
        if 1 <= pos <= self.__cantidad:
            i = 0
            aux = self.__cab
            while i < pos-1:
                aux = aux.getSiguiente()
                i += 1
                
            return aux.getSiguiente().getDato()
                
        else:
            raise ValueError("No se puede buscar posicion siguiente")
        
    def anterior(self, pos):
        if 1 < pos <= self.__cantidad:
            aux = self.__cab
            i = 1
            while i < pos-1:
                aux = aux.getSiguiente()
                i += 1
                
            return aux.getDato()
        else:
            raise ValueError("No se puede buscar posicion anterior")
        
    def vacia(self):
        return self.__cantidad == 0
        