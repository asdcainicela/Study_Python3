import numpy as np

array1 = np.random.randint(0,15,size= 10)
print(array1)

array2 = np.random.randint(0, 15, size= (2,3))
print(array2)

#crea una imagen del array, el valor cambiadop se refleja en los dos
array_copy= array2.view()
print(array_copy)

# -- modificamos  un valor de la copia
array_copy[0,2] = 100
print(np.array_equal(array2, array_copy))
print(array_copy)

# Si hacemos una copia independiente seria
array_copy2 = np.copy(array2)
array_copy2[1,2] = 100
print(array_copy2)
print(np.array_equal(array_copy2, array2))