"""
Solicita nombre, edad y carrera al usuario y muestra los datos en forma de diccionario.
"""

nombre = input("introduzca nombre: ")
edad = int(input("introduzca edad: "))
carrera = input("Introudzca carrera: ")

datos_registrados = {}
datos_registrados['nombre'] = nombre
datos_registrados['edad'] = edad
datos_registrados['carrera'] = carrera
print("="*40)
print(f"Datos registrados: {datos_registrados}")