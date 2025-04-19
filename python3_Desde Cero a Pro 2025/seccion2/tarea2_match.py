"""
scribe un programa Python que solicite al usuario ingresar un número entero y luego determine en qué rango se encuentra ese número utilizando la declaración match. El programa debe imprimir un mensaje que indique el rango al que pertenece el número.
Instrucciones:

    1.   Pídele al usuario que ingrese un número entero.
    2.  Utiliza la declaración match para clasificar el número en uno de los siguientes rangos:
             Rango 1: Números negativos (menores que 0).
              Rango 2: Números entre 0 (incluido) y 10 (excluido).
              Rango 3: Números mayores o iguales a 10.

    3.  Imprime un mensaje que indique en qué rango se encuentra el número ingresado.
"""

#solicitamos al cliente

numero = int(input("Introduce un número: "))

match numero:
    case n if n <0:
        print(" El numero es negativo")
    case n if n>=0 and n< 10:
        print("El numero es mayor o igual a 0 y menor a 10")
    case _:
        print("El numero es mayor o igual a 10")