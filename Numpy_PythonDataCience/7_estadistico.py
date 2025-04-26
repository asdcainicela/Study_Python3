import numpy as np 

def crear_array(fila, columna):
    array = np.random.random((fila, columna))
    return array

array1 =  crear_array(5,5)
print(array1)

print(array1.sum()) # Suma
print(array1.min()) # minimo
print(array1.max()) # maximo

print(array1.max(axis=0)) # maximo por columnas

#suma acumulada
print(array1.cumsum(axis= 1))

#media
print(np.mean(array1))
#mediana
print(np.median(array1))

#correlacion
print(np.corrcoef(array1))

# desviacion
print(np.std(array1))