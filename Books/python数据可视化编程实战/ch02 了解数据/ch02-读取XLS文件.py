#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: ch02-读取XLS文件.py
@time: 2017/10/14 10:18
"""

import xlrd
from xlrd.xldate import XLDateAmbiguous

file = 'ch02-xlsxdata01.xlsx'

wb = xlrd.open_workbook(filename=file)

ws = wb.sheet_by_name('Sheet1')

dataset = []

for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r, c).value)
        if ws.cell_type(r, c) == xlrd.XL_CELL_DATE:
            try:
                print("#" * 20)
                print(ws.cell_type(r, c))
                from datetime import datetime

                date_value = xlrd.xldate_as_tuple(ws.cell(r, c).value, wb.datemode)
                print("####" * 50)
                # 星号变量的特殊用法http://python.jobbole.com/86589/
                print(*date_value)
                print(type(date_value))
                print(datetime(*date_value))
            except XLDateAmbiguous as e:
                print(e)
    dataset.append(col)

from pprint import pprint

pprint(dataset)
