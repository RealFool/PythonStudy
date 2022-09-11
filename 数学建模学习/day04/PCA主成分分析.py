# 李亚钦
# 2022/8/11 14:09


# 用python实现主成分分析（PCA）
import numpy as np
from numpy.linalg import eig
from sklearn.datasets import load_iris


def pca(X, k):
    X = X - X.mean(axis=0)  # 向量X去中心化
    X_cov = np.cov(X.T, ddof=0)  # 计算向量X的协方差矩阵，自由度可以选择0或1
    eigenvalues, eigenvectors = eig(X_cov)  # 计算协方差矩阵的特征值和特征向量
    klarge_index = eigenvalues.argsort()[-k:][::-1]  # 选取最大的K个特征值及其特征向量
    k_eigenvectors = eigenvectors[klarge_index]  # 用X与特征向量相乘
    return np.dot(X, k_eigenvectors.T)


iris = load_iris()

if __name__ == '__main__':
    X = np.array([[1, 2, 3, 4], [10, 20, 30, 40], [5, 6, 7, 8], [1, 1.9, 2.1, 4]])
    k = 2
    X_pca = pca(X, k)
    print(X_pca)
