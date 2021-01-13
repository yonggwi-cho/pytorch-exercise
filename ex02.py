import torch

a = torch.tensor([[1,2],[3,4]])

b = a.numpy()
print(b)

c = torch.from_numpy(b)
print(c)


a = torch.tensor([[1,2,3],[4,5,6]])

print(a)

print(a[0,1])

print(a[1:2,:2])

print(a[:,[0,2]])


