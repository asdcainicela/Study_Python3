"""
Descripción: Escribe un programa en Python que calcule el promedio de una lista de números. Debes seguir estos pasos:

    Crea una lista llamada numeros que contenga al menos cinco números enteros.
    Inicializa una variable llamada suma en 0.
    Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.
    Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).

    Imprime el resultado como el promedio de los números en la lista.
"""

numeros = [41.5, 23.7, 56.8, 12.4, 34.9]
suma = 0

for numero in numeros:
    suma += numero

promedio = suma/ len(numeros)
print(f"El promedio de los números en la lista es: {promedio:.2f}")  