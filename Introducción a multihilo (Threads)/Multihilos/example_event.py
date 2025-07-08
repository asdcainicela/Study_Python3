"""
Pregunta / Reto de sincronización con threading.Event
Implementa un programa en Python con las siguientes características:

Hay dos hilos (Hilo A y Hilo B).

El hilo A debe imprimir "Hilo A: esperando luz verde" y quedarse esperando hasta que reciba una señal (evento).

El hilo B debe esperar 3 segundos, luego imprimir "Hilo B: luz verde activada" y activar el evento para desbloquear al hilo A.

Una vez que el hilo A continúa, imprime "Hilo A: cruzando" y termina.

Al final, el hilo principal debe imprimir "Programa terminado" cuando ambos hilos hayan terminado.
"""

import threading
import time

evento = threading.Event()

def sincronizacion1(event):
    print("Hilo A: Esperando luz verde")
    event.wait()  # Espera a que el evento sea activado
    print("Hilo A: cruzando")

def sincronizacion2(event):
    time.sleep(3)  # Simula un tiempo de espera antes de activar el evento
    print("Hilo B: Esperando luz verde")
    event.set()

hiloA= threading.Thread(target=sincronizacion1, args=(evento,))
hiloA.start()

hiloB = threading.Thread(target=sincronizacion2, args=(evento,))
hiloB.start()

hiloA.join()
hiloB.join()

print("programa finalizado")