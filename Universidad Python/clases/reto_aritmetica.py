class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    def sumar(self):
        return self.operando1 + self.operando2
    def restar(self):
        return self.operando1 - self.operando2  
    def multiplicar(self):
        return self.operando1 * self.operando2
    def dividir(self):
        if self.operando2 == 0:
            return "Error: División por cero"
        return self.operando1 / self.operando2
    def mostrar_resultados(self):
        print(f"Operando 1: {self.operando1}")
        print(f"Operando 2: {self.operando2}")
        print(f"Suma: {self.sumar()}")
        print(f"Resta: {self.restar()}")
        print(f"Multiplicación: {self.multiplicar()}")
        print(f"División: {self.dividir()}")
def main():
    print("Bienvenido al sistema de operaciones aritméticas")
    operando1 = float(input("Ingrese el primer operando: "))
    operando2 = float(input("Ingrese el segundo operando: "))
    
    aritmetica = Aritmetica(operando1, operando2)
    aritmetica.mostrar_resultados()

if __name__ == "__main__":
    main()