import torch
from torch import autograd, optim
import torch.nn as nn
import torch.nn.functional as F

input_size = 9
hidden_size = 3
batch_size = 5
output_size = 9

# target = autograd.variable(batch_size * torch.Tensor([1, 0, 0, 0, 0, 0, 0, 0, 0]))
# input = autograd.Variable(torch.rand(batch_size, input_size) - 0.5)

target = autograd.Variable((torch.Tensor(batch_size) * output_size).long())
input_tensor = autograd.Variable(torch.randn(batch_size, input_size))


class Net(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Net, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.tanh(x)
        x = self.layer2(x)
        x = F.relu(x)
        return x


net = Net(input_size, hidden_size, output_size)
opt = optim.Adam(params=net.parameters())

for epoch in range(5000):
    out = net(input_tensor)
    _, pred = out.max(1)

    print('target:', target.view(1, -1)[0])
    print('pred:', pred.view(1, -1)[0])
    loss = F.nll_loss(out, target)
    print(loss)
    print()

    net.zero_grad()
    loss.backward()
    opt.step()
