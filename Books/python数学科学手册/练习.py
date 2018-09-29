#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: 练习.py
@time: 2018/9/21 15:03
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def demo01():
    import seaborn as sns;
    sns.set(style="ticks", color_codes=True)

    # 通过Series和字典创建DF
    population_dict = {'California': 38332521,
                       'Texas': 26448193,
                       'New York': 19651127,
                       'Florida': 19552860,
                       'Illinois': 12882135,
                       'shanghai':12882135,
                       'gz':12882135}
    population = pd.Series(population_dict)
    area_dict = {'California': 423967,
                 'Texas': 695662,
                 'New York': 141297,
                 'Florida': 170312,
                 'Illinois': 149995,
                 'shanghai':149995,
                       'gz':149995
                 }
    kinds = pd.Series({'California': 'a',
                       'Texas': 'b',
                       'New York': 'c',
                       'Florida': 'd',
                       'Illinois': 'e',
                       'shanghai': 'f',
                       'gz': 'g'
                       })
    area = pd.Series(area_dict)
    states = pd.DataFrame({'population': population, 'area': area,'kinds':kinds})
    print(states)
    # iris = sns.load_dataset("iris")
    # g = sns.pairplot(iris, hue="species", palette="husl")
    g = sns.pairplot(states, hue="kinds", palette="husl")
    plt.show()


if __name__ == '__main__':
    demo01()
