#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0513获取目录内容的列表.py
@time: 2017/10/10 10:00
"""
# 问题： 获得目录下文件列表
# 解决： os.listdir()
# 如果要筛选数据使用列表推导式
import os.path


def func():
    pass


if __name__ == '__main__':
    path = 'C:\\测试\\图片'
    # print(path)
    # names = os.listdir(path)
    # print(names)
    file_names = [os.path.join(path, name) for name in os.listdir(path)
                  if os.path.isfile(os.path.join(path,name))]
    # print(file_names)
    dir_names = [os.path.join(path, name) for name in os.listdir(path)
                 if os.path.isdir(os.path.join(path, name))]
    print(dir_names)

    py_files = [name for name in os.listdir(path) if name.endswith('.py')]

    # 文件名的匹配，可能会想到使用glob 或者 fnmatch 模块

    import glob
    pyfiles = glob.glob('somedir/*.py')

    from fnmatch import fnmatch
    pyfiles = [name for name in os.listdir(path) if fnmatch(name, '*.py')]
