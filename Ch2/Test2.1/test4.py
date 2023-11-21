#节省内存
import torch
X = torch.arange(12, dtype=torch.float32).reshape((3,4))
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
before = id(Y)    #id()函数返回变量的内存地址
Y = Y + X
print(id(Y)==before)  #表明会为运算结果分配一个新的地址

##
# 我们可以使用切片表示法将操作的结果分配给先前分配的数组，例如Y[:] = <expression>。
# 首先创建一个新的矩阵Z，其形状与另一个Y相同， 使用zeros_like来分配一个全 0 的块。
# #
Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X + Y
print('id(Z):', id(Z))   #可以发现变量使用的是原来的地址

#即使后面没有重复使用X ,我们也可以使用X[:] = X + Y或X += Y来减少操作的内存开销。
