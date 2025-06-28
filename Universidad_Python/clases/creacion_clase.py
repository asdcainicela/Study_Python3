class Persona:
    def inicializamos_persona(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def mostrar_persona(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}")

def main():
    print("Bienvenido al sistema de gestión de personas")
    persona1 = Persona()
    persona1.inicializamos_persona("Layla", "Acosta", 30)
    persona2 = Persona()
    persona2.inicializamos_persona("Ian", "Sanchez", 25)
    persona1.mostrar_persona()
    persona2.mostrar_persona()

if __name__== "__main__":
    main()