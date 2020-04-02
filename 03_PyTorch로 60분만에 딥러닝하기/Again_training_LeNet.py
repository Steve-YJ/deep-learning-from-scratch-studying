import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)
        
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))  # max_pooling over 2window
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_features(self, x):
        size=  x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


'''
net = Net()
print('net: ', net)

# 학습가능한 매개변수들은 net.parameters()에 의해 반환된다.
params = list(net.parameters())
print(len(params))
print(params[0].size())  # conv1's weight
                         # torch.size([6, 1, 3, 3])  <- why?
                         # feature map 6장 filter(kernel) size 3?
                         # 6 * 3 * 3

# print(params[0].shape)

# 32x32 이미지를 입력으로 학습을 시켜보자
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)

net.zero_grad()
out.backward(torch.randn(1, 10))  # forward함수만 정의하고 나면, 
                                  # (변화도를 계산하는) backward함수는 autograd를 사용하여 자동으로 정의

# 손실함수
output = net(input)
target = torch.randn(10)
target = target.view(1, -1)
criterion = nn.MSELoss()

loss = criterion(output, target)
print(loss)

net.zero_grad()
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)

loss.backward()

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

# 가중치 갱신
learning_rate = 0.01
for f in net.parameters():
    f.data.sub_(f.grad.data * learning_rate)
'''


import torch.optim as optim

net = Net()
input = torch.randn(1, 1, 32, 32)
output = net(input)
target = torch.randn(10)
target = target.view(1, -1)
criterion = nn.MSELoss()

optimizer = optim.SGD(net.parameters(), lr=0.01)
optimizer.zero_grad()

loss = criterion(output, target)
loss.backward()
optimizer.step()
