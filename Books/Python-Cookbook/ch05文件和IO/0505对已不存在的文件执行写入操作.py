#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0505对已不存在的文件执行写入操作.py
@time: 2017/10/10 9:51
"""
# 问题： 我们想将数据写入到文件中，但只在文件不存在文件系统时才这么做。
# 解决： 1.open() x 模式（文本xt,二进制xb） 2. if 判断
import os


if __name__ == '__main__':
    # with open('somefile', 'wt') as f:
    #     f.write('0505Hello\n')
    #
    # with open('somefile', 'xt') as f:
    #     f.write('xt\n')

    if not os.path.exists('somefile'):
        with open('somefile') as f:
            f.write('Hello\n')
    else:
        print("file is exists")