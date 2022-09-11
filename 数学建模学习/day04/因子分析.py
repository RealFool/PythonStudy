# 李亚钦
# 2022/8/11 15:29
# 数据处理
"""
https://blog.csdn.net/qq_25990967/article/details/122566533

   因子分析就是将存在某些相关性的变量提炼为较少的几个因子，用这几个因子去表示原本的变量，也可以根据因子对变量进行分类。
   因子分子本质上也是降维的过程，和主成分分析（PCA）算法比较类似。
"""

import pandas as pd
import numpy as np

# 绘图
import seaborn as sns
import matplotlib.pyplot as plt
# 因子分析
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 读取数据
df = pd.read_csv("yinzifenxi.csv", index_col=0).reset_index(drop=True)
"""
如果不想要城市那一列的话，可以在读取的时候就删除，也可以后面再删, 比如，读取时删除
df = pd.read_csv("yinzifenxi.csv", index_col=0).reset_index(drop=True)
"""
print(df)
print(df.isnull().sum())
"""
然后，我们可以针对的，对数据进行一次处理：
比如删除无效字段的那一列
# 去掉无效字段
df.drop(["变量名1","变量名2","变量名3"],axis=1,inplace=True)
或者，删除空值
# 去掉空值
df.dropna(inplace=True)
"""

"""
Bartlett's球状检验
        检验总体变量的相关矩阵是否是单位阵（相关系数矩阵对角线的所有元素均为1,所有非对角线上的元素均为零）；即检验各个变量是否各自独立。
        如果不是单位矩阵，说明原变量之间存在相关性，可以进行因子分子；反之，原变量之间不存在相关性，数据不适合进行主成分分析
"""

chi_square_value, p_value = calculate_bartlett_sphericity(df)
print('Bartlett\'s球状检验:', chi_square_value, p_value)

"""
KMO检验
        检查变量间的相关性和偏相关性，取值在0-1之间；KOM统计量越接近1，变量间的相关性越强，偏相关性越弱，因子分析的效果越好。
        通常取值从0.6开始进行因子分析
"""
# KMO检验

kmo_all, kmo_model = calculate_kmo(df)
print('KMO检验:', kmo_model)
# 通过结果可以看到KMO大于0.6，也说明变量之间存在相关性，可以进行分析。

"""
选择因子个数
方法：计算相关矩阵的特征值，进行降序排列
"""
faa = FactorAnalyzer(25, rotation=None)
faa.fit(df)
# 得到特征值ev、特征向量v
ev, v = faa.get_eigenvalues()
print('得到特征值ev、特征向量v:', ev, v)

# 将特征值和因子个数的变化绘制成图形：
# 同样的数据绘制散点图和折线图
plt.scatter(range(1, df.shape[1] + 1), ev)
plt.plot(range(1, df.shape[1] + 1), ev)

# 显示图的标题和xy轴的名字
# 最好使用英文，中文可能乱码
plt.title("Scree Plot")
plt.xlabel("Factors")
plt.ylabel("特征值")

plt.grid()  # 显示网格
plt.show()  # 显示图形
# 从上面的图形中，我们明确地看到：选择2或3个因子就可以了

"""
因子旋转
建立因子分析模型
在这里选择，最大方差化因子旋转
"""
# 选择方式： varimax 方差最大化
# 选择固定因子为 2 个
faa_two = FactorAnalyzer(2, rotation='varimax')
print('因子旋转:', faa_two.fit(df))
# 公因子方差
print('公因子方差:', faa_two.get_communalities())
# 查看每个变量的公因子方差数据
print('每个变量的公因子方差数据:', pd.DataFrame(faa_two.get_communalities(), index=df.columns))
print('旋转后的特征值:', faa_two.get_eigenvalues())
print(pd.DataFrame(faa_two.get_eigenvalues()))
# 变量个数*因子个数
print('查看成分矩阵:', faa_two.loadings_)
print(pd.DataFrame(faa_two.loadings_, index=df.columns))

"""
查看因子贡献率
通过理论部分的解释，我们发现每个因子都对变量有一定的贡献，存在某个贡献度的值，在这里查看3个和贡献度相关的指标：
总方差贡献：variance (numpy array) – The factor variances
方差贡献率：proportional_variance (numpy array) – The proportional factor variances
累积方差贡献率：cumulative_variances (numpy array) – The cumulative factor variances
 我们来看一下总方差贡献吧
"""
print('因子贡献率:', faa_two.get_factor_variance())

df1 = pd.DataFrame(np.abs(faa_two.loadings_), index=df.columns)
print(df1)
# 绘图

"""
隐藏变量可视化
为了更直观地观察每个隐藏变量和哪些特征的关系比较大，进行可视化展示，为了方便取上面相关系数的绝对值：
"""
# 绘图
plt.figure(figsize=(14, 14))
ax = sns.heatmap(df1, annot=True, cmap="BuPu")

# 设置y轴字体大小
ax.yaxis.set_tick_params(labelsize=8)
plt.title("Factor Analysis", fontsize="xx-large")

# 设置y轴标签
plt.ylabel("Sepal Width", fontsize="xx-large")
# 显示图片
plt.show()

# 保存图片
# plt.savefig("factorAnalysis", dpi=500)

"""
转成新变量
上面我们已经知道了2个因子比较合适，可以将原始数据转成2个新的特征，具体转换方式为：
"""
faa_two.transform(df)
df2 = pd.DataFrame(faa_two.transform(df))
print(df2)
