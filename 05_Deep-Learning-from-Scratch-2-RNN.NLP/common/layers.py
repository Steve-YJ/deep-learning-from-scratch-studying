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
        self.x = None

    def forward(self, x):
        self.x = x
        out = 1 / (1 + np.exp(-x))
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out  # dout * (1-y) * y
        return dx

# Softmax 함수 정의
# 2차원일 때와 1차원일 때 각각 구하는 방법이 다름에 주의하자
def Softmax:
    if x.ndim == 2:  # 2차원일 경우
        x = x - x.max(axis=1, keepdim=True)
        x = np.exp(x)
        x /= x.sum(axis=1, keepdim=True)

    elif x.ndim == 1:
        x = x - x.max(x)
        x = np.exp(x)
        x = x / x.sum(axis=1, keepdim=True)
    return x

# Cross-Entropy 함수 정의
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    # 정답 데이터가 원-핫 벡터일 경우 정답 레이블 인덱스로 변환
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]

    return -np.sum(np.log(y[np.arrange(batch_size), t] + 1e-7)) / batch_size  # y[np.arrage(batch_size), t]: 각 데이터의 정답 레이블에 대한
                                                         # 신경망의 출력값을 출력

# Softmax 계층과 Softmax with Loss 계층 구현하기
# 1. Softmax 계층 구현하기
class Softmax:
    def __init__(self):
        self.params, self.grads = [], []
        self.out = None

    def forward(self, x):
        self.out = Softmax(x)
        return self.out

    def backward(self, dout):  # Q1. backward는 어떻게 해서 이와 같이 구할 수 있는건가?
        dx = self.out * dout
        sumdx = np.sum(dx, axis=1, keepdims=True)
        dx -= self.out * sumdx
        return dx

# 2. Softmax with Loss
class SoftmaxWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.y = None  # softmax의 출력
        self.t = None  # 정답 레이블

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)

        # 정답 레이블이 원-핫벡터일 경우 정답의 인덱스로 변환
        if self.t.size == self.y.size:
            self.t = self.t.argmax(axis=1)

        loss = cross_entropy_error(self.y, self.t)
        return loss




class Affine:
    def __init__(self, W, b):
        self.params = [W, b]
        self.grads = [np.zeros_like(W), np.zeros_like(b)]
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



