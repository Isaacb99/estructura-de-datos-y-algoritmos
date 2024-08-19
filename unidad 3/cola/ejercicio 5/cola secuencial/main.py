from cola_secuencial import Cola

if __name__ == "__main__":
    cola = Cola()

    salir = True
    while salir:
        print("opcion 1: insertar un elemento a la cola")
        print("opcion 2: suprimir el primer elemento")
        print("opcion 3: salir")
        opcion = int(input("ingrese opcion: \n"))

        if opcion == 1:
            x = int(input("ingrese el elemento: "))
            cola.insertar(x)
        
        elif opcion == 2:
            print("elemento suprimido: {}".format(cola.suprimir()))
        
        else:
            salir = not salir
