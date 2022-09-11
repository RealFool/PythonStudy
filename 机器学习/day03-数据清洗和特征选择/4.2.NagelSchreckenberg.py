#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def clip(x, path):
    for i in range(len(x)):
        if x[i] >= path:
            x[i] %= path


if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    path = 5000     # 环形公路的长度
    n = 100         # 公路中的车辆数目
    v0 = 50          # 车辆的初始速度
    p = 0.3         # 随机减速概率
    Times = 3000

    np.random.seed(0)
    # 给定车辆初始坐标
    x = np.random.rand(n) * path
    x.sort()
    # np.tile函数的作用 1.沿X轴复制 2.XY轴都复制，或只沿着Y轴复制的方法
    # 把初始速度v0沿着x轴复制n=100个
    v = np.tile([v0], n).astype(np.float_)

    plt.figure(figsize=(9, 7), facecolor='w')
    # 迭代Times=3000次
    for t in range(Times):
        # plt.scatter() 函数用于生成一个scatter散点图。
        plt.scatter(x, [t]*n, s=1, c='k', alpha=0.05)
        for i in range(n):
            if x[(i+1) % n] > x[i]:
                d = x[(i+1) % n] - x[i]   # 距离前车的距离
            else:
                d = path - x[i] + x[(i+1) % n]
            if v[i] < d:
                # 车速不快，随机加速减速
                if np.random.rand() > p:
                    v[i] += 1
                else:
                    v[i] -= 1
            else:
                # 车速很快，正常减速
                v[i] = d - 1
        # clip函数：限制一个array的上下界，限制车速在0到150之间
        v = v.clip(0, 150)
        # 一秒钟的位移
        x += v
        clip(x, path)
    # 绘图
    # x轴范围
    plt.xlim(0, path)
    # y轴范围
    plt.ylim(0, Times)
    plt.xlabel('车辆位置', fontsize=14)
    plt.ylabel('模拟时间', fontsize=14)
    plt.title('环形公路车辆堵车模拟', fontsize=18)
    # 图的边距离窗口的距离，2英寸
    plt.tight_layout(pad=2)
    plt.show()
