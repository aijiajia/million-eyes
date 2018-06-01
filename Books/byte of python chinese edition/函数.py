#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: 函数.py
@time: 18-6-1 上午11:07
"""

# global 关键字的使用
x = 50


def func():
    global x
    print('x is', x)
    x = 2
    print('x changed :', x)


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    func()
    print(x)