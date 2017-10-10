#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0112找出序列中出现次数最多的元素.py
@time: 2017/10/8 9:47
"""
# 问题： 我们有一个元素序列， 想知道在序列中出现次数最多的元素是什么。
# 解决： collections Counter类
from collections import Counter
import copy


def func():
    pass


if __name__ == '__main__':
    words = [
        'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes'
    ]
    word_counts = Counter(words)
    word_counts_copy = copy.deepcopy(word_counts)
    top3 = word_counts.most_common(3)
    print(top3)
    print(word_counts['eyes'])
    word_counts['eyes'] = 10
    print(word_counts['eyes'])
    print(word_counts)
    print(word_counts_copy)
    print(word_counts - word_counts_copy)
    print(word_counts + word_counts_copy)
