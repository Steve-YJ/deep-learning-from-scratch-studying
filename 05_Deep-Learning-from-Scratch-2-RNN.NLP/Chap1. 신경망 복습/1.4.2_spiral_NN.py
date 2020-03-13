import sys
sys.path.append('C:\\Users\\Lee\\Documents\\steve-home\\05_Deep-Learning-from-Scratch-2-RNN.NLP')
from dataset import spiral
from matplotlib.pyplot import plt

x, t = spiral.load_data()
print('x.shape: ', x.shape)
print('t.shape: ', t.shape)