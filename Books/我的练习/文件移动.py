#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 文件移动.py
@time: 2019/6/20 12:06
"""
import shutil
import os

# Move src to dst (mv src dst)
src = r'D:\kk\07-四大维度解锁 Webpack 前端工程化\project'
dst = r'D:\kk\07-四大维度解锁 Webpack 前端工程化\pptx'


def func(src,dst):
    for root, dirs, files in os.walk(src, topdown=False):
        for name in files:
            if name.endswith('.pptx'):
                shutil.move(os.path.join(root, name), dst)
                print(name)


if __name__ == '__main__':
    func(src,dst)
