class Division:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def dividir(self):
        try:
            return   self.numerador / self.denominador
        except ZeroDivisionError as e:
            return f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}' 
        except TypeError as e:
            return f'TypeError - Ocurrió un error: {e} , {type(e)}' 
        except Exception as e:
            return f'Exception - Ocurrió un error: {e} , {type(e)}' 
        
# Manejo de excepciones en Python
resultado = None 
a=5
b=2
resultado = Division(a,b).dividir()


print(f'Resultado: {resultado}')
print('Continuamos...')


 


print(f'Resultado: {resultado}')
print('Continuamos...')