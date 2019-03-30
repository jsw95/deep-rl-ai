import torch
from torch import autograd

x = torch.Tensor(5, 3).uniform_(-1, 1)
y = torch.Tensor(5, 3).uniform_(-1, 1)

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.ones(2, 3, requires_grad=True)

print(w)
w.backward()
print(w)

print("Here is some more code test this fancy git plugin with")
