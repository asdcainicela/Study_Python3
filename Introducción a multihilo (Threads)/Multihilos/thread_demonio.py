import threading
import time

def prueba1():
    while True:
        print("Prueba 1 en ejecución")
        time.sleep(1)

# el demon thread se ejecuta en segundo plano y no bloquea el hilo principal
# si el hilo principal termina, el demon thread también termina

hilo = threading.Thread(target=prueba1, daemon=True)
hilo.start()
print("hola")