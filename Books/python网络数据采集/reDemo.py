#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: reDemo.py
@time: 2018/8/8 17:14
"""
import re


def func():
    pass


if __name__ == '__main__':
    # pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
    # string = 'Its after 12 noon, do you know where your rooftops are? http://tinyurl.com/NYCRooftops '
    # url = re.findall(pattern, string)
    # print(url)
    # pattern = r'(http.*)/\d+\.html'
    # string = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/11/1101.html"
    # matchList = re.findall(pattern, string)
    # print(matchList)
    # match = re.search(pattern,string)
    # print(match.groups())

    result = re.findall("a\+","a+")
    print(result)