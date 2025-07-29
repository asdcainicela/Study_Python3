"""
Lee 'nombres.txt'. Luego pide un nuevo nombre al usuario.
Si ya está registrado, muestra un mensaje.
Si no está, agréguelo y actualiza el archivo.
"""

ruta = "test_gpt/e5/nombres.txt"
new_name = input("agregue nuevo nombre: ").strip().capitalize()

with open(ruta, "r") as f:
    existing_names = [line.strip() for line in f.readlines()]


if new_name in existing_names:
    print("ya existe nombre")
else:
    with open(ruta, "a") as f:
        f.write(new_name + "\n")  