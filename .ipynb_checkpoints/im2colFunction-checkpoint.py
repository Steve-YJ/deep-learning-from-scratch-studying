# 이전 3장 3.5.2에서 배운 것들을 떠올려보자.
# 3.5.2 소프트맥스 함수 구현시 주의할 점
# 1차원일 때 소프트맥스와 2차원 이상일 때는 값이 다르지...!
'''
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 오버플로 대책
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y
'''

'''
# 4.2.4 배치용 크로스엔트로피 오차 구현하기
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None  # 손실
        self.y = None     # softmax의 출력
        self.t = None     # 정답 레이블(원-핫 벡터)
        
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss
    
    def backward(self, dout=1):
        batch_size = self.t.shape[0]         # ?
                                             # 정답레이블이 원-핫벡터로 이루어져 있는데
                                             # ??
        dx = (self.y - self.t) / batch_size  # backward에서 dx는 어떻게 구해지는 걸까? 20.02.05.wed pm6:00
        
        return dx
''' 
    
# common/functions.py    
# coding: utf-8
import numpy as np

def identity_function(x):
    return x

def step_function(x):
    return np.array(x > 0, dtype=np.int)  # numpy 트릭 사용
                                          # 값이 0보다 크면 True, 작으면 Fale
                                          # 
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)

def relu(x):
    return np.maximum(0, x)

def relu_grad(x):
    grad = np.zeros(x)
    grad[x>=0] = 1
    return grad

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T
    
    x = x - np.max(x)  # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))

def mean_squared_error(y, t):
    return 0.5 * np.sum*((y-t)**2)

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 훈련 데이터가 원-핫 베터라면 정답 레이블의 인덱스 반환
    if t.size == y.size:
        t = t.argmax(axis=1)
        
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

def softmax_loss(X, t):
    y = softmax(x)
    return cross_entropy_error(y, t)