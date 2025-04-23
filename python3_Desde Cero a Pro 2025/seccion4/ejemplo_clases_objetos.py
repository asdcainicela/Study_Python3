 
    
class calculadora:
    def __init__(self, numero):
        self.resultado = numero
    
    def sumar(self, numero):
        self.resultado += numero

    def restar(self, numero):
        self.resultado -= numero

    def multiplicar(self, numero):
        self.resultado *= numero
    
    def division(self, numero):
        if numero !=0 :
            self.resultado /= numero
        else:
            print("error: no se puede divivir")

calculo = calculadora(0)

calculo.sumar(5)
calculo.multiplicar(4)
calculo.restar(10)
calculo.division(2)
resultado = calculo.resultado
print(resultado)