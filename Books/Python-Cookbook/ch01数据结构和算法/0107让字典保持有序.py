#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0107让字典保持有序.py
@time: 2017/10/8 9:46
"""
# 问题： 我们想创建一个字典，同时当对字典迭代或者序列化操作时，也能控制其中的元素顺序。
# 解决： collections模块中的OrderedDict类。
from collections import OrderedDict
import json


def func():
    pass


if __name__ == '__main__':
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    # for key in d:
    #     print(key, d[key])

    print(json.dumps(d))

# 讨论： OrderedDict 维护了一个双向链表，他会根据元素加入的顺序来排列键的位置。
# 注意： OrderedDict 大小是普通的字典大小的两倍多，这是因为创建双向链表导致。所以大数据量时，要考虑性能。
