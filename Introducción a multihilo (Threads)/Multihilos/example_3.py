"""
🧩 Problema final: Fábrica sincronizada de incrementos
🏭 Contexto:
Una fábrica tiene varias máquinas (hilos trabajadores) que realizan tareas.
El proceso se divide en 2 fases sincronizadas:

🔁 Fase de espera:
    Las máquinas esperan una luz verde (evento) para empezar a trabajar.
⚙️ Fase de trabajo crítico:
    Cada máquina incrementa un contador compartido muchas veces, protegido con with lock:.
Al final, el hilo principal imprime el valor final del contador, y se asegura que todas las máquinas hayan terminado.
"""

"""
📄 Enunciado para implementar
Implementa un programa en Python que:

Cree una variable contador inicializada en 0.
Inicie 5 hilos que:
    Esperan a que se active un evento_inicio.
    Luego, suman 1000 al contador, protegidos con with lock:.
El hilo principal:
    Espera 2 segundos y luego activa el evento (.set()).
    Espera a que todos los hilos terminen.
    Imprime Contador final: 5000.
"""
import threading
import time

lock = threading.Lock()
evento_inicio = threading.Event()

def activar_evento():
    print("Esperando 2 segundos para activar el evento de inicio...")
    time.sleep(2)
    print("Activando evento de inicio...")
    evento_inicio.set()

def incrementar(evento):
    global contador
    evento.wait()  # Se bloquea hasta que esté activado
    for _ in range(1000):
        with lock:
            contador += 1
        
contador = 0

hilos = []
num_hilos = 5

for _ in range(num_hilos + 1):
    if _ == num_hilos:
        hilo = threading.Thread(target=activar_evento)
    else:
        hilo = threading.Thread(target=incrementar, args=(evento_inicio,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join() 

print(f"Contador final: {contador}")
