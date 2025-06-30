import numpy as np

a = np.array([[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]])

# Reshaping lists
print(a.shape) # Out: (rows, columns)
print()
print(a.reshape((5, 4)))
print()
print(a.reshape((20,))) # not specifying how many columns, will create a 1d list
print()
print(a.reshape((2, 2, 5))) # (2 collections, 2 lists, 5 elements)
print()
print(a.reshape((2, 5, 2))) # (2 collections, 5 lists, 2 elements)
print()
print(a.reshape((5, 2, 2))) # (5 collections, 2 lists, 2 elements)
print()

# Flattening lists
print(a.flatten()) # returns a flatten copy of the list
print()
print(a.ravel()) # returns a flatten view of the list
print()

a_flat = a.flatten() # it creates a copy of the list, not a new list
a_flat[1] = 25
print(a_flat)
print()
print(a) # when printing the original list, it will remain the same
print()

a_ravel = a.ravel() # it won't create a copy, it actually changes the list
a_ravel[1] = 25
print(a_ravel)
print()
print(a) # the 25 appears here also, it changed the list
print()

# Swapping columns in rows, and vice versa
print(a.transpose())
print()
print(a.T) # it can also be done with only a capital T
print()
print(a.swapaxes(0, 1)) # it works the same way as transpose, 
                        # but you can utilize it to change specific axis in multimensional lists
print()