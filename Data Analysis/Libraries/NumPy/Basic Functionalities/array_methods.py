import numpy as np

a = np.array([1, 2, 3])

# Adding numbers to the end of a list
a = np.append(a, [7, 8, 9])
print(a)
print()

# Inserting numbers into a list
a = np.insert(a, 3, [4, 5, 6]) # (list, position, list to insert)
print(a)
print()

# Deleting numbers, rows or columns, from a list
b = np.array([[1, 2, 3], [4, 5, 6]])
print(np.delete(b, 1)) # by only providing the list and index, it will only delete the index
print()
print(np.delete(b, 0, 0)) # by providing the list, index and axis, it will either delete the row or the column
print()
print(np.delete(b, 1, 1)) # by specifying the axis, it will delete the column