#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0113 通过公共键对字典列表排序.py
@time: 2017/10/7 21:39
"""

# 问题：有一个列表，想根据一个或多个字典中的值来对列表排序
# 方案：使用operator模块中的itemgetter函数对这类结构进行排序是非常简单的。

from operator import itemgetter
rows = [
    {'fname':'Brian','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1001},
    {'fname':'Big','lname':'Jones','uid':1004}
]

# 按fname排列
rows_by_name = sorted(rows, key=itemgetter('fname'))
# 按uid排序
rows_by_uid = sorted(rows, key=itemgetter('uid'))
# 取最小的uid
min_uid = min(rows, key=itemgetter('uid')) # 输出： {'lname': 'Cleese', 'uid': 1001, 'fname': 'John'}

# 可以接受多个键值
rows_by_lfname = sorted(rows, key=itemgetter('fname','lname'))

# 讨论：
# 在这个例子中，rows被传递给内建的sorted()函数，该函数接受一个关键字参数key。
# 这个参数应该代表一个可调用对象(callable)，该对象从rows中接收一个单独的元素作为输入
# 并返回一个用来做排序依据的值。

# 函数operator.itemgetter()接受的参数为查询标记，用来从rows的记录提取出所需的值。
# 它可以是字典的键名称、用数字表示的列表元素或者是任何可以对象的__getitem__() 方法的值。
# 如果传给多个标记给itemgetter(),那么它产生的对象将返回一个包含所有元素的元组。
# 然后sorted将根据对元组的排序结果来排序输出结果。


# 有时候用lambda表达式来取代itemgetter()的功能。例如：
rows_by_name = sorted(rows, key=lambda r:r['fname'])
rows_by_lfname = sorted(rows, key=lambda r:(r['fname'],r['lname']))

# lambda 表达式性能要低于itemgetter()

# 不仅可以使用在sorted函数中，也可以使用在min、max函数中