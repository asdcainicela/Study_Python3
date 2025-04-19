"""
 deben crear un programa en Python que verifique 
si una palabra ingresada por el usuario está presente en una tupla predefinida de palabras.
 El programa debe informar al usuario si la palabra está o no en la tupla.

Instrucciones: 
    Crear una tupla llamada palabras que contenga varias palabras, por ejemplo, "manzana", "banana" y "cereza". 
    Solicitar al usuario que ingrese una palabra mediante la función input(). La palabra ingresada será almacenada
      en la variable palabra_buscar. 
    Utilizar una estructura condicional (un if y un else) para verificar si palabra_buscar está presente en la tupla palabras. 
    Si la palabra está en la tupla, imprimir "La palabra está en la tupla." 
    Si la palabra no está en la tupla, imprimir "La palabra no está en la tupla."

"""

tupla_1 = ("manza", "banana", " cereza")
palabra_buscar = input("ingrese una palabra: ")

for x in tupla_1:
    if palabra_buscar == x:
        print(f"La palabra {palabra_buscar} está en la tupla: ", x)
    else:
        print("La palabra no está en la tupla: ", x)