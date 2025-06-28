
class Division: 
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    def dividir(self):
        try:
            return self.numerador/self.denominador
        except Exception as e:
            return f'Ocurrió un error: {e}'

def main():
    val = Division(10, 0)
    val2 = Division(10, 2)
    print(val2.dividir())  # 5.0
    print(val.dividir())  # Ocurrió un error: division by zero

if __name__ == "__main__":
    main()
