#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: mysql56Demo.py
@time: 2018/8/9 11:44
"""
import pymysql


def read_data():
    pass


def insert_data(title,contents):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='herbert', db='scrping', charset='utf8')
    cur = conn.cursor()
    cur.execute("select * from pages")
    print(cur.fetchone())
    sql = "INSERT INTO pages (title, content) VALUES ('%s','%s')" % (title, contents)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    insert_data("中文标题2","文档内容2")

