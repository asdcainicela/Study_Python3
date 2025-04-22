personas = {
    "persona1":{
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid"
    },
    "persona2":{
        "nombre": "Maria",
        "edad": 28,
        "ciudad": "Barcelona"
    },
    "persona3":{
        "nombre": "Carlos",
        "edad": 35,
        "ciudad": "Valencia"
    }
    
}

datos = personas["persona1"]
datos2 = personas["persona2"]
datos3 = personas["persona3"]
 
print(datos["nombre"])
print(datos2["edad"])
print(datos3["ciudad"])





persona1  = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None,
}

persona1["nombre"]= input("Introduce un nombre:")
persona1["edad"]= input("Introduce tu edad:")
persona1["direccion"]= input("Introduce tu direccion:")
persona1["telefono"]= input("Introduce tu telefono:")

print(persona1["nombre"], "tiene", persona1["edad"], "años, vive en", persona1["direccion"], "y su numero de telefono es", persona1["telefono"])