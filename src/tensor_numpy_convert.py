import torch
import numpy as np

a = [[1,2], [3,4]]

a = torch.tensor(a)

print(a) # 张量 作为 深度学习


numpy_a = a.numpy()
print(numpy_a) # tensor a was converted to numpy （numpy 在深度学习中不用去学习


tensor_a = torch.from_numpy(numpy_a) # numpy a was converted to numpy
print(tensor_a)
tensor_a2 = torch.tensor(numpy_a) # numpy a was converted to numpy
print(tensor_a2)

torch_30 = torch.tensor(30)
print(torch_30) 
item_30 = torch_30.item()
print(item_30) # torch_30 was converted to scalar
print(type(item_30)) # <class 'int'>


