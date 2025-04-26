import numpy as np

array_1d= np.array([1,4,3])
print(array_1d)

array_2d = np.array([(1,5,9), (1,8,7)])
print(array_2d)

array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(array_3d.shape)  # (2, 2, 2)

 
array_3d1 = np.array(
    [
        [(1.6, 5.9, 4.3), (1, 5.8, 9)],
        [(7, 5, 9.3), (7, 1.4, 3)],
        [(1.6, 5.9, 4.3), (1, 5.8, 9)]
    ], 
    dtype=float
)

print(array_3d1)
print("Shape:", array_3d1.shape)
