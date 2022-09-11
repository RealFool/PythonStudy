# 李亚钦
# 2022/8/11 22:41
"""
https://blog.csdn.net/qq_34229228/article/details/123581540

灰色预测模型是通过少量的、不完全的信息，建立数学模型并做出预测的一种预测方法。
灰色系统理论建模采用的是先对原始数据列做生成处理再成立微分方程模型。
是处理小样本（4个就可以）预测问题的有效工具，而对于小样本预测问题回归和神经网络的效果都不太理想。
"""

from decimal import *


class GM11():
    def __init__(self):
        self.f = None

    def isUsable(self, X0):
        # 判断是否通过光滑检验
        X1 = X0.cumsum()
        rho = [X0[i] / X1[i - 1] for i in range(1, len(X0))]
        rho_ratio = [rho[i + 1] / rho[i] for i in range(len(rho) - 1)]
        print("rho:", rho)
        print("rho_ratio:", rho_ratio)
        flag = True
        for i in range(2, len(rho) - 1):
            if rho[i] > 0.5 or rho[i + 1] / rho[i] >= 1:
                flag = False
        if rho[-1] > 0.5:
            flag = False
        if flag:
            print("数据通过光滑校验")
        else:
            print("该数据未通过光滑校验")

        # 判断是否通过级比检验
        lambds = [X0[i - 1] / X0[i] for i in range(1, len(X0))]
        X_min = np.e ** (-2 / (len(X0) + 1))
        X_max = np.e ** (2 / (len(X0) + 1))
        for lambd in lambds:
            if lambd < X_min or lambd > X_max:
                print('该数据未通过级比检验')
                return
        print('该数据通过级比检验')

    def train(self, X0):
        X1 = X0.cumsum()
        Z = (np.array([-0.5 * (X1[k - 1] + X1[k]) for k in range(1, len(X1))])).reshape(len(X1) - 1, 1)
        # 数据矩阵A、B
        A = (X0[1:]).reshape(len(Z), 1)
        B = np.hstack((Z, np.ones(len(Z)).reshape(len(Z), 1)))
        # 求灰参数
        a, u = np.linalg.inv(np.matmul(B.T, B)).dot(B.T).dot(A)
        u = Decimal(u[0])
        a = Decimal(a[0])
        print("灰参数a：", a, "，灰参数u：", u)
        self.f = lambda k: (Decimal(X0[0]) - u / a) * np.exp(-a * k) + u / a

    def predict(self, k):
        X1_hat = [float(self.f(k)) for k in range(k)]
        X0_hat = np.diff(X1_hat)
        X0_hat = np.hstack((X1_hat[0], X0_hat))
        return X0_hat

    def evaluate(self, X0_hat, X0):
        # 根据后验差比及小误差概率判断预测结果
        S1 = np.std(X0, ddof=1)  # 原始数据样本标准差
        S2 = np.std(X0 - X0_hat, ddof=1)  # 残差数据样本标准差
        C = S2 / S1  # 后验差比
        Pe = np.mean(X0 - X0_hat)
        temp = np.abs((X0 - X0_hat - Pe)) < 0.6745 * S1
        p = np.count_nonzero(temp) / len(X0)  # 计算小误差概率
        print("原数据样本标准差：", S1)
        print("残差样本标准差：", S2)
        print("后验差比：", C)
        print("小误差概率p：", p)


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
    plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

    # 原始数据X
    X = np.array(
        [21.2, 22.7, 24.36, 26.22, 28.18, 30.16, 32.34, 34.72, 37.3, 40.34, 44.08, 47.92, 51.96, 56.02,
         60.14, 64.58, 68.92, 73.36, 78.98, 86.6])

    # 例一的数据
    # X = np.array([72.03, 73.84, 74.49, 76.68, 78.00, 79.68,
    #              81.21, 82.84, 84.5, 86.19, 87.92, 89.69, 91.49])

    # 训练集，前20*0.7 = 14项数据用于训练
    X_train = X[:int(len(X) * 0.7)]
    # X_train = X[:6]
    # 测试集，后6项数据预测并对比
    X_test = X[int(len(X) * 0.7):]
    # X_test = X[6:]

    model = GM11()
    model.isUsable(X_train)  # 判断模型可行性
    model.train(X_train)  # 训练
    Y_pred = model.predict(len(X))  # 预测
    Y_train_pred = Y_pred[:len(X_train)]
    Y_test_pred = Y_pred[len(X_train):]
    # score_test = model.evaluate(Y_test_pred, X_test)  # 评估
    # print('评估', score_test)

    # 可视化
    plt.grid()
    plt.plot(np.arange(len(X_train)), X_train, '->')
    plt.plot(np.arange(len(X_train)), Y_train_pred, '-o')
    plt.legend(['负荷实际值', '灰色预测模型预测值'])
    plt.title('训练集')
    plt.show()

    plt.grid()
    plt.plot(np.arange(len(X_test)), X_test, '->')
    plt.plot(np.arange(len(X_test)), Y_test_pred, '-o')
    plt.legend(['负荷实际值', '灰色预测模型预测值'])
    plt.title('测试集')
    plt.show()
