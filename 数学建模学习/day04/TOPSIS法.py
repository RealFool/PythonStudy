# 李亚钦
# 2022/8/10 22:43
"""
出自：https://zhuanlan.zhihu.com/p/37738503
TOPSIS 法是一种常用的组内综合评价方法，能充分利用原始数据的信息，其结果能精确地反映各评价方案之间的差距。
基本过程为基于归一化后的原始数据矩阵，采用余弦法找出有限方案中的最优方案和最劣方案，
然后分别计算各评价对象与最优方案和最劣方案间的距离，获得各评价对象与最优方案的相对接近程度，以此作为评价优劣的依据。
该方法对数据分布及样本含量没有严格限制，数据计算简单易行。
"""

import pandas as pd
import numpy as np


# 极小型指标
def dataDirection_1(datas, offset=0):
    def normalization(data):
        return 1 / (data + offset)

    return list(map(normalization, datas))


# 中间型指标
def dataDirection_2(datas, x_min, x_max):
    def normalization(data):
        if data <= x_min or data >= x_max:
            return 0
        elif x_min < data < (x_min + x_max) / 2:
            return 2 * (data - x_min) / (x_max - x_min)
        elif x_max > data >= (x_min + x_max) / 2:
            return 2 * (x_max - data) / (x_max - x_min)

    return list(map(normalization, datas))


# 区间型指标
def dataDirection_3(datas, x_min, x_max, x_minimum, x_maximum):
    def normalization(data):
        if x_min <= data <= x_max:
            return 1
        elif data <= x_minimum or data >= x_maximum:
            return 0
        elif x_max < data < x_maximum:
            return 1 - (data - x_max) / (x_maximum - x_max)
        elif x_min > data > x_minimum:
            return 1 - (x_min - data) / (x_min - x_minimum)

    return list(map(normalization, datas))


# 计算权重
def entropyWeight(data):
    data = np.array(data)
    # 归一化
    P = data / data.sum(axis=0)

    # 计算熵值
    E = np.nansum(-P * np.log(P) / np.log(len(data)), axis=0)

    # 计算权系数
    return (1 - E) / (1 - E).sum()


# TOPSIS
def topsis(data, weight=None):
    # 归一化
    data = data / np.sqrt((data ** 2).sum())

    # 最优最劣方案
    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])

    # 距离
    weight = entropyWeight(data) if weight is None else np.array(weight)
    Result = data.copy()
    Result['正理想解'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
    Result['负理想解'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

    # 综合得分指数
    Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']

    return Result, Z, weight


# data_csv = pd.read_csv('TOPSIS.csv', header=0)

data = pd.DataFrame(
    {'人均专著': [0.1, 0.2, 0.4, 0.9, 1.2], '生师比': [5, 6, 7, 10, 2], '科研经费': [5000, 6000, 7000, 10000, 400],
     '逾期毕业率': [4.7, 5.6, 6.7, 2.3, 1.8]}, index=['院校' + i for i in list('ABCDE')])

data['生师比'] = dataDirection_3(data['生师比'], 5, 6, 2, 12)  # 师生比数据为区间型指标
# data['逾期毕业率'] = 1 / data['逾期毕业率']  # 逾期毕业率为极小型指标
data['逾期毕业率'] = dataDirection_1(data['逾期毕业率'])  # 逾期毕业率为极小型指标
# 其余均为极大型指标

out = topsis(data, weight=[0.2, 0.3, 0.4, 0.1])  # 设置权系数

print(out)
