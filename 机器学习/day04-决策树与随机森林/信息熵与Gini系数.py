# 李亚钦
# 2022/8/23 23:02
import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0, 1, 100)[1:99]
print(p)
# 信息熵
h = -(1-p)*np.log(1-p) - p*np.log(p)
# Gini系数
h2 = 2*(1-p)*p
plt.plot(p, h, 'r-', lw=3, label='Entropy')
plt.plot(p, h2, 'b-', lw=3, label='Gini')
plt.legend()
plt.show()
