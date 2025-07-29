"""
Crea un sistema de control de stock de libros usando funciones:

1. Define una función `agregar_libro(stock: list) -> None` que:
   - Pida al usuario un título y lo agregue al stock si no está repetido.
   - Muestra un mensaje si ya existe.

2. Define una función `mostrar_stock(stock: list) -> None` que:
   - Muestre todos los libros con índice.
   - Si está vacío, muestre "No hay libros en stock".

3. En el programa principal:
   - Crea una lista vacía llamada `stock`.
   - Muestra un menú con opciones:
     1. Agregar libro
     2. Ver stock
     3. Salir
   - Repite hasta que el usuario elija salir.
"""

def agregar_libro(stock: list) -> None:
    titulo = input("Ingrese título del libro: ").strip()
    if not titulo:
        print("Título vacío, intente de nuevo.")
        return

    titulo = titulo.title()
    if titulo in stock:
        print("El libro ya está en el stock.")
    else:
        stock.append(titulo)
        print(f"Libro '{titulo}' agregado con éxito.")

def mostrar_stock(stock: list) -> None:
    if not stock:
        print("No hay libros en stock.")
    else:
        print("Libros en stock:")
        for i, libro in enumerate(stock, start=1):
            print(f"{i}. {libro}")

def menu():
    stock = []
    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Ver stock")
        print("3. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Use solo números.")
            continue

        match opcion:
            case 1:
                agregar_libro(stock)
            case 2:
                mostrar_stock(stock)
            case 3:
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida.")

if __name__ == "__main__":
    menu()
