"""
Crea un archivo llamado 'saludo.txt' y escribe dentro la frase:
"Hola, bienvenido al curso de Python"
"""
import os

path = "test_gpt/e5/saludo.txt"

if not os.path.exists(path):
    print("Creando archivo...") 
with open(path, "w") as f:
    f.write("Hola, bienvenido al curso de Python")
    print("Texto escrito en el archivo con exito")
