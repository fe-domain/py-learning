import torch

# 创建张量的方式
t = torch.randn(3,4) # 创建 3 行 4 列的 随机张量
print(t) # tensor([[2, 3]])

print(torch.ones(1,3)) # 生成 1 行 3列的 tensor （以 1 作为填充值）
print(torch.zeros(2,3)) # 生成 2 行 3列的 tensor （以 0 作为填充值）
print(torch.full((2,3),20)) # # 生成 2 行 3列的 tensor （以 20 作为填充值）创建全为指定值的张量

print(torch.Tensor(2,3))

# 二维数组(列表)
a = [[1,2], [3,4]]
print(a)

a = torch.tensor(a)
print(a.dtype) # torch.int64

# convert torch.int64 to double type(float type)
f_a = a.type(torch.DoubleTensor)
f_b = a.double()

print(f_a.dtype) # torch.float64
print(f_b.dtype) # torch.float64
