#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 字符串练习题.py
@time: 2019/5/22 15:00
"""


def func():
    # 使用字符串的内置方法a.swapcase()：
    a = 'aAsmr3idd4bgs7Dlsf9eAF'
    print(a)
    tab = str.maketrans('aA', 'Aa')
    aa = a.translate(tab)
    print(aa)


if __name__ == '__main__':
    func()
