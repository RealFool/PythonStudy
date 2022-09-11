# 李亚钦
# 2022/8/12 23:10
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime  # 数据索引改为时间
import numpy as np
import statsmodels.api as sm  # acf,pacf图
from statsmodels.tsa.stattools import adfuller  # adf检验
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA

excelFile = 'train2.csv'
# 读取数据，指定日期列为指标，Pandas自动将“日期”列识别为Datetime格式
data = pd.read_csv(excelFile, index_col=u'日期')
data = pd.DataFrame(data, dtype=np.float64)

print(data)
# 时序图
plt.figure(figsize=(10, 6))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
data["销量"].plot()
plt.xlabel('日期', fontsize=12, verticalalignment='top')
plt.ylabel('销量', fontsize=14, horizontalalignment='center')
plt.show()
