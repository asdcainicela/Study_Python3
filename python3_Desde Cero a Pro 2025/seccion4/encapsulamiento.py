#Encapsulamiento
from types import prepare_class


class encap:
    
    def __init__(self):
        self.__numero = 0

    def operacion(self):
        print(self.__numero + 20)

    def resultado(self):
        return self.__numero

ejemplo = encap()
ejemplo.operacion()
ejemplo.__numero = 100
print(ejemplo.resultado())