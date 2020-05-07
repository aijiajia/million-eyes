#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: Contacts.py
@time: 2019/6/14 12:02
"""


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __str__(self):
        return '{0}  {1}'.format(self.name, self.email)

    def all_print(self):
        all_str = []
        for user in self.all_contacts:
            all_str.append(str(self))
        print(all_str)


def func():
    c1 = Contact("zs", "zhangssan@163.com")
    c2 = Contact("ls", "lisi@163.com")
    c1.all_print()



if __name__ == '__main__':
    func()
