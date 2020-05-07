#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 递归修改文件名.py
@time: 2019/9/21 14:16
"""

import os, re


class Ren:

    def __init__(self, file_dir):

        self.file_dir = file_dir
        # self.new_str = new_str

    def file_name(self):
        L = []
        if os.path.exists(self.file_dir):
            for root, dirs, files in os.walk(self.file_dir):
                for file in files:
                    # if os.path.splitext(file)[1] == '.success':
                    L.append(os.path.join(root, file))
            return L
        else:
            print('文件夹不存在！！')

    def ren_name(self):

        for file in self.file_name():
            try:
                # new_str = re.compile('.success')
                # str = new_str.sub('', file)
                str = file.replace('江门政务大数据管理平台','天水智慧城管')
                print(str)
                os.rename(file, str)
                print('%s修改成功！！！' % file)
            except(FileExistsError):
                print('%s文件已存在' % str)
            continue


if __name__ == '__main__':
    FILE_DIR = r'D:\work\天水\项目管理-天水项目\项目验收文档创我科技'
    ren = Ren(FILE_DIR)
    files = ren.file_name()
    # for file in files:
    #     print(file)
    ren.ren_name()