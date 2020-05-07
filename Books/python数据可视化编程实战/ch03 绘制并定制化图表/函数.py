#!/usr/bin/env python
# encoding: utf-8


"""
@version:
@author: Herbert
@license: Apache Licence
@contact:
@site:
@software: PyCharm Community Edition
@file: 0303-简单的正弦图与余弦图.py
@time: 2017/10/14 10:39
"""

from pylab import *
import numpy as np

# generate uniformly distributed
# 256 points from -pi to pi, inclusive
x = np.linspace(0, 3000, 256, endpoint=True)

# these are vectorised versions
# of math.cos, and math.sin in built-in Python maths
# compute cos for every x
y = 1000 * x

# compute sin for every x
y1 = x ** 2

# plot cos
plot(x, y)

# plot sin
plot(x, y1)

show()
