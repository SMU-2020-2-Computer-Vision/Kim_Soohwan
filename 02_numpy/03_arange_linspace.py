import numpy as np

# Create a range with min, max, and step
a = np.arange(10, 30, 5)
print(a)    # [10 15 20 25]

b = np.arange(0, 2, 0.3)
print(b)    # [0.  0.3 0.6 0.9 1.2 1.5 1.8]

# Create a evenly spaced numbers
c = np.linspace(0, 2, 9)
print(c)    # [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.]

# Function evaluation
x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)
