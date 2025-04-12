

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")
elif edad >= 0:
    print("Eres un niño.")
else:
    print("Edad no válida.")
    