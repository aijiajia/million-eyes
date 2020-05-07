#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 删除文件.py
@time: 2019/6/5 14:02
"""
import os
import re


def remove_files(path):
    file_list = os.listdir(path)
    for file in file_list:
        if re.match(r'.*201904.*.docx', file) and (not file.find("水务") >= 0):
            print(file)


def remove_files2(path):
    file_list = os.listdir(path)
    for file in file_list:
        if file.endswith(".exe"):
            os.remove(os.path.join(path,file))
            print(os.path.join(path,file))


if __name__ == '__main__':
    remove_files2(r"D:\myspace\study\37大前端教程\02 CSS3\08 CSS背景及应用")
    # print(re.match(r'a\.c', "a.c").group())
