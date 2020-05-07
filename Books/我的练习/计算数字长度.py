#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 计算数字长度.py
@time: 2020/3/4 8:59
"""

def score_kun():
    # 在家办公 1- 7号
    s1 = ((100/21)*6*0.5)
    print (s1)
    # 在家办公10-21
    s2=((100 / 21) * 10 * 0.7)
    print(s2)
    # 公司办公
    s3=((100 / 21) * 2)
    print(s3)
    print("总分：" + str(s1+s2+s3-10))
def score_kang():
    s1 = ((100/21)*6*0.5)
    s2 = ((100/21)*15*0.7)
    print(s1+s2)

def score_fang():
    # 在家办公 1- 7号
    print ((100/21)*6*0.5)
    # 在家办公10-18
    print((100/21)*7*0.7)
    # 公司办公
    print((100/21)*8)

    print("总分："+ str(((100/21)*7*0.7)+((100/21)*8)+((100/21)*6*0.5)))
    # 扣分项


if __name__ == '__main__':
    score_fang()