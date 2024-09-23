from pila_secuencial import Pila

if __name__ == "__main__":
    pila = Pila()
    numero = int(input("ingrese numero para su calculo:"))

    aux = numero
    while aux != 1:
        pila.insertar(aux)
        aux -= 1
    
    
    while not pila.vacia():
        aux *=  pila.suprimir()

    
    print("factorial = {}".format(aux))