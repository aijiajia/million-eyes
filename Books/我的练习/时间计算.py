#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 时间计算.py
@time: 2019/7/8 11:25
"""
from datetime import datetime


def get_page(origin_page):
    print([i + 24 for i in origin_page])


def get_days():
    print((datetime(2019, 12, 31) - datetime(2018, 1, 1)).days)


def get_per_month():
    print(sum([22, 17, 22, 20, 22, 20, 22, 23, 21, 18, 22, 22]))


if __name__ == '__main__':
    # get_page([61, 89,122,156,180,198,243,263,286,317,334,364,446])
    # get_days()
    get_per_month()
