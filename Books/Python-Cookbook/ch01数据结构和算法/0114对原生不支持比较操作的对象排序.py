#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0114对原生不支持比较操作的对象排序.py
@time: 2017/10/7 22:22
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    # 相当于toString方法
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users= [User(23),User(3),User(99)]
# 使用lambda 排序
sorted_users = sorted(users, key=lambda u: u.user_id)
# print(sorted_users)  # 输出：[User(3), User(23), User(99)]

# 使用attgetter排序
sorted_users_attgetter = sorted(users, key=attrgetter('user_id'))
print(sorted_users_attgetter)