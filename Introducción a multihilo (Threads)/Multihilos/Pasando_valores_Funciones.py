import threading

def sumar1(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

def sumar2(a, b):
    resultado = a + b
    print(f"La suma de {a} y {b} es: {resultado}")

def sumar3(a):
    resultado = a + a
    print(f"La suma de {a} y {a} es: {resultado}")

def sumar4(a, b): 
    print(a+b)

hilo1 = threading.Thread(target=sumar1, args=[5, 10])
hilo1.start()

hilo2 = threading.Thread(target=sumar2, args=(5, 10))
hilo2.start()

hilo3 = threading.Thread(target=sumar3, args=(5,))
hilo3.start()

hilo4 = threading.Thread(target=sumar4, kwargs={'a': 5, 'b': 10})
hilo4.start()