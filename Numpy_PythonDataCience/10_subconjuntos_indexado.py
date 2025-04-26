import numpy as np
 
array_1 =  np.random.randint(41, size=(10,10)) 


#seleccionamos elemento de la fila 2, columna 3
print(array_1[2,3] )

# Slicing
print(array_1[1:4])

print(array_1[1:4,2])

print(array_1[::,-1])