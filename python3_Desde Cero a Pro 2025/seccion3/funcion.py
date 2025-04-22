def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Jose")

def suma(a,b):
    return a+b

print(suma(2,5))

num1 =  int(input("introduce un numero: "))
num2 = int(input("ingrese otro numero: "))

resultado = suma(num1, num2)

print(resultado)

def espar(numero):
    if numero %2 ==0: 
        print(f"el {numero}  es par")
    else:
        print(f"el { numero} es impar")

numero1 = int(input("ingrese numero: "))       
espar(numero1)

def listanumeros(lista):
    maximo = max(lista)
    return maximo
numeros = [1, 56, 1, 9, 74, 56, 45, 65, 4]
valor = listanumeros(numeros)
print(f"el numero maximo de la lista {numeros} es {valor}")