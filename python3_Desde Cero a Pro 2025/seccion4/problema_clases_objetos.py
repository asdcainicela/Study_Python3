class ContadorPalabras:
    def __init__(self):
        # Inicializa el contador en 0
        self.contador = 0

    def contar(self, texto):
        # Cuenta las palabras en el texto y actualiza el contador
        palabras = texto.split()
        self.contador += len(palabras)

    def obtener_contador(self):
        # Devuelve el valor actual del contador
        return self.contador

# Crea una instancia de la clase ContadorPalabras
mi_contador = ContadorPalabras()

# Utiliza el método contar para contar palabras en una cadena de texto
texto = "Este es un ejemplo de contador de palabras en Python"
mi_contador.contar(texto)

# Utiliza el método obtener_contador para obtener el resultado y mostrarlo
resultado = mi_contador.obtener_contador()
print("Número de palabras:", resultado)


