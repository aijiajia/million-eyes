#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 日期和时间数据类型及工具.py
@time: 2018/9/4 15:12
"""
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import pandas as pd


def demo01():
    now = datetime.now()
    print(now)
    print(now.year, now.month, now.day)
    # datetime以毫秒形式存储日期和时间。datetime.timedelta表示两个datetime对象之间的时间差。
    delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
    print(delta)
    print(delta.days)
    print(delta.seconds)
    print(56700 / (60 * 60))
    a = timedelta(hours=2)
    print(a)

    start = datetime(2011, 1, 7)
    print(start + timedelta(12))


def demo02():
    stamp = datetime(2011, 1, 3)
    print(str(stamp))
    print(stamp.strftime('%Y-%m-%d'))
    #     转换日期
    value = '2011-01-04'
    a = datetime.strptime(value, '%Y-%m-%d')
    print('中文: %s' % str(a))


def demo03():
    a = parse('2011-1-03')
    print(a)
    b = parse('6/12/2011', dayfirst=True)  # 这个参数很不错
    print(b)


def demo04():
    datestrs = ['7/6/2011', '8/6/2011']
    pddate=pd.to_datetime(datestrs)
    print(pddate)


if __name__ == '__main__':
    demo04()
