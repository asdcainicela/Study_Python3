"""
Abre el archivo 'saludo.txt' y muestra su contenido línea por línea.
"""
import os

path = "test_gpt/e5/saludo.txt"
if not os.path.exists(path):
    print("el archivo no existe")
else:
    with open(path, "r") as f:
        for line in f:
            print(line.strip())
