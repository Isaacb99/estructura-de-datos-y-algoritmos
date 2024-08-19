from pila_secuencial import Pila

if __name__ == "__main__":

    numero = int(input("ingrese cantidad de discos para jugar: "))
    pila1 = Pila(numero)
    pila2 = Pila(numero)
    pila3 = Pila(numero)

    while numero != 0:
        pila1.insertar(numero)
        numero -= 1

    # pila1.mostrar()
    while not pila1.vacia() and not pila2.vacia():
        print("ingreso")
        pila_origen = input("seleccione con A, B, o C la pila origen")
        pila_destino = input("seleccione con A, B, o C la pila destino")

        if pila_origen == "A":
            item1 = pila1.suprimir()
            if pila_destino == "B":
                item2 = pila2.suprimir()
                if item2 > item1:
                    print("mov exitoso")
                    pila2.insertar(item2)
                    pila2.insertar(item1)
            if pila_destino == "C":
                item2 = pila3.suprimir()
                if item2 > item1:
                    print("mov exitoso")
                    pila3.insertar(item2)
                    pila3.insertar(item1)
        
        if pila_origen == "B":
            item1 = pila2.suprimir()
            if pila_destino == "C":
                item2 = pila3.suprimir()
                if item2 > item1:
                    print("mov exitoso")
                    pila3.insertar(item2)
                    pila3.insertar(item1)
            if pila_destino == "A":
                item2 = pila1.suprimir()
                if item2 > item1:
                    print("mov exitoso")
                    pila1.insertar(item2)
                    pila1.insertar(item1)
        
        
        if pila_origen == "C":
            item1 = pila3.suprimir()
            if pila_destino == "A":
                item2 = pila1.suprimir()
                if item2 > item1:
                    print("mov exitoso")
                    pila1.insertar(item2)
                    pila1.insertar(item1)
            if pila_destino == "B":
                item2 = pila2.suprimir()
                if item2 > item1:
                    print("mov exitoso")
                    pila2.insertar(item2)
                    pila2.insertar(item1)

