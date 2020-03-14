# https://brownbears.tistory.com/296
# 상위 폴더 내 파일 참조
# coding: uft-8

import os
import sys

print(sys.path[0])
sys.path.append('../dataset')

from spiral import *
from matplotlib.pyplot import plt

x, t = spiral.load_data()
print('x.shape: ', x.shape)
print('t.shape: ', t.shape)