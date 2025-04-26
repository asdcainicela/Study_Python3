import numpy as np
import os

# Crear las carpetas necesarias
os.makedirs("Numpy_PythonDataCience/wr", exist_ok=True)

# Guardar un array 3D en formato binario .npy
np.save("Numpy_PythonDataCience/wr/mi_array", np.random.random((3, 3, 1)))

# Cargar el archivo .npy
mi_array = np.load("Numpy_PythonDataCience/wr/mi_array.npy")
print("Array cargado desde .npy:")
print(mi_array)

# Crear un array 2D
array_2d = np.array([(1, 5, 9), (1, 8, 7)])

# Guardar en archivo de texto con delimitador espacio
np.savetxt("Numpy_PythonDataCience/wr/mi_array.txt", array_2d, delimiter=" ")

# Cargar desde archivo de texto
array_2d_1 = np.loadtxt("Numpy_PythonDataCience/wr/mi_array.txt")
print("\nArray cargado desde .txt:")
print(array_2d_1)
