# 李亚钦
# 2022/8/10 17:17
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(0, 0.4, 100)  # 生成符合正态分布的随机数
x2 = np.random.normal(0, 0.6, 100)
x3 = np.random.normal(0, 0.2, 100)
eps = np.random.normal(0, 0.05, 100)  # 生成噪声数据
c = np.array([0.1, 0.2, 0.7])  # 生成模拟数据时的系数的值
x = np.c_[x1, x2, x3]  # 调用c_函数来生成自变量的数据的矩阵，按照列进行生成；100x3的矩阵
print('x', x)
y = x.dot(c) + eps  # 点积+噪声
print('y', y)

x_model = sm.add_constant(x)    # add_ constant给矩阵加上一列常量1，主要目的:便于估计多元线性回归模型的截距，也是便于后面进行参数估计时的计算
print('x_model', x_model)
model = sm.OLS(y, x_model)  # 调用OLS普通最小二乘法
results = model.fit()   # fit拟合，主要功能就是进行参数估计，参数估计的主要目的是估计出回归系数，根据参数估计结果来计算统计量，这些统计量主要的目的就是对我们模型的有效性或是显著性水平
print(results.summary())    # summary方法主要是为了显示拟合的结果
# 结果为 y = -0.0019 + 0.0932x1 +0.1965x2 + 0.7204x3

# y.plot.scatter(x='x', y='y')
plt.plot(x, y)
plt.show()
