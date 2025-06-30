import numpy as np

x = np.array([1, 2, 3, 4, 5]) # one dimensional array

x_y = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]) # two dimensional array

print(x)
print(x_y)
print()

# showing the array size
print(x.shape)
print(x_y.shape)
print()

# showing the array dimensions
print(x.ndim)
print(x_y.ndim)
print()

# showing the amount of elements
print(x.size)
print(x_y.size)
print()

# showing the data type
print(x.dtype)
print(x_y.dtype)
print()