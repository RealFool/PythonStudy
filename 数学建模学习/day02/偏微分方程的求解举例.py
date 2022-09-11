# 李亚钦
# 2022/8/9 20:32
"""
例一、求解微分方程组
dx/dt = 2x - 3y + 3z
dy/dt = 4x - 5y + 3z
dz/dt = 4x - 4y + 2z
x(0) = 1, y(0) = 2, z(0) = 1
"""
# solve_ivp是解微分方程组数值解的一个方法
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


def fun(t, w):
    x = w[0]
    y = w[1]
    z = w[2]
    return [2 * x - 3 * y + 3 * z,
            4 * x - 5 * y + 3 * z,
            4 * x - 4 * y + 2 * z]


# 初始条件，t=0时
y0 = [1, 2, 1]
# (0, 10) t_span： 2 元组的浮点数,积分区间 (t0, tf)。求解器从 t=t0 开始并积分，直到达到 t=tf。
yy = solve_ivp(fun, (0, 10), y0, method='RK45', t_eval=np.arange(0, 10, 1))
print(yy)
t = yy.t
data = yy.y
plt.plot(t, data[0, :], label='x')
plt.plot(t, data[1, :], label='y')
plt.plot(t, data[2, :], label='z')
plt.legend()
plt.xlabel('时间t')
plt.show()
