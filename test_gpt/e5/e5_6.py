"""
Abre 'nombres.txt' y muestra cuántas personas hay registradas 
(cantidad de líneas).
"""
import os

path = "test_gpt/e5/nombres.txt"

if os.path.exists(path):
    with open(path, "r") as f:
        i=0
        for f_ in f:
            i+=1
        print(f"Existen {i} personas registradas")