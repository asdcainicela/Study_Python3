"""
Lee el archivo 'palabras.txt' y reconstruye la
 lista original sin saltos de línea.
"""

path = "test_gpt/e5/palabras.txt"

lista_archivo = []
with open(path, "r") as f:
    for lines_ in f:
        lista_archivo.append(lines_.strip())
        print(lines_.strip())

print(lista_archivo)