import numpy as np

# Ordenamiento 
array_1 =  np.random.randint(41, size=(10,10))
array_2 =  np.random.randint(41, size=(10,10))

array_1.sort() # ordenar
print(array_1)

array_2.sort(axis= 1)
print(array_2)