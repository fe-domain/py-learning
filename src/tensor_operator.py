
import torch

a = [[1,2], [3,4]]
tensor_a = torch.tensor(a)


print("tensor sum: ",tensor_a.sum()) # tensor(10)
print("tensor pow: ", torch.pow(tensor_a,2)) # tensor([[ 1,  4], [ 9, 16]])
print("tensor sqrt: " , torch.sqrt(tensor_a)) # tensor tensor([[1.0000, 1.4142], [1.7321, 2.0000]])


print("tensor log: ", tensor_a.log())
print("tensor log2: ", torch.log2(tensor_a))
print("tensor log10: ", torch.log10(tensor_a))
print("tensor exp: ", torch.exp(tensor_a))
print("tensor neg: ", torch.neg(tensor_a))
print("tensor abs: ", torch.abs(tensor_a))
print("tensor sin: ", torch.sin(tensor_a))
print("tensor cos: ", torch.cos(tensor_a))



