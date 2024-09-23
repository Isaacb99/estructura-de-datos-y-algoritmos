from clase_arbol import Arbol
from clase_nodo import Nodo


if __name__ == "__main__":
    arbol = Arbol()
    arbol.insertarRaiz(50)
    arbol.insertar(arbol.obtenerRaiz(), 36)
    arbol.insertar(arbol.obtenerRaiz(), 53)
    arbol.insertar(arbol.obtenerRaiz(), 12)
    arbol.insertar(arbol.obtenerRaiz(), 83)
    arbol.insertar(arbol.obtenerRaiz(), 90)
    arbol.insertar(arbol.obtenerRaiz(), 65)
    arbol.insertar(arbol.obtenerRaiz(), 20)
    arbol.insertar(arbol.obtenerRaiz(), 58)
    arbol.mostrar_inorden()
