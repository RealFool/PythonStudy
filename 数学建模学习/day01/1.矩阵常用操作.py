# 李亚钦
# 2022/8/8 21:30
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])
c = np.array([[1, 2, 3]])
d = np.array([[9, 8, 7], [3, 2, 1]])
e = np.array([[1, 2], [3, 4]])

# 矩阵加法
print('-' * 5, '矩阵加法', '-' * 5)
print(a + d)
# 放缩
print('-' * 5, '放缩', '-' * 5)
print(3 * a)
# 数乘、矩阵乘
print('-' * 5, '数乘、矩阵乘', '-' * 5)
print(np.dot(a, b))
# 元素乘
print('-' * 5, '元素乘', '-' * 5)
print(a * d)
# 转置
print('-' * 5, '转置', '-' * 5)
print(c.T)
# 逆矩阵
print('-' * 5, '逆矩阵', '-' * 5)
print(np.linalg.inv(e))
# 行列式
print('-' * 5, '行列式', '-' * 5)
print(np.linalg.det(e))
# 矩阵的秩
print('-' * 5, '矩阵的秩', '-' * 5)
print(np.linalg.matrix_rank(d))
np.linspace
