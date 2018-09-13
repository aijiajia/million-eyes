#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 类方法实例方法静态方法.py
@time: 2018/9/10 14:31
"""


class Person:
    grade = 1

    def __init__(self, name):
        self.name = name

    def sayHi(self):  # 加self区别于普通函数
        print('Hello, your name is?', self.name)

    @staticmethod  # 声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
    def sayName():  # 使用了静态方法，则不能再使用self
        print("sayName staticmethod ")  # ,grade,#self.name

    @classmethod  # 类方法
    def classMethod(cls):
        print("class method")


if __name__ == '__main__':
    p = Person("king")
    p.sayHi()
    p.sayName()
    p.classMethod()
    Person.classMethod()
    Person.sayName()
