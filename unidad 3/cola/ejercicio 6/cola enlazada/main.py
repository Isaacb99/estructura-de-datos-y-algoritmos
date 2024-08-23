from clase_cola import Cola
import random

if __name__ == "__main__":

    cola = Cola()

    impresora = 0 #varaible cajero en los apuntes
    t_i = 5 #tiempo de impresora
    acumula_tiempo_espera = 0
    contador_impresion = 0

    x = int(input("ingrese frecuencia de llegada de la impresiones \n"))
    y = int(input("ingrese tiempo de atencion de la impresora \n"))
    tms = int(input("ingrese tiempo maximo de simulacion \n"))

    reloj = 0

    while reloj <= tms:

        if(0 < random.random() <= 1/x):
            ta = int(input("ingrese tiempo asociado \n"))
            cola.insertar(ta, reloj)
            p = cola.recuperarPr()
            cola.recorrer(p)
        
        if(impresora == 0): #evalua que la impresora este libre
            if(not cola.vacia()):
                t_a, t_e = cola.suprimir()
                acumula_tiempo_espera = reloj - t_e
                contador_impresion += 1
                if t_a <= t_i:
                    impresora = t_a
                else:
                    impresora = t_i
                    cola.insertar(t_a - t_i, reloj)
        elif(impresora > 0):
            impresora -= 1
        
        reloj += 1
    


    print("tiempo promedio de espera: {}". format(acumula_tiempo_espera/contador_impresion))


