import threading
import time

# ================================
# Función que ejecutará el hilo
# ================================
def ciclar(evento1, evento2):
    """
    Este hilo imprime "Ciclo While" repetidamente,
    pero se bloquea en .wait() hasta que evento1 esté activo.
    Termina cuando evento2 se activa.
    """
    while not evento2.is_set():  # Repite hasta que se active evento2
        print("Ciclo While")     # Muestra mensaje
        evento1.wait()           # Espera a que evento1 sea activado

# ================================
# Crear eventos
# ================================
evento1 = threading.Event()  # Evento de "permiso para continuar"
evento2 = threading.Event()  # Evento de "detener ejecución"

# ================================
# Crear y lanzar hilo
# ================================
hilo = threading.Thread(target=ciclar, args=(evento1, evento2))
hilo.start()

# ================================
# Hilo principal imprime 5 veces
# ================================
for i in range(5):
    time.sleep(0.5)
    print("Ciclo for")

# ================================
# Activar evento1: desbloquea .wait()
# ================================
evento1.set()  # Ahora el hilo secundario dejará de bloquearse

# ================================
# Pausa y luego finalizar
# ================================
time.sleep(1)   # Le damos tiempo para que imprima una vez más
evento2.set()   # Esto hará que el hilo termine su while

# ================================
# Esperamos a que el hilo termine
# ================================
hilo.join()
