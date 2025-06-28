class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
def main():
    print("Bienvenido al sistema de gestión de personas")
    persona1 = Persona("Layla", 30)
    persona2 = Persona("Ian", 25)
    print(persona1.saludar())
    print(persona2.saludar())

if __name__ == "__main__":
    main()
