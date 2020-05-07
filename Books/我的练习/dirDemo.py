#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: dirDemo.py
@time: 2020/3/3 13:26
"""


import sys,os

def func():
    dir = 'D:\\work\\天水\\创我-项目管理-天水项目'
    a = [{'00管理':['项目计划','会议纪要','项目周报']},{'01需求':['资料收集','调研报告','需求变更']},{'02设计':['概要设计','详细设计']},{'03开发':['开发指南','程序设计']},{'04测试':['测试用例','测试报告']},{'05发布':['部署环境','发布记录']},{'06实施':['用户培训','数据初始化','运维情况']},{'07验收':['验收文档']}]
    for d in a:
        for key in d:
            for child in d[key]:
                path = os.path.join(dir,key,child)
                if(os.path.exists(path)):
                    print("文件夹已存在")
                print (path)
                os.makedirs(path)

def func2():
    dir = 'D：\\work\\天水\\创我-项目管理-天水项目'
    os.makedirs(os.path.join(dir,'新目录'))

if __name__ == '__main__':
    func()