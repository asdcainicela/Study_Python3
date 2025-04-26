"""
Crea un array
1. array de 4 filas
    a. primera fila debe estar formada por 6,7,9,15,22,34
    b. la 2 fila es 2 veces la primera fila
    c. 3 fila es 1 fila-5
    d. 4 fila es fila1^2
2.cuantos elemenos son pares 
"""
import numpy as np

array = np.empty([4,4])

fila1 = [6, 7, 9, 15, 22]
fila2 = [2*x for x in fila1]
fila3 = [x-5 for x in fila1]
fila4 = [x*x for x in fila1]
array = np.array([fila1, fila2, fila3, fila4])
print(array)

# pares
pares = array[array%2 ==0]
print(len(pares))

# otra forma
count = 0

for fila in array:
    for val in fila:
        if val % 2 == 0:  # aquí es doble igual
            count += 1

print(f"Hay {count} numeros pares")       