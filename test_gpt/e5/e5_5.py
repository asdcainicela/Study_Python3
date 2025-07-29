"""
Pide al usuario escribir nombres de personas hasta que diga "fin".
Guarda todos los nombres en 'nombres.txt', uno por línea.
"""
path = "test_gpt/e5/nombres.txt"
lista_name = []
while True:
    user_ = input("Introduzca nombre del nuevo usuario: ").strip()
    if user_.lower() == "fin":
        break
    lista_name.append(user_.capitalize())

with open(path, "w") as f:
    for nombre in lista_name:
        f.write(nombre+"\n")
