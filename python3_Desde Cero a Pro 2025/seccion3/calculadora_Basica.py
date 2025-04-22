"""
Escribe un programa en Python que realice operaciones matemáticas 
simples (suma, resta, multiplicación y división) utilizando una función.
El programa debe permitir al usuario ingresar dos números y seleccionar 
una operación para realizar.
"""
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b !=0 :
        return a/b
    else:
        return None

def calculadora(num1, num2, operacion):
    match operacion:
        case "+":
            return suma(num1, num2)
        case "-":
            return resta(num1, num2)
        case "*":
            return multiplicacion(num1, num2)
        case "/":
            return division(num1, num2)
        case _:
            return None

numero1 = float(input("Ingrese número 1: "))
numero2 = float(input("Ingrese número 2: "))
operacion = input("Ingrese operacion (+,-,*,/): ")
value = calculadora(numero1, numero2, operacion)
print(f" la operacion {operacion} y el resultado es : {value}")