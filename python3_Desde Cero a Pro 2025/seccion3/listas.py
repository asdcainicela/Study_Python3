# listas de numeros enteros

numeros = [ 1, 2, 3, 4, 5]

frutas = ["manzanas", "bananas", "cereza"]
mixta = [1, "hla", 1_2_3, True, 3.14159254]

print(numeros[0])
print(frutas[1])

numeros[2]=9
print(numeros[2])

numeros.append(8)
print(numeros)

frutas.append("orange")
print(frutas)

#del sirve para eliminar 

del numeros[2]
print(numeros)

del frutas[1]
print(frutas)


for frutas in frutas:
    print(frutas)

suma = sum(numeros)
print(suma)