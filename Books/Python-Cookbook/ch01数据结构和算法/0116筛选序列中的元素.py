#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0116筛选序列中的元素.py
@time: 2017/10/7 23:16
"""
import math
from itertools import compress


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':

    # 问题： 序列中有一些数据，我们需要提取其中的值或者根据某些标准对序列做删减
    # 方案1: 列表推导式
    # 缺点： 如果输入非常大将会返回一个庞大的结果

    myList = [1, 4, -5, 10, -7, 2, 3, -1]
    positive_number = [n for n in myList if n > 0]
    # print(positive_number)

    # 方案2： 生成器表达式
    pos = (n for n in myList if n > 0)
    # print(pos)  # 输出 <generator object <genexpr> at 0x0000000000A18150>

    # 方案3： filter
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    # 注意list转换
    ivals = list(filter(is_int, values))
    # print(ivals)

    # 讨论1 使用列表推导转换数据
    sqrt_num = [math.sqrt(n) for n in myList if n > 0]
    # 输出：[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]
    # print(sqrt_num)

    # 讨论2 替换不满足条件的值
    clip_neg = [n if n > 0 else 0 for n in myList]
    # 输出： [1, 4, 0, 10, 0, 2, 3, 0]
    # print(clip_neg)

    # 讨论3 itertools.compress() ，它接受一个可迭代对象以及一个布尔选择器序列作为输入。
    # 输出时，给出所有在相应的布尔选择器中为True的可迭代元素。
    # 如果想把对一个序列的筛选结果施加到另一个相关的序列上时，这会非常有用。
    # rows = [
    #     {'address': '5412 N CLARK', 'date': '07/01/2012'},
    #     {'address': '5148 N CLARK', 'date': '07/04/2012'},
    #     {'address': '5800 E 58TH', 'date': '07/02/2012'},
    #     {'address': '2122 N CLARK', 'date': '07/03/2012'},
    #     {'address': '5645 RAVENSWOOD', 'date': '07/02/2012'},
    #     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    #     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    #     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
    # ]
    # address = []
    # for r in rows:
    #     address.append(r['address'])
    # print(len(address))
    addr = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE'
    ]
    # print(len(addr))

    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    # more5: [False, False, True, False, False, True, True, False]
    more5 =[n > 5 for n in counts]
    # 注意转换为list
    addr_more5 = list(compress(addr,more5))
    print(addr_more5)