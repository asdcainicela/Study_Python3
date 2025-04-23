class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return f"{self.marca} {self.modelo} esta arrancando"
    
class coche(vehiculo):
    def acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando" 
    
class motocicleta(vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} esta haciendo un caballito"
    
cochee = coche("Toyota", "Camry")
motocicletaa = motocicleta("Harley-Davidson", "Sportster")

print(f"Coche marca y modelo: {cochee.marca}, {cochee.modelo}")
print(f"Motocicleta marca y modelo: {motocicletaa.marca}, {motocicletaa.modelo}")

print(cochee.acelerar())
print(motocicletaa.arrancar())

print(cochee.arrancar())
print(motocicletaa.arrancar())