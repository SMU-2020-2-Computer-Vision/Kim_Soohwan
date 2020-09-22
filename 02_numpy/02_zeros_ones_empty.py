import numpy as np

# Create zeros
a = np.zeros((2, 3))
print(a)    # [[0. 0. 0.]
            #  [0. 0. 0.]]

# Create Ones
b = np.ones((2, 3, 4), dtype=np.int16)
print(b)    #[[[1 1 1 1]
            #  [1 1 1 1]
            #  [1 1 1 1]]
            #
            #  [[1 1 1 1]
            #   [1 1 1 1]
            #   [1 1 1 1]]]

# Create a random array
c = np.empty((2, 3))
print(c)    # [[0.00000000e+000  0.00000000e+000  0.00000000e+000]
            #  [-1.62971049e-311  0.00000000e+000  0.00000000e+000]]