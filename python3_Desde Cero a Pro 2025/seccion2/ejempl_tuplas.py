

personas = (("Luis", 20), ("jose", 25), ("maria", 16), ("pedro", 45))

for name, edad in personas:
    #print("el nombre es: ", name,  "y  su  edad es : ", edad)
    if edad >=18:
        print(name, "es mayor de edad")
    else:
        print(name, "es menor de edad")

numeros = (10, 20, 30, 40, 50, 100, 5000, 100000)
suma = sum(numeros)
print("La suma de los numeros es:", suma)