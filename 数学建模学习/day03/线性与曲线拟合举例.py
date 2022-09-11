# 李亚钦
# 2022/8/10 17:59
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

X = np.arange(1, 11, 1)
Y = np.array([1.1, 2.5, 3.6, 4.9, 6.2, 9.0, 9.5, 11.0, 15.6, 14.1])
# 线性拟合，deg=1拟合多项式的次数
p = np.polyfit(X, Y, deg=1)
print(p)


# 定义要拟合的测试函数，作为曲线拟合方程
def Pfun(X, a, b):
    return 1 / (a + b * X)


# 曲线拟合
popt, pcov = curve_fit(Pfun, X, Y)
print(popt)

plt.plot(X, Y, '*', X, np.polyval(p, X), 'r-')
# *popt个数可变的位置参数
plt.plot(X, Pfun(X, *popt), 'b-')
plt.show()
