#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0511处理路径名.py
@time: 2017/10/10 10:00
"""
# 问题： 需要处理路径名、基文件名、目录名、决对路径名
# 解决： os.path
import os


def func():
    pass


if __name__ == '__main__':
    path = '/Users/beazley/Data/data.csv'
    print("basename: ", os.path.basename(path))
    print("dirname: ", os.path.dirname(path))
    # 从左到右
    print("join: ", os.path.join('tep','data', os.path.basename(path)))

    # 展开家目录
    path = '~/Data/data.csv'
    print("展开家目录", os.path.expanduser(path))

    # 分割文件拓展名
    print("分割文件拓展名 ", os.path.splitext(path))

    # 分割文件夹名字和文件名字
    print("分割文件夹名字和文件名字 ", os.path.split(path))
