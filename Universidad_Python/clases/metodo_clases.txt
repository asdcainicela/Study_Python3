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

    @staticmethod
    def get_contador_personas_estatico():
        print('Método estático')
        return Persona.contador_persona

    @classmethod
    def get_contador_personas_clase(cls):
        print('Método de clase')
        return cls.contador_persona


def main():
    personas = []
    for i in range(2):
        nombre = f"Nombre{i+1}"
        apellido = f"Apellido{i+1}"
        persona = Persona(nombre, apellido)
        personas.append(persona)

    for persona in personas:
        print(f"ID: {persona.id}, Nombre completo: {persona.nombre} {persona.apellido}")
 
    # Imprimir el valor del contador de objetos de personas
    print(f'*** ----------------------- ***')
    print(f'Contador objetos Persona: {Persona.contador_persona}')
    print(f'Contador objetos Persona (persona1): {personas[1].contador_persona}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')

if __name__ == '__main__':
    main()