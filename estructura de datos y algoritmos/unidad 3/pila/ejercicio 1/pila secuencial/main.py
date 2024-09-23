from pila_secuencial import Pila
import os

if __name__ == "__main__":
    salir = True
    pila = Pila()
    while salir:
        print("opcion 1: ingresar item a la pila")
        print("opcion 2: suprimir y recuperar el ultimo item de la pila")
        print("opcion 3: recorrer la pila")
        print("opcion 4: salir")
        opcion = int(input("Ingrese opcion: \n"))
        #os.system("cls")

        if opcion == 1:
            item= int(input("Ingrese dato a ingresar"))
            pila.insertar(item)
        
        elif opcion == 2:
            item = pila.suprimir()
            print("item al final de la pila: {}".format(item))
        
        elif opcion == 3:
            pila.mostrar()

        else:
            salir = not salir
            print("programa finalizado")
