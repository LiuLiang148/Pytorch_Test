import torch
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x + y, x - y, x * y, x / y, x ** y) # **运算符是求幂运算
x = torch.exp(x)
print(x)


X = torch.arange(12, dtype=torch.float32).reshape((3,4))#生成3行4列，内容为0-11的张量
Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
A = torch.cat((X, Y), dim=0)    #将两个张量按行连接，结果为6行4列。其中dim表示维数
B = torch.cat((X, Y), dim=1)    #将两个张量按列连接，结果为3行8列

print(A)
print(B)
print(X==Y)  #判断两个同型张量对应位置上的值是否相等

print(X.sum())