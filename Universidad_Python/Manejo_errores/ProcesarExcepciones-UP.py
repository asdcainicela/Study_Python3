class Division:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def dividir(self):
        try:
            return self.numerador / self.denominador
        except Exception as e:
            return f'Error: {e}' 
# Manejo de excepciones en Python
resultado = None 
resultado = Division('10',0).dividir()
print(f'Resultado: {resultado}')
print('Continuamos...')