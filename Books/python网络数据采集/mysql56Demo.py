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

def func():
    pass


if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='herbert',db='scrping',charset='utf8')
    cur = conn.cursor()
    # cur.execute("select * from pages where id=1")
    # print(cur.fetchone())
    title="中文标题"
    contents="中文内容"
    sql="INSERT INTO pages (title, content) VALUES ('%s','%s')"%(title, contents)
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

