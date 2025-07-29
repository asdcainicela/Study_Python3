"""
Simula un sistema de registro para una biblioteca:

- Pide el nombre del usuario, su edad y si es estudiante (S/N).
- Si tiene menos de 12 años, solo puede acceder a libros infantiles.
- Si es mayor de edad y estudiante, puede acceder a todo el catálogo con 50% de descuento.
- Si es mayor de edad pero no estudiante, accede a todo sin descuento.
- Si tiene entre 12 y 17, accede solo a libros generales (sin descuento).

Muestra un resumen claro del acceso y beneficios.
"""

estudiante = {}
estudiante["nombre"] = input("Introduzca su nombre: ")
estudiante["edad"] = int(input("Introduzca su edad: "))
estudiante["estudiante"] = input("¿Eres estudiante? (Si/No): ")

estudiante["beneficio"] = "Sin descuento"

if estudiante["edad"] < 12:
    estudiante["acceso"] = "Libros infantiles"
    
elif estudiante["edad"] <= 17:
    estudiante["acceso"] = "Libros generales"
else:
    if estudiante["estudiante"].lower() == "si":
        estudiante["acceso"] = "Catálogo completo"
        estudiante["beneficio"] = "50% de descuento"
    else:
        estudiante["acceso"] = "Catálogo completo"

print("=" * 40)
print(f"Resumen de acceso para {estudiante['nombre']}:")
print(f"Edad: {estudiante['edad']}")
print(f"Acceso: {estudiante['acceso']}")
print(f"Beneficio: {estudiante['beneficio']}")
