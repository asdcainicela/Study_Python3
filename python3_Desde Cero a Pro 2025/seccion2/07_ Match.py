
# Es similar al  swicth case de other languages !
 
numero = float(input("Por favor, introduce un numero entero:"))

if numero >=0 :
    i=1
    for i in range (1,11):
        if numero % i == 0:
            print(f"el numero {numero} es divisible por {i}")
            break 
numero = int(numero)

match numero:
    case 0: 
        print("El numero es un cero")
    case numero if numero % 2 == 0:
        print("El numero es par.")
    case numero if numero % 2 != 0:
        print("El numero no es par.")
    case _:
        print("Numero no reconocido")

