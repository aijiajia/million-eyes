#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: 0223列表python的苦力.py
@time: 18-6-10 上午9:58
"""


# 2.3.1list函数
# 因为字符串不能像列表一样被修改，所以有时根据字符串创建列表会有用。
def str2list(str):
    print(list(str))


# 列表转字符串
def list2str(lst, separator=''):
    print(separator.join(lst))


# 2.3.2 列表的基本操作
# 改变列表：元素赋值
def list_change_value():
    x = [1, 1, 1]
    x[1] = 2
    print(x)


# 删除元素
def delete_element():
    x = [1, 2, 3]
    del x[2]
    print(x)


# 分片赋值
def slice_value():
    name = list('perl')
    print(name)
    name[2:] = list('ar')
    print(name)


# 分片替换
def slice_replace():
    name = list('perl')
    print(name)
    name[1:] = list('ython')
    print(name)


# 分片删除
def slice_delete():
    num = [i for i in range(1, 6)]
    print(num)
    num[1:4] = []
    print(num)


# 分片插入
def slice_insert():
    num = [1, 5]
    print(num[1:1])
    num[1:1] = [2, 3, 4]
    print(num)


if __name__ == "__main__":
    # str2list("hello")
    list_change_value()
    delete_element()
    slice_value()
    slice_replace()
    slice_delete()
    slice_insert()
