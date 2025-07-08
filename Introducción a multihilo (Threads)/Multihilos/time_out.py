import threading
import time


def ciclar(evento1):
    print(" Presione para enviar la señal\n")
    resp = evento1.wait(timeout=5)  # Espera a que el evento sea activado
    if resp :
        print("Sistema de enfriamiento disparado de forma manual\n")
    else:
        print("Sistema de enfriamiento disparado de forma automática\n") 

evento1= threading.Event()
hilo1 = threading.Thread(target=ciclar, args=(evento1,))
hilo1.start()

print("Esperando para enviar la señal")

time.sleep(3) 
# evento1.set()  # Activar el evento 
time.sleep(1)