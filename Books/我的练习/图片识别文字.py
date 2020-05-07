#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 图片识别文字.py
@time: 2019/6/4 9:07
"""

import os


def get_results(result_folder, img_folder):
    """
    Parameters
    ----------
    result_folder: results directory
    img_folder: image directory
    """
    # Windows
    # cmd = 'cmd.exe /k tesseract.exe ' + img + 'result -l chi_sim+eng'

    # OS X

    # cmd = 'tesseract ' + img + ' result -l chi_sim'

    img_list = os.listdir(img_folder)
    os.chdir(img_folder)
    for i in range(0, len(img_list)):
        if os.path.isfile(img_list[i]) and img_list[i].endswith('.PNG'):
            result_file = ' %s-result' % (img_list[i].split('.')[0])
            print(result_file)
            print('tesseract ' + img_list[i] + result_file + ' -l chi_sim')
            cmd = 'tesseract.exe ' + img_list[i] + result_file + ' -l chi_sim'
            output = os.popen(cmd)
            print(output.read())


if __name__ == '__main__':
    # D:\work\长沙县应急项目
    # get_results("D:\\work\\长沙县应急项目", "D:\\work\\长沙县应急项目")
    get_results(r'D:\work\甘肃省自然灾害监测预警体系与应急管理指挥系统项目\toword',r'D:\work\甘肃省自然灾害监测预警体系与应急管理指挥系统项目\toword')
