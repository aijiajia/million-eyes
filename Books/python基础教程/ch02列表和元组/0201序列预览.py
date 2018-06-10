#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: 0201序列预览.py
@time: 18-6-10 上午9:17
"""
# 序列：python内建有6种：列表、元组、字符串、Unicode字符串、Buffer对象和Xrange对象。
# 使用元组通常是技术性的，与python内部运作方式有关，这也是内建函数返回元组的原因。
# 使用元组作为字典的键，因为键不能修改，所以不能使用列表。
"""
序列通用操作：索引、分片、加、乘、检查成员资格、序列长度、最大元素、最小元素。
"""

if __name__ == "__main__":
    # 2.2序列通用操作
    # 索引
    greeting = 'hello'
    # print(greeting[0])

    num = [i for i in range(1, 11)]
    print(num[-3:])
    num2 = num[:]
    num2[0] = 2
    print(num2[::-1])

    # 序列相加，连接两个列表。相同类型的序列才能相加
    print([1, 2] + [3, 4])

    # 序列相乘 生成新的重复序列
    print([10]*5)
