#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 修改文件名.py
@time: 2019/5/21 10:43
"""
import os


def rename_java1234(path):
    file_list = os.listdir(path)
    for files in file_list:
        old_dir = os.path.join(path, files)
        new_dir = os.path.join(path, files.replace('@www.java1234.com', '').replace('[www.java1234.com]', '').replace(
            'www.java1234.com', ''))
        if new_dir != old_dir:
            os.rename(old_dir, new_dir)
            print(old_dir, '======>', new_dir)


def rename_project(path):
    file_list = os.listdir(path)
    for files in file_list:
        old_dir = os.path.join(path, files)
        new_dir = os.path.join(path, files.replace('@www.java1234.com', ''))
        if new_dir != old_dir:
            os.rename(old_dir, new_dir)
            print(old_dir, '======>', new_dir)

def rename_kejichaxin(path):
    file_list = os.listdir(path)
    for files in file_list:
        old_dir = os.path.join(path, files)
        new_dir = os.path.join(path, files.replace('创我家宽精准营销支撑系统', '创我大数据分析服务平台—灵狐'))
        os.rename(old_dir, new_dir)
        print(old_dir, '======>', new_dir)


if __name__ == '__main__':
    # rename('C:\\Users\\herbert\\Downloads')
    # rename('D:\\movie')
    # rename('D:\\文档')
    # rename_kejichaxin('D:\\work\\科技查新20190603\\4、参照样本：创我家宽精准营销支撑系统项目')
    rename_java1234('D:\myspace\【但行好事，莫问前程】\Java')
