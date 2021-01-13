import torch

x = torch.tensor(3.)
#x = torch.tensor(3.,requires_grad=True)
w = torch.tensor(4.,requires_grad=True)
b = torch.tensor(5.,requires_grad=True)

y = w * x + b

print(y)
y.backward()

print('dy/dx:',x.grad)
print('dy/dw:',w.grad)
print('dy/db:',b.grad)


