import numpy as np


array_1 =  np.random.randint(41, size=(5,5))
array_2 =  np.random.randint(41, size=(5,5))
# Transpuesta
array_t= np.transpose(array_1)
print(array_t)

# Aplanar array
array_1.ravel()
print(array_1)

# cambiamos la forma, peo no los datos

array_1.reshape(5,5)
# otra forma
array = np.random.randint(10, size=(4,2))
array.resize(2,8)

# Add o eliminar elementos

np.append(array, 35)

np.insert(array, 2, 29)
np.delete(array, [2])

# combinado
array_combinado = np.concatenate((array_1, array_t), axis=0 )
print(array_combinado)
# otra forma
array_combinado = np.r_[array_1, array_t]

# combinado horizontal
array_combinado = np.hstack((array_1, array_t))
# otra forma
np.column_stack((array_1, array_2))

np.c_[array_1, array_2]

# splitting, corte array verticalmente
#np.vsplit(array_2,2)

#np.hsplit(array_2,2)