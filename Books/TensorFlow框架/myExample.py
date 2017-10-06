#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: myExample.py
@time: 2017/10/6 11:18
"""


from numpy.random import RandomState
rdm = RandomState(1)
dataset_size = 4
X = rdm.rand(dataset_size, 2)
Y1 = [[int(x1+x2 < 1)] for (x1,x2) in X ]
Y2 = [int(x1+x2 < 1) for (x1,x2) in X ]
# print(type(Y1)," == ",type(Y2))
print(Y1)
print(Y2)