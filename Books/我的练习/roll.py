#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: roll.py
@time: 2019/6/13 16:46
"""
from matplotlib.pyplot import *

x = [1, 4, 2, 4]
y = [5, 4, 3, 2]
# 创建一个新图表
figure()
subplot(111)

subplot(231)
plot(x, y)

subplot(232)
bar(x, y)

subplot(233)
barh(x, y)

subplot(234)
# 柱状对叠图
bar(x, y)
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')

subplot(235)
boxplot(x)

subplot(236)
scatter(x, y)
# plot([1,3,2,3,2],[112,33,2,3,2])

show()

import random


def roll():
    print(random.sample(range(0, 100), 10))


if __name__ == '__main__':
    roll()
