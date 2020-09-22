import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)         # [[1, 2, 3],
                 #  [4, 5, 6]])

print(a.shape)   # (2, 3)

# Get flatten 1-D arrays from N-D arrays 
b = a.ravel()    
print(b)         # [1 2 3 4 5 6]

# Get reshaped arrays
c = a.reshape(3, 2)
print(c)         # [[1 2]
                 #  [3 4]
                 #  [5 6]]

# Get transposed arrays
d = a.T
print(d)         # [[1, 4],
                 #  [2, 5],
                 #  [3, 6]])

# The orriginal array is untouched
print(a.shape)   # (2, 3)