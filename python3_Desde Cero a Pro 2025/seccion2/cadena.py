nombre = "Marco"
apellido =  "Mendoza"
frace = " Hola esto es una frase"

longitud = len(frace)
print(longitud)

print(apellido[4])

palabras = frace.split() # separa 
print(palabras)

mayuscula =  apellido.upper()
print(mayuscula)

minuscula = nombre.lower()
print(minuscula)

message = "Hello, Mundo"
print(message)

change = message.replace("Mundo", "Pablo")
print(change)

for x in apellido:
    print(x)