import numpy as np

a1 = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]])

a2 = np.array([[11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20]])


# Concatenating lists
a = np.concatenate((a1, a2), axis=0) # the list format will change depending on the axis specified
print(a)
print()

a = np.concatenate((a1, a2), axis=1)
print(a)
print()

# Stacking lists
a = np.stack((a1, a2)) # the difference between the two is that stacking results in a new dimension
print(a)
print()

a = np.vstack((a1, a2)) # vertical stacking, works in the same way as concataneting with axis 0
print(a)
print()

a = np.hstack((a1, a2)) # horizontal stacking, works in the same way as concataneting with axis 1
print(a)
print()

# Splitting
a = np.concatenate((a1, a2), axis=0)

b = np.split(a, 2, axis=0) # splitting in two rows
print(b)
print()

b = np.split(a, 4, axis=0) # splitting in four rows
print(b)
print()