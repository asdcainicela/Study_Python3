"""
Simula un sistema de registro de préstamos de libros:

1. Crea una lista vacía llamada `prestamos`.
2. En un bucle, pide al usuario ingresar el nombre de un libro prestado.
3. Detén el bucle cuando el usuario escriba "fin".
4. Al final, imprime todos los libros prestados con su número de orden.
5. Si no se prestó ningún libro, muestra un mensaje correspondiente.
"""

prestamos = []

while True:
    libro_prestado = input("Ingrese libro a prestar (o 'fin' para terminar): ").strip()
    if libro_prestado.lower() == "fin":
        break
    if libro_prestado:  
        prestamos.append(libro_prestado)

print("=" * 40)
if not prestamos:
    print("No se prestó ningún libro.")
else:
    print("Libros prestados:")
    for i, libro in enumerate(prestamos, start=1):
        print(f"{i}. {libro}")
