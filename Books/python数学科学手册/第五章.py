#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 第五章.py
@time: 2018/9/29 15:29
"""


def demo01():
    import seaborn as sns
    iris = sns.load_dataset('iris')
    print(iris.head())


if __name__ == '__main__':
    demo01()