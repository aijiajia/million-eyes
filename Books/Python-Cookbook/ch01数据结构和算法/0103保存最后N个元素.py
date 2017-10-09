#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0103保存最后N个元素.py
@time: 2017/10/8 9:45
"""

# 问题： 我们希望在迭代或是其他形式的处理过程中，对最后几项记录做一个有限的历史记录
# 解决： collections.deque
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    # text = 'hello world, python'
    # if 'python' in text:
    #     print('-'*20)
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)