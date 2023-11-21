#import os
#os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import torch
x = torch.arange(12)
print(x)
print(x.shape)
print(x.shape)

print(x.numel())
X = x.reshape(3,4)
print(X)
print(torch.zeros((2,3,4)))#生成形状为(2,3,4)的张量
print(torch.randn(3,4))#创建一个形状为（3,4）的张量。 其中的每个元素都从均值为0、标准差为1的标准高斯分布（正态分布）中随机采样
print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))