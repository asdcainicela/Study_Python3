import numpy as np

# De ceros con 3 filas y 4 columnas

array_ceros =np.zeros((3,4))
print(array_ceros)

# intervalos y salto
int_saltos = np.arange(2,20,6)
print(int_saltos)

# intervalos y divisiones

int_div = np.linspace(0,7,15)
print(int_div)

#valor dado
val_full = np.full((3,3),8)
print(val_full)

#Matriz identidad diagonal de unos
m_diag = np.eye(5)
print(m_diag)

# valores aleatorios entre 0 y 1
val_random = np.random.random((5,5))
print(val_random)

#vacio de 4 filas y 3 columnas
m_empty = np.empty((4,3))
print(m_empty)