import time
import threading

def imprimirValor():
    time.sleep(0.3)
    print("Hola mundo")

#Ejecucion secuencial
#for i in range(15):
#    imprimirValor()

#Ejecucion concurrente
#for i in range(15):
#    hilo = threading.Thread(target=imprimirValor)
#    hilo.start()

def imprimir1():
    time.sleep(0.3)
    print("Ejecutando hilo 1")

def imprimir2():
    time.sleep(0.3)
    print("Ejecutando hilo 2")

def imprimir3():
    time.sleep(0.3)
    print("Ejecutando hilo 3")

hilo1= threading.Thread(target=imprimir1)
hilo2= threading.Thread(target=imprimir2)
hilo3= threading.Thread(target=imprimir3)

hilo1.start()
hilo2.start()
hilo3.start()