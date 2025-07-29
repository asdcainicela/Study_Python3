"""
Pide al usuario su nombre y edad, y guarda el diccionario {'nombre': ..., 'edad': ...}
en 'usuarios.json'. Cada ejecución debe agregar un nuevo usuario.
"""

import json

path = "test_gpt/e5/usuarios.json"

try:
    with open(path, "r") as f:
        usuarios = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    usuarios = []

name = input("Introduzca nombre: ").strip().capitalize()
edad = int(input("Agregue edad: "))
usuarios.append({"nombre": name, "edad": edad})

with open(path, "w") as f:
    json.dump(usuarios, f, indent=4)