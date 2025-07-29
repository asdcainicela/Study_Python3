"""
Crea una lista de 5 palabras y guarda cada una en una línea del
 archivo 'palabras.txt'.
"""

path = "test_gpt/e5/palabras.txt"

lista_fruta = ["manaza", "fresa", "platano", "naranja", "zandia"]
with open(path, "w") as f:
    for lista in lista_fruta:
        f.write(lista+"\n")
