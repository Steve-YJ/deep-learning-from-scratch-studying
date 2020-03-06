# 3. Neural Networks.ipynb에서 구현했던 LeNet을 정리해서 구현한다.
# Tutorial을 따라가면서 놓쳤던 부분을 다시한번 리마인드 할 수 있도록 하자


# #1.신경망 정의하기
import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
    # 1. 신경망의 Layer를 정의한다.
        self.conv1 = nn.Conv2d(1, 6, 3)  # input image chanel, output image chanel, kernel(filter size)
        self.conv2 = nn.Conv2d(6, 16, 3)

        # Affine Operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 6 * 6, 120)  # (output_chanel_num * input_height * input_weight), size_of_output features
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    # 2. 신경망의 function을 정의한다.
    def forward(self, x):  # forward함수만 정의하고 나면, (변화도를 계산하는)backward함수는 autograd를 사용하여 자동으로 정의된다.
                           # forward함수에서는 어떠한 Tensor연산을 사용해도 된다.
        # Max pooling over a (2, 2) windows
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


# 위에서 구성한 Net class의 인스턴스 net을 정의한다.
net = Net()
# print(net)

# 모델의 학습 가능한 매개변수들은 net.tarameters()에 의해 반환된다.
params = list(net.parameters())
print('len(params): ', len(params))
# print(params)
# print(params.shape) # 'list' object has no attribute 'shape'
input = torch.randn(1, 1, 32, 32)
out = net(input)
# print(out)  # random한 input값에 대한 output 출력 확인


# #2. 손실함수(Loss Function)
output = net(input)
target = torch.randn(10)
target = target.view(1, -1)  # make it the same shape as output
criterion = nn.MSELoss()

loss = criterion(output, target)
print('loss: ', loss)
print('MSE Loss:', loss.grad_fn)
print('Linear differenciation(gradient): ', loss.grad_fn.next_functions[0][0])
print('ReLU differenciation(gradient): ', loss.grad_fn.next_functions[0][0].next_functions[0][0])

# #3. 역전파(Backpropagation)
# 오차(Error)를 역전파하기 위해서는 loss.backward()만 해주면 된다. 
net.zero_grad()  # zeroes the gradient buffers of all parameters

print('conv1.bias.grad before backward: ', net.conv1.bias.grad)
loss.backward()

print('conv1.bias.grad before backward: ', net.conv1.bias.grad)

# #4. 가중치 갱신
# W = W - eta(learning rate) * gradient

learning_rate = 0.01
for f in net.parameters():
    f.data.sub_(f.grad.data * learning_rate)

import torch.optim as optim
# Optimizer를 생성한다.
optimizer = optim.SGD(net.parameters(), lr=0.01)

# 학습 과정(training loop)에서는 다음과 같다.

optimizer.zero_grad()
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()

print("Done!! -20.02.23.Sun pm 4:00")