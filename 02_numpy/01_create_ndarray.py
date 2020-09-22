import numpy as np

# Create an 1-D array
a = np.array([2, 3, 4])
print(a)                # [2 3 4]
print(type(a))          # <class 'numpy.ndarray'>
print(a.ndim)           # 1
print(a.shape)          # (3,)
print(a.size)           # 3
print(a.itemsize)       # 4
print(a.nbytes)         # 12 = 3x4
print(a.dtype)          # int32

# Create an 1-D array with a specific data type
b = np.array((1.2, 3.5, 5.1, 4.7))
print(b)                # [1.2 3.5 5.1 4.7]
print(type(b))          # <class 'numpy.ndarray'>
print(b.ndim)           # 1
print(b.shape)          # (4,)
print(b.size)           # 4
print(b.itemsize)       # 8
print(b.nbytes)         # 32 = 4x8
print(b.dtype)          # float64

# Create a 2-D array
c = np.array([[1, 2, 3], [4, 5, 6]], dtype='float32')
print(c)                # [[1. 2. 3.]
                        # [4. 5. 6.]]
print(type(c))          # <class 'numpy.ndarray'>
print(c.ndim)           # 2
print(c.shape)          # (2, 3)
print(c.size)           # 6 = 2x3
print(c.itemsize)       # 4
print(c.nbytes)         # 24 = 6x4
print(c.dtype)          # float32

# Create a 3-D array
d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
print(d)                # [[[ 1  2  3  4]
                        #  [ 5  6  7  8]
                        #  [ 9 10 11 12]]]
print(type(d))          # <class 'numpy.ndarray'>
print(d.ndim)           # 3
print(d.shape)          # (1, 3, 4)
print(d.size)           # 12 = 3x4
print(d.itemsize)       # 4
print(d.nbytes)         # 48 = 12x4
print(d.dtype)          # int32
