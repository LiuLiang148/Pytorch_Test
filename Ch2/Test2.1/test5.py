import torch
#转换为其他python对象
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
A = X.numpy()
B = torch.tensor(A)
print(type(A))
print(type(B))



a = torch.tensor([3.5]) #将大小为1的张量转换为Python标量

print(a, a.item(), float(a), int(a))

