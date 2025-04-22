Persona = {
    "nombre" : None,
    "edad" : None,
    "direccion" : None,
    "telefono" : None,
}

Persona["nombre"]=input("Ingrese su nombre: ")
Persona["edad"] = input("ingrese edad: ")
Persona["direccion"] = input("Ingrese su dirección: ")
Persona["telefono"] = input("Ingrese su telefono: ")

print(f"{Persona["nombre"]}, tiene {Persona['edad']} y vive en {Persona["direccion"]} y su telefono es {Persona["telefono"]}")