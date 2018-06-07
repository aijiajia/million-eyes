#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: 直方图.py
@time: 18-6-7 下午3:11
"""

from matplotlib.pyplot import *


def word_count(dataset):
    wc = {}
    for x in dataset:
        if x in wc.keys():
            wc[x] += 1
        else:
            wc[x] = 1
        sorted_wc=sorted(wc.items(), key=lambda x: x[0], reverse=True)
    print(sorted_wc)

if __name__ == "__main__":
    dataset = [113, 115, 119, 121, 124,
               124, 125, 126, 126, 126,
               127, 127, 128, 129, 130,
               130, 131, 132, 133, 136]
    word_count(dataset)
    subplot(121)
    subplot(122)
    hist(dataset)

    show()
