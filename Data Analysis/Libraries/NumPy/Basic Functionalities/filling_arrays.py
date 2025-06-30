import numpy as np

x = np.full((3, 2, 2), 7.5) # ((nº arrays, nº columns, nº rows), nº to fill it with)
y = np.zeros((1, 2, 2))
z = np.ones((1, 3, 3))

a = np.empty((1,2,3)) # this one allocates space in memory without initializing the values

x_values = np.arange(0, 20, 2) # (nº it begins, nº it ends, step value)
y_values = np.linspace(0, 20, 5) # (nº it begins, nº it ends, value distribution)


print(x)
print()

print(y)
print()

print(z)
print()

print(a)
print()

print(x_values)
print()

print(y_values)