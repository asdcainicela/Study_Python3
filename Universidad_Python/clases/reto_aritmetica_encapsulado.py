class Aritmetica:
    def __init__(self, operando1, operando2):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        return self._operando1 + self._operando2
    def restar(self):
        return self._operando1 - self._operando2
    def multiplicar(self):
        return self._operando1 * self._operando2
    def dividir(self):
        try:
            return float(self._operando1) / float(self._operando2)
        except Exception as e:
            return f"Error: División por cero no permitida. {e}"
    
    def mostrar_resultados(self):
        print(f"Operando 1: {self._operando1}")
        print(f"Operando 2: {self._operando2}")
        print(f"Suma: {self.sumar()}")
        print(f"Resta: {self.restar()}")
        print(f"Multiplicación: {self.multiplicar()}")
        print(f"División: {self.dividir()}")
    @property
    def operando1(self):
        return self._operando1
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1
    @property
    def operando2(self):
        return self._operando2
    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2

def main():
    print('*** Ejemplo Clase Aritmética ***')
    value1 = 2
    value2 = 3
    aritmetica = Aritmetica(value1, value2)
    aritmetica.mostrar_resultados()
    aritmetica.operando1 = 10
    aritmetica.operando2 = 0
    print("\nDespués de modificar los operandos:")
    aritmetica.mostrar_resultados()

    aritmetica2 = Aritmetica(operando2=0, operando1=16)
    print("\nSegundo objeto:")
    aritmetica2.mostrar_resultados()
    aritmetica2.operando2 = 4
    print("\nDespués de modificar el segundo operando:")
    aritmetica2.mostrar_resultados()


if __name__ == "__main__":
    main()