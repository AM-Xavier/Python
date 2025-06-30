import numpy as np

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

a1 = np.array(l1)
a2 = np.array(l2)


# Multiplication
print(l1 * 5) # this will create 5 equal lists
print(a1 * 5) # this will multiply each value inside it by 5
print()

# Division
# print(l1 / 2) # this will create an error
print(a1 / 2)
print()

# Addition
print(l1 + l2) # this will concatenate both lists
print(a1 + a2) # this will sum each value
print()

# Subtraction
# print(l1 - l2) # this will also create an error
print(a1 - a2)
print()

# Adding up into different lists
a3 = np.array([1, 2, 3])
a4 = np.array([[1], [2]])

print(a3 + a4) # this will generate a new 2d list by adding up the first list,
               # into the other two
print()

# Different mathematical operators
x = np.array([[5, 10, 15, 20], [2, 4, 6, 8]])

print(np.sqrt(x)) # Square root
print()
print(np.sin(x)) # Sine
print()
print(np.cos(x)) # Cosine
print()
print(np.tan(x)) # Tangent
print()
print(np.exp(x)) # Exponential
print()
print(np.log(x)) # Logarithm
print()
print(np.log2(x)) # Logarithm base 2
print()
print(np.log10(x)) # Logarithm base 10
print()