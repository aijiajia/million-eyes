#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 数字生成.py
@time: 2019/5/22 11:15
"""




def func3(args, step):
    list = [x + step for x in args]
    for number, y in enumerate(list):
        print(number+1, y)



if __name__ == '__main__':
    # a=[1,14,48,53,82,97,120,136]
    # pages = [1, 22, 54, 91, 147, 232]
    # func3(pages,9)
    # a = [1,21,37,63,75,97,127,163,193,213]
    # a = [1,65,115,186,208,228,270,322,347,396,415,435]
    # func3(a, 24)
    a= [1,25,71,107,137,171,201,223,261]
    func3(a,20)