#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 利用pandas读写数据库.py
@time: 2020/4/17 9:10
"""
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

def func():
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
    engine = create_engine('mysql+pymysql://root:herbert@localhost:3306/scrping')
    # 查询语句，选出employee表中的所有数据
    sql = ''' select * from mydf; '''
    # read_sql_query的两个参数: sql语句， 数据库连接
    df = pd.read_sql_query(sql, engine)
    # 输出employee表的查询结果
    print(df)

    # 新建pandas中的DataFrame, 只有id,num两列
    df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
    # 将新建的DataFrame储存为MySQL中的数据表，储存index列
    df.to_sql('mydf', engine, index=True)
    print('Read from and write to Mysql table successfully!')


def func2():
    # -*- coding: utf-8 -*-

    # 导入必要模块
    import pandas as pd
    from sqlalchemy import create_engine

    # 初始化数据库连接，使用pymysql模块
    db_info = {'user': 'root',
               'password': 'herbert',
               'host': 'localhost',
               'port': 3306,
               'database': 'manhole'
               }

    engine = create_engine(
        'mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info, encoding='utf-8')
    # 直接使用下一种形式也可以
    # engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test')

    # 读取本地CSV文件
    # df = pd.read_csv("C:\Users\herbert\Desktop\天水项目设备汇总表20191106.xls", sep=',')
    df = pd.read_excel("C:\\Users\\herbert\\Desktop\\天水项目设备汇总表20191106.xls",converters={u'IMEI号':str})
    #print(df)
    # 将新建的DataFrame储存为MySQL中的数据表，不储存index列(index=False)
    # if_exists:
    # 1.fail:如果表存在，啥也不做
    # 2.replace:如果表存在，删了表，再建立一个新表，把数据插入
    # 3.append:如果表存在，把数据插入，如果表不存在创建一个表！！
    pd.io.sql.to_sql(df, 'manhole', con=engine, index=False, if_exists='replace')
    # df.to_sql('example', con=engine,  if_exists='replace')这种形式也可以
    print("Write to MySQL successfully!")


if __name__ == '__main__':
    func2()
