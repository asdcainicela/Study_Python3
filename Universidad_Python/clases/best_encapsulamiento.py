class Carro:
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        
    def conducir(self):
        return f"El {self._color} {self._marca} {self._modelo} está conduciendo."
    
    # Marca property and setter
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Modelo property and setter
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    # Color property and setter
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    
def setup():
    global carro1
    carro1 = Carro("Toyota", "Corolla", "Rojo")
    print(carro1.conducir())
    carro1.marca = "Honda"
    carro1.modelo = "Civic"
    carro1.color = "Azul"
    print(carro1.conducir())


if __name__ == "__main__":
    setup()
    