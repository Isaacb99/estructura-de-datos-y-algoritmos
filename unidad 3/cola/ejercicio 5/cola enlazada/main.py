from clase_cola import Cola
import os

if __name__ == "__main__":
    cola = Cola()

    salir = True
    while salir:
        print("opcion 1: ingresar item a la pila")
        print("opcion 2: suprimir y recuperar el ultimo item de la pila")
        print("opcion 3: recorrer la pila")
        print("opcion 4: salir")
        opcion = int(input("Ingrese opcion: \n"))
        os.system("cls")

        if opcion == 1:
            item= int(input("Ingrese dato a ingresar"))
            cola.insertar(item)
        
        elif opcion == 2:
            item = cola.suprimir()
            print("item al principio de la cola: {}".format(item))
        
        elif opcion == 3:
            pr = cola.recuperarPr()
            cola.recorrer(pr)

        else:
            salir = not salir
            print("programa finalizado")
