#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 第三章栗子.py
@time: 2018/9/29 9:32
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()


def demo01():
    data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
    print(data.head())
    data.columns = ['West', 'East']
    data['Total'] = data.eval('West + East')
    print(data.dropna().describe())
    data.plot()
    plt.ylabel('Hourly Bicycle Count')
    plt.show()


def demo02():
    data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
    print(data.head())
    data.columns = ['West', 'East']
    data['Total'] = data.eval('West + East')
    print(data.dropna().describe())
    weekly = data.resample('W').sum()
    weekly.plot(style=[':', '--', '-'])
    plt.ylabel('Weekly bicycle count')
    plt.show()


def demo03():
    data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
    print('data.shape: ', data.shape)
    # print(data.head())
    data.columns = ['West', 'East']
    data['Total'] = data.eval('West + East')
    # print(data.dropna().describe())
    daily = data.resample('D').sum()
    # print(daily.head())
    # print(daily.shape)
    # daily.rolling(30, center=True).mean().plot(style=[':', '--', '-'])
    # plt.ylabel('mean of 30 days count')
    daily50 = daily.rolling(50, center=True, win_type='gaussian').sum(std=10)
    print(daily50.shape)
    print(daily50[:100])
    # daily.rolling(50, center=True,win_type='gaussian').sum(std=10).plot(style=[':', '--', '-'])
    # plt.show()


# 移动窗口
def demo04():
    df = pd.DataFrame({'key1': [3, 3, 3, 6, 6, 6],
                       'key2': ['one', 'two', 'one', 'two', 'one', 'two'],
                       'data1': [np.nan, np.nan, 'x1', 'x2', np.nan, 'x4'],
                       'data2': np.random.randn(6)})
    print(df)
    # print(df.rolling(window=3).count())
    print('*' * 100)
    print(df[['key1', 'data2']].rolling(window=4, center=True).mean())


# 窗口函数
def demo05():
    from scipy import signal
    from scipy.fftpack import fft, fftshift
    import matplotlib.pyplot as plt
    window = signal.gaussian(51, 7)
    print(window)


def demo06():
    data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
    # print(data.head())
    data.columns = ['West', 'East']
    data['Total'] = data.eval('West + East')
    by_time = data.groupby(data.index.time).mean()
    print(data.index.time.shape)
    print(data.index.time[:30])
    hourly_ticks = 4 * 60 * 60 * np.arange(6)
    by_time.plot(xticks=hourly_ticks, style=[':', '--', '-'])
    plt.show()


if __name__ == '__main__':
    demo06()
