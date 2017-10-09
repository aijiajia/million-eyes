#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0104找到最大或最小的N个元素.py
@time: 2017/10/8 9:45
"""

# 问题： 我们想在某个集合中找到最小或者最大的N个元素
# helpq 模块中有两个函数 nlargest() nsmallest()
import heapq


if __name__ == '__main__':
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # 这两个函数都可以接受一个函数key,从而允许他们工作在更加复杂的数据结构之上。例如：
    portfolio = [
        {'name': '', 'shares': '', 'price': 543.22},
        {'name': '', 'shares': '', 'price': 21.09},
        {'name': '', 'shares': '', 'price': 31.75},
        {'name': '', 'shares': '', 'price': 16.35},
        {'name': '', 'shares': '', 'price': 115.65},
        {'name': '', 'shares': '', 'price': 91.1}
    ]
    cheap3 = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive3 = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(expensive3)
