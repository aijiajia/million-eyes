#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 2.2日历转换.py
@time: 2019/5/22 11:19
"""

import string
# 1-3 是没有th结尾的
# [First, second, third,]
# 4-20是有th结尾的 共计17个
# [fourth, fifth, sixth, seventh, eighth, ninth, tenth，Eleventh, twelfth,
# thirteenth, fourteenth, fifteenth, sixteenth, seventeenth,
# Eighteenth, nineteenth, twentieth]
# 21-23 不是th结尾的
# [twenty-first, twenty-second, twenty-third]
# 24-30是th结尾共计7个
# [twenty-fourth, twenty-fifth,Twenty-sixth, twenty-seventh, twenty-eighth，twenty-ninth, thirtieth]
# 31first结尾
# [ thirty-first]


def func():
    year = input("年:")
    month = input("月:")
    day = input("日:")
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
    month_number = int(month)
    day_number = int(day)

    month_day_year = month_list[month_number - 1] +' '+ day + endings[day_number - 1] + '. ' + year
    print(month_day_year)


if __name__ == '__main__':
    # ['th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th', 'th']
    # print(17*["th"])
    func()
    string.letters
