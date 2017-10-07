#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0116筛选序列中的元素.py
@time: 2017/10/7 23:16
"""


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':


    # 问题： 序列中有一些数据，我们需要提取其中的值或者根据某些标准对序列做删减
    # 方案1: 列表推导式
    # 缺点： 如果输入非常大将会返回一个庞大的结果

    myList = [1, 4, -5, 10, -7, 2, 3, -1]
    positive_number = [n for n in myList if n > 0]
    # print(positive_number)

    # 方案2： 生成器表达式
    pos = (n for n in myList if n > 0)
    # print(pos)  # 输出 <generator object <genexpr> at 0x0000000000A18150>

    # 方案3： filter
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    # 注意list转换
    ivals = list(filter(is_int, values))
    print(ivals)