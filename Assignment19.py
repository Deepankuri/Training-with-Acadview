#Question1

import numpy as np
a = np.array(np.random.rand(10, 1))
print(a)
mean = a.mean()
print("The mean is")
print(mean)

#Question2

import numpy as np
a = np.array(np.random.rand(20, 1))
print(a)
print('the variance is')
print(a.var())
print('the std dev is')
print(a.std())

#Question3

import numpy as np
a = np.array(np.random.rand(10, 20))
print(a)
b = np.array(np.random.rand(20, 25))
print(b)
c = np.outer(b, a)
print('the matrix mult is')
print(c)
print('the sum of all the elements is')
print(c.sum())

#Question4

import numpy as np
import math

a = np.array(np.random.rand(10,1))
print(a)
i = 0
y = []
while i < len(a):
    x = 1 / (1 + math.exp(-a[i]))
    i += 1
    y.append(x)
print(y)

