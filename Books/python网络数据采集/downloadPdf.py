#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: downloadPdf.py
@time: 2018/8/9 10:54
"""

from urllib.request import urlretrieve
from urllib.request import urlopen
def func():
    pass


if __name__ == '__main__':
    urlretrieve("https://downloads.mysql.com/docs/refman-5.6-en.pdf","mysql.pdf")