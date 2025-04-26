import numpy as np

# Arrays de ejemplos
array1 = np.random.random((4,4))
array2 = np.random.random((4,4))
print(array1)
print(array2)
# Suma
suma = array1+array2
print(suma)

# otra forma de suma
array3 = np.add(array1, array2)
print(array3)

# resta
array3 = array1-array2
print(array3)

# multiplicaciones
array3 = np.multiply(array1, array2)
print(array3)

#division
array3 = array1/array2
print(array3)
array3 = np.divide(array1, array2)
print(array3)

print("------------------------")
# exponencial
array_exp= np.exp(array1)
print(array_exp)

# otros
np.cos(array3)
np.sin(array3)

print(np.sign(array1))
print(np.log(array1))
print(array1.dot( array2))

#Comparación

print(array1 == array2)
print(array1 < 0.5 )