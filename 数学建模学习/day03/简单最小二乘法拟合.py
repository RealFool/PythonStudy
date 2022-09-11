# 李亚钦
# 2022/8/10 15:58
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 不加这一句中文会乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读csv文件
data = pd.read_csv('SimpleLR.csv')
print(data)
# 画图
# data.plot.scatter(x='日均人流量（千人）', y='日均销售收入（千元）')
# plt.show()

# 简单线性回归
# features = data['日均人流量（千人）'].values.reshape(len(data['日均人流量（千人）'].values), 1)
# features = data['日均人流量（千人）'].values.reshape(-1, 1)
# target = data['日均销售收入（千元）']
# regression = LinearRegression()
# model = regression.fit(features, target)
# print(model.intercept_, model.coef_)

x = np.array(data['日均人流量（千人）'].values)
y = data['日均销售收入（千元）']
an = np.polyfit(x, y, 1)
print(an)
p1 = np.poly1d(an)
print(p1)

data_ = an[0] * x + an[1]
print(x)
print(data_)

data.plot.scatter(x='日均人流量（千人）', y='日均销售收入（千元）')
plt.plot(x, data_)
plt.show()
