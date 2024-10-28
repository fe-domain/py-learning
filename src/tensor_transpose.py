import torch

# 创建一个 2x3 的 tensor
tensor = torch.randint(1,10,[2,3,2])
"""
torch.randint(low, high, size, ...)
low: 第一个参数是最小值（包含在内），在这个例子中是 1。
high: 第二个参数是最大值（不包含在内），在这个例子中是 10。也就是说，生成的整数会在 [1, 10) 范围内。
size: 第三个参数是张量的形状。在这个例子中是 [2, 3, 2]，代表生成的张量的形状是 2×3×2。

张量形状: [2, 3, 2] 表示生成的张量是三维的，它有以下维度：
第一维度大小为 2，表示张量有 2 个子张量；
每个子张量中有 3 个元素（子张量）；
每个元素内部是一个含有 2 个随机整数的小张量。
"""

data = torch.tensor([
    [
        [9, 2],
        [5, 9],
        [7, 5]
    ],

    [
        [7, 4],
        [1, 3],
        [2, 1]
    ]
])


print(data.shape) # torch.Size([2, 3, 2]) 2x3x2

print(data.reshape(2,6).shape)
# reshape, squeeze, unsqueeze func 都不改变数据量，知识改变 tensor 的形状
# print(data.reshape(2,6)) # tensor([[9, 2, 5, 9, 7, 5],[7, 4, 1, 3, 2, 1]])


print("data.squeeze(dim=1): ", data.squeeze(dim=1), " data.squeeze(dim=1) shape: ",data.squeeze(dim=1).shape)
print("data.unsqueeze(dim=0): ",data.unsqueeze(dim=0), " data.unsqueeze(dim=0): ", data.unsqueeze(dim=0).shape)


# transpose 互换位置
print(data.shape) # torch.Size([2, 3, 2])
print(torch.transpose(data, 0, 1).shape) # torch.Size([3, 2, 2])

# permute 重新排列
print(torch.permute(data,[2,0,1]).shape)


# contiguous # 接近的
g_data = data.contiguous()
print(g_data.shape) # torch.Size([2, 2, 3])