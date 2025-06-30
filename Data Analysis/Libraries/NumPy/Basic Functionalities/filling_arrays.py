import numpy as np

x = np.full((3, 2, 2), 7.5) # ((nº arrays, nº columns, nº rows), nº to fill it with)
print(x)
print()

y = np.zeros((1, 2, 2))
print(y)
print()

z = np.ones((1, 3, 3))
print(z)
print()

a = np.empty((1,2,3)) # this one allocates space in memory without initializing the values
print(a)
print()

x_values = np.arange(0, 20, 2) # (nº it begins, nº it ends, step value)
print(x_values)
print()

y_values = np.linspace(0, 20, 5) # (nº it begins, nº it ends, value distribution)
print(y_values)
print()

# special values
print(np.nan) # nan stands for not a number value
print(np.inf)
print()

print(np.sqrt(-1)) # returns nan
print(np.array([10]) /0 ) # returns inf