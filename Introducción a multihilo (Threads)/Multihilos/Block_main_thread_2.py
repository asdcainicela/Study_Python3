import threading
import time

def prueba1(): 
    global x
    time.sleep(0.5)
    x=1
    print("Prueba 1 completada")

def prueba2(): 
    global y
    time.sleep(1)
    y=2
    print("Prueba 2 completada")

def prueba3(): 
    global z
    time.sleep(2)
    z=3
    print("Prueba 3 completada")    

x=0
y=0
z=0

hilo1 = threading.Thread(target=prueba1)
hilo2 = threading.Thread(target=prueba2)
hilo3 = threading.Thread(target=prueba3)
hilo1.start()
hilo2.start()
hilo3.start()
# sin join(), el hilo principal no espera a que los hilos terminen
# y puede que los valores de x, y, z no se hayan asignado cuando se 
# compruebe la condición final.
# Esto puede llevar a resultados inesperados.
hilo1.join()
hilo2.join()
hilo3.join()

if x ==1 and y ==2 and z ==3:
    print("Todo correcto")
else:
    print("Error")