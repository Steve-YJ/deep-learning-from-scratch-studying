# test VS python path

import os
print('current directory')
print(os.getcwd())

print(1*2)
print(2**3)



# add Line

import numpy as np
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
# print(a)
# print(a.shape)
# print(b.shape)
print(a+b)


import sys
sys.path.append('..')
# import spiral as spiral
from dataset import spiral

x, t = spiral.load_data()
print(x.shape)
print(t.shape)
print("Error Handled!")