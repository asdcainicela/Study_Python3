class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# crear una instancia de la clase Persona
persona1= Persona("Jean", 30)

# llamar al metodo saludar
persona1.saludar()

# Crear otra instancia de la clase persona

persona2 = Persona("Maria", 19)
persona2.saludar()