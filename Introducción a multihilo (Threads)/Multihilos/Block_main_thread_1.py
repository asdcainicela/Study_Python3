import threading
import time

def dormir(): 
    time.sleep(5)
    print("Desperté!")

hilo = threading.Thread(target=dormir)
hilo.start()

for i in range(1000):
    time.sleep(0.01)
    print(f"Contando: {i}")

# vemos que el resultado de cada hilo no llega en orden
# y que el hilo principal no se bloquea mientras el hilo duerme.
# Esto es porque el hilo principal sigue ejecutándose mientras el hilo secundario duerme.
# Si el hilo principal estuviera bloqueado, no podríamos ver la salida del hilo secundario.
# Esto es un ejemplo de cómo los hilos pueden ejecutarse de manera concurrente.
# Si queremos que el hilo principal espere a que el hilo secundario termine,
# podemos usar el método join() del hilo secundario.
# hilo.join()  # Descomentar para que el hilo principal espere al hilo secundario