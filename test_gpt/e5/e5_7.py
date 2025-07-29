"""
Cada vez que ejecutes el script, pide un nuevo nombre y agrégalo
al final de 'nombres.txt' sin borrar lo anterior.
"""
ruta = "test_gpt/e5/nombres.txt"
with open(ruta, "a") as f:
    nombre= input("agrega nuevo nombre: ").strip().capitalize()
    f.write(nombre)