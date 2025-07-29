"""
Crea un programa con menú:
1. Registrar nuevo libro (título + autor)
2. Mostrar todos los libros registrados
3. Salir

Guarda los datos como lista de diccionarios en 'libros.json'.
"""

# este codigo no es eficiente para data grande ni mediana
"""
Crea un programa con menú:
1. Registrar nuevo libro (título + autor)
2. Mostrar todos los libros registrados
3. Salir

Guarda los datos como lista de diccionarios en 'libros.json'.
"""

# este codigo no es eficiente para data grande ni mediana
import json
import json

path = "test_gpt/e5/libros.json"

def cargar_libros():
    """Carga los libros desde el archivo JSON. Si no existe, retorna una lista vacía."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Si el archivo no existe o está corrupto, retorna lista vacía

def guardar_libros(libros):
    """Guarda la lista de libros en el archivo JSON."""
    with open(path, "w") as f:
        json.dump(libros, f, indent=4)

while True:
    print("\n--- Menú ---")
    print("1. Registrar nuevo libro")
    print("2. Mostrar todos los libros")
    print("3. Salir")
    
    opcion = input("Ingrese opción: ").strip()
    
    match opcion:
        case "1":
            libros = cargar_libros()
            
            titulo = input("Introduzca título: ").strip().title()
            autor = input("Agregue autor: ").strip().capitalize()
            
            libros.append({"titulo": titulo, "autor": autor})
            
            guardar_libros(libros)
            print(" Libro registrado correctamente.")
        
        case "2":
            libros = cargar_libros()
            if not libros:
                print("No hay libros registrados.")
            else:
                print("\n Lista de libros:")
                for libro in libros:
                    print(f"- Título: {libro['titulo']}, Autor: {libro['autor']}")
        
        case "3":
            print("Saliendo del programa...")
            break
        
        case _:
            print(" Opción inválida. Intente de nuevo.")