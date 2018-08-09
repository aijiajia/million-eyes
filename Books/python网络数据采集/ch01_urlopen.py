#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: ch01_urlopen.py
@time: 2018/8/8 10:47
"""
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import re


def getHtml(url):
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url, headers=head)
    try:
        return (urlopen(req))
    except HTTPError as e:
        print(e)
        return None


def writeLines(filenmae, lines):
    fp = open(filenmae, "a", encoding='utf-8')
    # fp = open(filenmae, "a")
    for line in lines:
        fp.write(line)
        fp.write('\n')
    fp.close()


def getProvince(url):
    html = getHtml(url)
    if (html is not None):
        bsObj = BeautifulSoup(html.read(), "html.parser")
        trs = bsObj.findAll("tr", {"class": "provincetr"})
        provinces = []
        print(len(trs))
        for tr in trs:
            tds = tr.findAll(name="td")
            for td in tds:
                # print(td.get_text())
                provinces.append(td.get_text())
        writeLines("provinces.txt", provinces)
    else:
        print("html is None!")


def getCity(url):
    html = getHtml(url)
    if (html is not None):
        bsObj = BeautifulSoup(html.read(), "html.parser")
        trs = bsObj.findAll("tr", {"class": "citytr"})
        citys = []
        print("cityCount:",len(trs))
        for tr in trs:
            tds = tr.findAll(name="td")
            text = tds[0].get_text() + ',' + tds[1].get_text()
            citys.append(text)
        writeLines("citys.txt", citys)
        for city in citys:
            print("city",city)
    else:
        print("html is None!")


def getCounty(url):
    html = getHtml(url)
    if (html is not None):
        bsObj = BeautifulSoup(html.read(), "html.parser",from_encoding="gb18030")
        trs = bsObj.findAll("tr", {"class": "countytr"})
        countys = []
        print("countyCount:",len(trs))
        for tr in trs:
            tds = tr.findAll(name="td")
            # text = tds[0].string + ',' + tds[1].string
            text = tds[0].get_text() + ',' + tds[1].get_text()
            # for td in tds:
            #     print(td.get_text())
            # text=td[0].get_text()+','+td[1].get_text()
            print(tds[1].get_text())
            countys.append(text)
        writeLines("countys.txt", countys)
        for county in countys:
            print("county:",county)
    else:
        print("html is None!")


def getCountyLinkList(url):
    pattern = re.compile(r'(http.*/)\d+\.html')
    matchList = re.findall(pattern, url)
    if matchList:
        pre_string = matchList[0]
    linkList = set()
    html = getHtml(url)
    if (html is not None):
        bsObj = BeautifulSoup(html.read(), "html.parser")
        for link in bsObj.find_all('a'):
            # print(link.get('href'))
            linkList.add(pre_string + link.get('href'))
        return linkList


    else:
        print("html is None!")
        return None


def getProvinceLinkList(url):
    linkList = set()
    html = getHtml(url)
    if (html is not None):
        bsObj = BeautifulSoup(html.read(), "html.parser")
        for link in bsObj.find_all('a'):
            # print(link.get('href'))
            linkList.add(url + link.get('href'))
        return linkList


    else:
        print("html is None!")
        return None


if __name__ == '__main__':

    # 拿到全国各省数据
    getProvince(r"http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/")
    # 拿到各省链接
    ProvinceLinkList = getProvinceLinkList(r"http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/")
    if ProvinceLinkList:
        # 拿到各市数据
        for provice in ProvinceLinkList:
            getCity(provice)
            # 拿到各县链接
            countyLinkList = getCountyLinkList(provice)
            # 拿到各县数据
            if countyLinkList:
                for county in countyLinkList:
                    getCounty(county)

