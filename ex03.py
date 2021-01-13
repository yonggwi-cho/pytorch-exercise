import torch

a = torch.tensor([1,2,3])
b = torch.tensor([4,5,6])

c = torch.tensor([[6,5,4],[3,2,1]])

print(a+3)

print(a+b)

print(c+2)
print(c+a)                 
print(c+c)

a = torch.tensor([[1,2,3],[4,5,6]],dtype=torch.float64)

m = torch.mean(a)
print(m.item())

m = a.mean()
print(m.item())

print(a.mean(0))

print(torch.sum(a).item())
print(torch.max(a).item())
print(torch.min(a).item())

t2 = torch.tensor([1.,2,3,4])
print(t2)

t3 = torch.tensor([[5.,6],[7,8],[9,10]])
print(t3)

t4 = torch.tensor([[[11,12,13],
                   [13,14,15]],
                  [[15,16,17],
                   [17,18,19]]])
print(t4)

print(t2.shape)
print(t3.shape)
print(t4.shape)

