#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: 0402创建和使用字典.py
@time: 18-6-9 下午6:52
"""

# 字典方法：
# 1.clear
# 2.copy
# 3.fromkeys
# 4.get
# 5.has_key
# 6.items iteritems
# 7.keys iterkeys
# 8.pop
# 9.popitem
# 10.setdefault
# 11.update
# 13.values itervalues

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    # 创建字典
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    # print(a == b == c == d == e)
    f= zip(['one', 'two', 'three'], [1, 2, 3])
    print(type(f))





















