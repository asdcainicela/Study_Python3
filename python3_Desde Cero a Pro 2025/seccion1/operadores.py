
##Operadores aritmeticos

x= float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

#sumar
suma = x + y
print("la suma de ", x, " + ", y, " es ", suma)

#restar
resta = x - y
print("la resta de ", x, " - ", y, " es ", resta)

#multiplicar
multiplicacion = x * y
print("la multiplicacion de ", x, " * ", y, " es ", multiplicacion)

#dividir
if y == 0:
    print("No se puede dividir entre cero")
else:
    division = x / y
    print("la division de ", x, " / ", y, " es ", division)

## operadores comparativos

# >
print("x es mayor que y: ", x > y)
# <
print("x es menor que y: ", x < y)
# ==
print("x es igual a y: ", x == y)
# !=
print("x es diferente de y: ", x != y)
# >=
print("x es mayor o igual que y: ", x >= y)
# <=
print("x es menor o igual que y: ", x <= y)

## creo que esto no entraría o sí
# %
print("el residuo de la division de x / y es: ", x % y)

#- others
potencia = x ** y
print("la potencia de x ^ y es: ", potencia)