# https://brownbears.tistory.com/296
# 상위 폴더 내 파일 참조
# coding: uft-8

import os
import sys
from matplotlib import pyplot as plt

print('current working directory: ', sys.path[0])
sys.path.append('..')
sys.path.append(r"C:\Users\Lee\Documents\steve-home\05_Deep-Learning-from-Scratch-2-RNN.NLP\dataset")

# from spiral import *  # from ... import ...구문만 사용하면 Error 발생
# from ../dataset import spiral # 마찬가지 Error
# import dataset.spiral as spiral
from dataset.spiral import *


import spiral

x, t = spiral.load_data()
print('x.shape: ', x.shape)
print('t.shape: ', t.shape)

print('hello world') 