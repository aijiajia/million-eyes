#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: python对象.py
@time: 18-5-29 下午3:42
"""


# 类的命名必须符合标准的python变量命名规则（必须以字母或者下划线开头，名字中只能包含字母、下划线或者数字）

def func():
    pass


class MyFirstClass:
    # def __init__(self):
    #     pass
    pass


class Point:
    def reset(self):
        self.x = 0
        self.y = 0


if __name__ == "__main__":
    # print("hello world")
    # a = MyFirstClass()
    # b = MyFirstClass()
    # print(a)
    # print(b)
    p1 = Point()
    p1.x = 5
    p1.y = 4
    p1.reset()
    print(p1.x,p1.y)
    Point.reset(p1)
    print(p1.x)
