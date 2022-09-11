# 李亚钦
# 2022/7/22 23:17
"""求阶乘"""


def fun(num):
    if num == 1:
        return 1
    else:
        return num * fun(num - 1)


print(fun(6))


def fun2(n):
    if n < 3:
        return 1
    else:
        return fun2(n-1) + fun2(n-2)


print(fun2(6))


