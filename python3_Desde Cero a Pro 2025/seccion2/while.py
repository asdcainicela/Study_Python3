contador = 10

while contador >= 1:
    print(contador)
    contador-=1

numInput = int(input("Ingrese número entero positivo o (negativo para salir): "))
suma =0

while numInput >=0:
    suma+=numInput
    print(numInput)
    numInput = int(input("Ingrese otro número:"))

print("la suma es: ", suma)