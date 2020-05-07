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

    def say_hi(self):  # 加self区别于普通函数
        print('Hello, your name is?', self.name)

    @staticmethod  # 声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
    def say_name():  # 使用了静态方法，则不能再使用self
        print("sayName staticmethod ")  # ,grade,#self.name

    @classmethod  # 类方法
    def class_method(cls):
        print("class method")


if __name__ == '__main__':
    p = Person("king")
    p.say_hi()
    p.say_name()
    p.class_method()
    Person.class_method()
    Person.say_name()

