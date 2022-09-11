# 李亚钦
# 2022/8/8 22:03
"""
线性规划标准形式：
min cX

Ax <= b
Aeq * x = beq
lb <= x <= ub

求线性规划：
max z = 2x1 + 3x2 - 5x3

x1 + x2 + x3 = 7
2x1 - 5x2 + x3 >=10
x1 + 3x2 + x3 <= 12
x1 ,x2, x3 >= 0
"""
import numpy as np
from scipy.optimize import linprog
c = np.array([-2, -3, 5])
A = np.array([[-2, 5, -1], [1, 3, 1]])
b = np.array([-10, 12])
Aeq = np.array([[1, 1, 1]])
beq = np.array([7])
x1, x2, x3 = (0, None), (0, None), (0, None)
res = linprog(c, A, b, Aeq, beq, bounds=(x1, x2, x3))
print(res)

