import sys
sys.path.append('..')

from dataset import spiral
x, t = spiral.load_data()
print('x.shape: ', x.shape)
print('t.shape: ', t.shape)