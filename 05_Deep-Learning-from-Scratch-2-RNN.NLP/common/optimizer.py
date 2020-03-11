# SGD Optimizer
class SGD:
    '''
    확률적 경사하강법(Stochastic Gradient Descent)
    '''

    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for i in range(len(params)):
            params[i] -= self.lr * grads[i]