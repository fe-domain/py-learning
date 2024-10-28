# 张量的基本运算
import torch

a = [[1,2],[3,4]]
b = [[2,2],[4,4]]

tensor_a = torch.tensor(a)
print(tensor_a)
print(tensor_a.add(10)) # tensor_value.add(number) add func not changed value of called
print(tensor_a)



tensor_b = torch.tensor(b)

print('hadamard mul: ', tensor_a * tensor_b)
print('hadamard torch.mul: ',torch.mul(tensor_a,tensor_b))


print("\ntensor_a @ tensor_b: ", tensor_a @ tensor_b) # 张量 乘法
print("\ntorch.matmul", torch.matmul(tensor_a,tensor_b)) # 张量 乘法运算