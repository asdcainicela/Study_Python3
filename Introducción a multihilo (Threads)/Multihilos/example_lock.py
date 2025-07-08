"""
🧩 Problema: Contador seguro con múltiples hilos
Tienes una variable global llamada contador, que inicialmente es 0.
Crea 10 hilos, y cada hilo debe:

Sumar 1 al contador mil veces.

El acceso al contador debe estar protegido con with lock: para evitar condiciones de carrera.
"""

import threading 

lock = threading.Lock()

def suma_lock():
    global contador
    for i in range(1000):
        with lock:
            contador += 1

contador = 0
num_hilos = 10

hilos = []
for i in range(num_hilos):
    hilo = threading.Thread(target=suma_lock)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Contador final:", contador)