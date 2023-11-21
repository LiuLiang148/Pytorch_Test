#线性代数
import torch


#标量由只有一个元素的张量表示
x = torch.tensor(3)
y = torch.tensor(2.0)
print(x+y,x*y)

#向量 向量可以被视为标量值组成的列表

X = torch.arange(4)
print(X)
print(X[3])
print(len(X))