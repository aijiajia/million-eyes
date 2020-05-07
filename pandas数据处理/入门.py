#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 入门.py
@time: 2020/5/7 13:43
"""
from pandas import Series, DataFrame
import pandas as pd


# Series 是一种类似于一维数组的独享，由一组数据（Numpy数据类型）以及一组与之相关联的数据标签（索引）组成。
# 列表产生Serise
def func():
    obj = Series([1, 2, 3, 4, 5])
    print(obj)


if __name__ == '__main__':
    func()
