# 李亚钦
# 2022/8/8 22:42
from scipy.optimize import minimize
import numpy as np


# 目标函数即min(FG1 + FG2 + FG3)
def fun(x):
    # 常数项 + 一次项 + 二次项
    return 4 + 3 + 3.5 + \
           0.3 * x[0] + 0.32 * x[1] + 0.3 * x[2] + \
           0.0007 * x[0] ** 2 + 0.0004 * x[1] ** 2 + 0.00045 * x[2] ** 2


def con():
    # 约束条件： 分为eq 和 ineq
    # eq表示 函数结果等于0；ineq表示 表达式大于等于0；本题中要求x1 + x2 + x3 = 700，即x1 + x2 + x3 - 700 = 0，所以选eq
    cons_ = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] + x[2] - 700})
    return cons_


# 上下限约束
b1 = (100, 200)
b2 = (120, 250)
b3 = (150, 300)
bns = (b1, b2, b3)  # 边界约束
if __name__ == '__main__':
    cons = con()    # 约束
    # 设置x的初始猜测值
    x0 = np.array([150, 250, 300])
    res = minimize(fun, x0, method='SLSQP', constraints=cons, bounds=bns)
    print(res)
    print('代价', res.fun)
    print(res.success)
    print('解', res.x)
