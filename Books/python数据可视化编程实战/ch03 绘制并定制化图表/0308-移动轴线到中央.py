#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0308-移动轴线到中央.py
@time: 2017/10/14 10:44
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 500, endpoint=True)
y = np.sin(x)

plt.plot(x, y)

ax = plt.gca()

# hide two spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# move bottom and left spine to 0,0
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# move ticks positions
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()
