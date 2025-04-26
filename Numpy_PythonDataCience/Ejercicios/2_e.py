"""
 Resolver el siguiente sistema de ecuaciones, usando numpy
    x + 3y = 9
    6x + 3y = 5
"""
import numpy as np

# A
array1 = np.array([[1,3], [6,3]])

# C
array2 = np.array([[9], [5]])

#B
sol = np.linalg.solve(array1, array2) 
print(sol)

# -----------otra forma---------------
# Inversa de la matriz de coeficientes
array1_inv = np.linalg.inv(array1)

# Multiplicación de matrices
sol = np.dot(array1_inv, array2)
# o también: sol = array1_inv @ array2
print(sol)


