class Persona:
    contador_persona = 0
    def __init__(self, nombre, apellido):
        Persona.contador_persona += 1
        self.__id = Persona.contador_persona
        self._nombre=nombre
        self._apellido=apellido
    
    @property
    def id(self):
        return self.__id  # Solo lectura (sin setter)
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

def main():
    personas = []
    for i in range(10):
        nombre = f"Nombre{i+1}"
        apellido = f"Apellido{i+1}"
        persona = Persona(nombre, apellido)
        personas.append(persona)

    for persona in personas:
        print(f"ID: {persona.id}, Nombre completo: {persona.nombre} {persona.apellido}")

    print(f'Contador de personas: {Persona.contador_persona}')

if __name__ == '__main__':
    main()