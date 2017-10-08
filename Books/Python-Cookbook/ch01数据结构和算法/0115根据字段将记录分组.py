#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0115根据字段将记录分组.py
@time: 2017/10/7 23:08
"""
from operator import itemgetter
from itertools import groupby
from collections import defaultdict



rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]
# 改变自己排序后。
rows.sort(key=itemgetter('date'))
# print(rows)


# 按date分组返回(key,values),一对多。
# 注意：
# groupby() 只能检查连续的项，不首先排序的话，无法按所想的方式排序。
# for date, items in groupby(rows, key=itemgetter('date')):
    # print(date)
    # for i in items:
    #     # print(' ', i)


# 讨论
# 如果只是简单根据日期将数据分组到一起，放进一个大的数据结构中以允许进行随机访问
# 那么利用defaultdict()构建一个一键多值字典可能会更好。

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)