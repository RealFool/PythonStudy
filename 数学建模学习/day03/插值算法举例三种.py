# 李亚钦
# 2022/8/10 17:40
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

x0 = [1, 2, 3, 4, 5]
y0 = [1.6, 1.8, 3.2, 5.9, 6.8]
x = np.arange(1, 5, 1/30)
# 线性插值
f1 = interp1d(x0, y0, kind='linear')
y1 = f1(x)

# 三次样条插值
f2 = interp1d(x0, y0, 'cubic')
y2 = f2(x)

# 拉格朗日插值
def lagrange(x0, y0, x):
    y = []
    for k in range(len(x)):
        s = 0
        for i in range(len(y0)):
            t = y0[i]
            for j in range(len(y0)):
                if i != j:
                    t *= (x[k] - x0[j])/(x0[i] - x0[j])
            s += t
        y.append(s)
    return y


y3 = lagrange(x0, y0, x)
plt.plot(x0, y0, 'r*', label='原始数据')
plt.plot(x, y1, 'b-', label='线性插值')
plt.plot(x, y2, 'y-', label='三次样条插值')
plt.plot(x, y3, 'r-', label='拉格朗日插值')
plt.legend()
plt.show()


