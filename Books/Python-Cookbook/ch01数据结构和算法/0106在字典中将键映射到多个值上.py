#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0106在字典中将键映射到多个值上.py
@time: 2017/10/8 9:08
"""
from collections import defaultdict


def func():
    pass


if __name__ == '__main__':

    # 问题： k -> vs 一个键多个值
    # 方案: 要使用列表还是集合要看应用场景，列表可以保持插入顺序，集合可以消除重复元素。
    # 如：输出{1, 2, 3}
    # f = {1,1,3,2,3}
    # print(f)
    d = {
        'a': [1, 2, 3],
        'b': [4, 5]
    }
    e = {
        'a': {1, 2, 3},
        'b': {4, 5}
    }
    # 为了能方便地创建这些字典，可以利用collections模块中的defaultdict类。
    # defaultdict 的一个特点就是它会自动初始化一个值，这样只需关注添加元素即可。
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['a'].append(4)

    d2 = defaultdict(set)
    d2['a'].add(1)
    d2['a'].add(2)
    d2['a'].add(4)
    d2['a'].add(1)

    print(d2['a'])

    # 讨论
    # 使用defaultdict后代码清晰的多。如：
    d3 = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)