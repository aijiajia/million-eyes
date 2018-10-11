#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 正态分布.py
@time: 2018/10/11 13:18
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


def normal001():
    mu, sigma, num_bins = 0, 1, 50
    x = mu + sigma * np.random.randn(100000)
    print(np.mean(x))
    # 正态分布的数据
    n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor='blue', alpha=0.5)
    # 拟合曲线
    print("bins: {}".format(bins))

    y = mlab.normpdf(bins, mu, sigma)
    plt.plot(bins, y, 'r--')
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('histogram of normal distribution: $\mu = 0$, $\sigma=1$')

    plt.subplots_adjust(left=0.15)
    plt.show()


def normal002():
    # x的范围为60-150，以1为单位,需x根据范围调试
    x = np.arange(60, 151, 1)
    print(x)
    mean = x.mean()
    std = x.std()
    print(x)
    # x数对应的概率密度
    y = normfun(x, mean, std)

    # 参数,颜色，线宽
    plt.plot(x, y, color='g', linewidth=3)

    # 数据，数组，颜色，颜色深浅，组宽，显示频率
    # plt.hist(iq, bins=7, color='r', alpha=0.5, rwidth=0.9, normed=True)

    plt.title('IQ distribution')
    plt.xlabel('IQ score')
    plt.ylabel('Probability')
    plt.show()


# 散点图
def normal003():
    mu, sigma, num_bins = 0, 1, 50
    x = mu + sigma * np.random.randn(100000)
    print(np.mean(x))
    # 正态分布的数据
    # n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor='blue', alpha=0.5)
    # 拟合曲线
    # print("bins: {}".format(bins))

    y = mlab.normpdf(x, mu, sigma)
    plt.scatter(x, y)
    plt.xlabel('Expectation')
    plt.ylabel('Probability')
    plt.title('histogram of normal distribution: $\mu = 0$, $\sigma=1$')

    plt.subplots_adjust(left=0.15)
    plt.show()


if __name__ == '__main__':
    normal003()
