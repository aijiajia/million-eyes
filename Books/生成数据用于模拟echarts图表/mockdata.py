#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: mockdata.py
@time: 2018/7/26 14:20
"""
import random


def mock_int(size, low, high):
    my_data = []
    for x in range(size):
        my_data.append(random.randint(low, high))
    return my_data


if __name__ == '__main__':
    data = mock_int(10, 100, 200)
    print(data)