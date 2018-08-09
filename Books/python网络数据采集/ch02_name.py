#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: ch02_name.py
@time: 2018/8/8 13:52
"""
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime


def func():
    pass


if __name__ == '__main__':
    try:
        html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    except HTTPError as e:
        print(e)
        exit(0)
    a = datetime.now()
    bsObj = BeautifulSoup(html.read(), "html.parser")
    nameList = bsObj.findAll("span", {"class": "green"})
    for name in nameList:
        print(name)
    b = datetime.now()
    runTime = (b - a).total_seconds()
    print("runtime: ", runTime)
