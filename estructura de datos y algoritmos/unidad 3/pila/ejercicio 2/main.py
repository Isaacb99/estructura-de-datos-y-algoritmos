from pila_secuencial import Pila

if __name__ == "__main__":
    pila = Pila()
    numero = int(input("ingrese numero a convertir:"))

    aux = numero

    while aux >= 1:
        num = aux % 2
        pila.insertar(num)
        aux = aux // 2

    #pila.mostrar()
    #print("numero convertido a binario:")
    while not pila.vacia():
        item = pila.suprimir()
        print(item, end="")