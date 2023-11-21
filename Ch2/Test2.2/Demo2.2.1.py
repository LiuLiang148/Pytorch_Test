#读取数据集
import os
import  torch
import pandas as pd

os.makedirs(os.path.join('..', 'data'), exist_ok=True) #返回上级目录并创建data文件夹
data_file = os.path.join('..', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

##
# 要从创建的CSV文件中加载原始数据集,需要导入pandas包并调用read_csv函数。
# 该数据集有四行三列。
# 其中每行描述了房间数量（“NumRooms”）、巷子类型（“Alley”）和房屋价格（“Price”）。
# #


data = pd.read_csv(data_file)
print(data)


inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]  #iloc即index location,
# [:, 0:2] 即所有行的第一列和第二列元素，[:, 2]即所有行的第三列
inputs = inputs.fillna(inputs.mean()) #fillna 即填充NA，不对字符类型数据进行填充
print(inputs)


##
#对于inputs中的类别值或离散值，我们将“NaN”视为一个类别。
# 由于“巷子类型”（“Alley”）列只接受两种类型的类别值“Pave”和“NaN”，
# pandas可以自动将此列转换为两列“Alley_Pave”和“Alley_nan”。
# 巷子类型为“Pave”的行会将“Alley_Pave”的值设置为1，“Alley_nan”的值设置为0。
# 缺少巷子类型的行会将“Alley_Pave”和“Alley_nan”分别设置为0和1。
# #

inputs = pd.get_dummies(inputs, dummy_na=True)  #将离散型特征的每一种取值都看成一种状态
print(inputs)

X, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(X)
#print(y)