#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0701编写可接受任意数量参数的函数.py
@time: 2017/10/10 10:50
"""
# 问题：接受任意数量参数
# 解决： *开头形参


# rest 是一个元组，包含了所有传过来的参数
def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))


# 如果要接受任意数量的关键字参数，可以使用**开头。

def anyargs(*args, **kwargs):
    print(args)  # A tuple
    print(kwargs)  # A dict

if __name__ == '__main__':
    print(avg(1, 2))


# 讨论 ： *开头的参数只能作为最后一个【位置参数】出现。
#        **开头的参数只能作为最后的参数出现
#         这样的参数称为 keyword-only参数。即出现在*args之后的参数只能作为关键参数使用。
