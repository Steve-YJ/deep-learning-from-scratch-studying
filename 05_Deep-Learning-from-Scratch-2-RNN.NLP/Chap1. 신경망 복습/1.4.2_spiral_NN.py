# https://brownbears.tistory.com/296
# 상위 폴더 내 파일 참조
# coding: uft-8

import os
import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# sys.path.append('..')
'''
for p in sys.path:
    print(p)
    print('=='*20)

print('line-11: len(sys.path)', len(sys.path))
print(sys.path)

# Trial & Errors -20.03.13.Fri

'''
os.chdir('C:\Users\Lee\Documents\steve-home\05_Deep-Learning-from-Scratch-2-RNN.NLP')
print(os.getcwd())
print(os.path.abspath("__file__"))

from dataset import spiral
from matplotlib.pyplot import plt

x, t = spiral.load_data()
print('x.shape: ', x.shape)
print('t.shape: ', t.shape)