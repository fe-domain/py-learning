import torch


# data1 = torch.randint(1,10,[2,3,2])
# data2 = torch.randint(1,10,[2,3,2])

# print("data1: ", data1)
# print("data2: ", data2)
# # 除了拼接的维度其他维度一定是相同的，连接的维度相加
# print("torch.cat([data1,data2],dim=0): ",torch.cat([data1,data2],dim=0), "shape: ", torch.cat([data1,data2],dim=0).shape)
# print("torch.cat([data1,data2],dim=1): ",torch.cat([data1,data2],dim=1), " shape: ", torch.cat([data1,data2],dim=1).shape)


# 1. 当  x 为标量时梯度的计算
def test01():
    x = torch.tensor(5)
    # 目标值
    y = torch.tensor(0.)
    # 设置要更新的权重和偏置的初始值
    w = torch.tensor(1., requires_grad=True, dtype=torch.float32)
    b = torch.tensor(3.0, requires_grad=True, dtype=torch.float32)
    # 设置网络的输出值
    z = x*w+b # 矩阵乘法
    # 设置损失函数，并进行损失的计算
    loss = torch.nn.MSELoss()
    loss = loss(z,y)
    # 自动微分
    loss.backward()
    # 打印 w,b 变量的梯度
    # backward 函数计算的梯度值回存储在张量的 grad 变量中
    print("w 的梯度:",w.grad)
    print("b 的梯度:",b.grad)


test01()