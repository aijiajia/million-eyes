# encoding: utf-8
"""
@author: monitor1379 
@contact: herbert_git@163.com
@site: www.monitor1379.com

@version: 1.0
@license: Apache Licence
@file: wapperlayer.py
@time: 18/6/19 下午8:37

这一行开始写关于本文件的说明与解释
"""
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    countdown(10000)
