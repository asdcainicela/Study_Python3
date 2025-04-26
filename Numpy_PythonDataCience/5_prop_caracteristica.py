import numpy as np

array_3d1 = np.array(
    [
        [(1.6, 5.9, 4.3), (1, 5.8, 9)],
        [(7, 5, 9.3), (7, 1.4, 3)],
        [(1.6, 5.9, 4.3), (1, 5.8, 9)]
    ], 
    dtype=float
)

#Dimension y forma
print(array_3d1.shape)

# Longitud
print(len(array_3d1))

# Numero de dimensiones
print(array_3d1.ndim)

# Tamaño o numero de elementos
print(array_3d1.size)

#Saber el tipo del array
print(array_3d1.dtype.name)

# Convertir de un tipo a otro
array_3d1.astype(int)
print(array_3d1.dtype.name)

# Ayuda en np
np.info(np.ndarray.dtype)