# 李亚钦
# 2022/8/9 18:20
"""
例一、求解：y'' + 2y' + y = x^2
"""

# from sympy import *
#
# y = symbols('y', cls=Function)
# x = symbols('x')
# # y(x).diff(x, 2)：y对x求二阶导
# eq = Eq(y(x).diff(x, 2) + 2 * y(x).diff(x, 1) + y(x), x ** 2)
# print(dsolve(eq, y(x)))


"""
例二、求数值解：y' = x^2 + y^2
"""
# from scipy.integrate import odeint
# import numpy as np
#
# dy = lambda y, x: x ** 2 + y ** 2
# x = np.arange(0, 10.5, 0.5)
# sol = odeint(dy, 0, x)
# print('x={}\n对应的数值解y={}'.format(x, sol.T))


"""
例三、y' = 1/(x^2+1) - 2y^2 , y(0) = 0
"""
# from scipy.integrate import odeint
# import matplotlib.pyplot as plt
# import numpy as np
# dy = lambda y, x: 1/(1 + x**2) - 2 * y**2
# x = np.arange(0, 10.5, 0.5)
# sol = odeint(dy, 0, x)
# print('x={}\n对应的数值解y={}'.format(x, sol.T))
# plt.plot(x, sol)
# plt.show()


"""
例四、高阶微分方程求解
y'' = 1000(1-y^2)y' + y = 0
y(0) = 0, y'(0) = 2
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def fvdp(t, y):
    """
    要把y看出一个向量，y = [dy0, dy1, dy2, ...]分别表示y的n阶导，要么y[0]就是需要求解的函数，y[1]表示一阶导，y[2]表示二阶导，以此类推
    """
    dy1 = y[1]  # y[1] = dy/dt, 一阶导
    dy2 = 1000 * (1 - y[0] ** 2) * y[1] + y[0]
    # y[0]是最初始，也就是需要求解的函数
    # 注意返回的顺序是[一阶导，二阶导]，这就形成了一阶微分方程组
    return [dy1, dy2]


def solve_second_order_ode():
    """
    求解二阶ODE
    """
    x = np.arange(0, 0.25, 0.01)  # 给x规定范围
    y0 = [0.0, 2.0]  # 初值条件
    # 初值[0.0, 2.0]表示y(0) = 2, y'(0) = 0
    # 返回y，其中y[:, 0]是y[0]的值，就是最终解，y[:, 1]是y'(x)的值
    y = odeint(fvdp, y0, x, tfirst=True)
    print(y)

    plt.plot(x, y[:, 0], label='y')
    plt.plot(x, y[:, 1], label='y’')
    plt.legend()    # label图例
    plt.show()


solve_second_order_ode()
