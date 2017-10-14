#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0302-定义图标类型-柱状图、线形图和堆积柱状图.py
@time: 2017/10/14 10:34
"""

from matplotlib.pyplot import *

x = [1, 2, 3, 4]
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
bar(x, y)
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color='r')

subplot(235)
boxplot(x)

subplot(236)
scatter(x, y)
# plot([1,3,2,3,2],[112,33,2,3,2])

show()
