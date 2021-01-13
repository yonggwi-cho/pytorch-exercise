import torch
import numpy as np

x = np.array([[1,2],[3,4.]])
y = torch.from_numpy(x)
print(y)

print(x.dtype,y.dtype)

z = y.numpy()
print(z)
