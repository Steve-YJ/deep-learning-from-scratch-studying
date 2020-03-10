import numpy as np

class MatMul:
    def __init__(self, W):
        self.params = [W]
        self.grads = [np.zeros_like(W)]
        self.x = None
    
    def forward(self, x):
        W, = self.params
        out = np.dot(x, W)
        self.x = x
        return out


    def backward(self, dout):
        W, = self.params
        dx = np.dot(dout, W.T)
        dW = np.dot(self.x.T, dout)
        self.grads[0][...] = dW
        return dx


class Sigmoid:
    def __init__(self):  # Sigmoid 함수의 경우 학습해야 할 파라미터가 따로 없다.
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        self.x = x
        out = 1 / (1 + np.exp(-x))
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out  # dout * (1-y) * y
        return dx


class Affine:
    def __init__(self, W, b):
        self.params = [W, b]
        self.grads = [zeros_like(W), zeros_like(b)]
        self.x = None

    def forward(self, x):
        W, b = self.params
        out = np.dot(x, W) + b
        self.x = x
        return out


    def backward(self, dout):
        W, b = self.params
        dx = np.dot(dout, W.T)
        dW = np.dot(self.x.T, dout)
        db = np.sum(dout, axis=0)

        self.grads[0][...] = dW
        self.grads[1][...] = db
        return dx   
