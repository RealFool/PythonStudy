# 李亚钦
# 2022/8/11 14:38
"""
主成分分析法概述
主成分分析法是一种线性的降维算法，通过将N维特征进行正交变换，得到相互独立的k维(k<N)数据，通过分析得出“主成分”，利用“主成分”确定影响权重。

"""
import matplotlib.pyplot as plt
import sklearn.decomposition as dp
from sklearn.datasets import load_iris

x, y = load_iris(return_X_y=True)   # 加载数据，x表示数据集中的属性数据，y表示数据标签
pca = dp.PCA(n_components=2)   # 加载pca算法，设置降维后主成分数目为2
reduced_x = pca.fit_transform(x)  # 对原始数据进行降维，保存在reduced_x中
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

"""
pca.components_ #模型的各个特征向量 也叫成分矩阵
pca.explained_variance_  # 贡献方差，即特征根
pca.explained_variance_ratio_ #各个成分各自的方差百分比（贡献率）
"""

print(reduced_x)
print(pca.explained_variance_ratio_)
for i in range(len(reduced_x)):
    if y[i] == 0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()
