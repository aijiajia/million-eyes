#!/usr/bin/env python
# encoding: utf-8


"""
@version:
@author: Herbert
@license: Apache Licence
@contact:
@site:
@software: PyCharm Community Edition
@file: ch03-start.py
@time: 2017/9/12 16:41
"""

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

#
# #3.1 计算图定义计算
# a = tf.constant([1.0, 2.0], name="a")
# b = tf.constant([2.0, 3.0], name="b")
# result = a + b
# print(result)
# #3.2 张量
# #三个属性： name, shape,type
#
# #3.3 会话（运行模型）执行计算
#
#
# with tf.Session() as sess:
#     print(sess.run(result))

# 3.4.3 神经网络参数与TensorFlow变量
# #声明w1 w2 两个变量。这里还通过seed参数设定了随机种子
# #这样可以保证每次运行得到结果是一样的
#
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
w3 = tf.Variable(tf.truncated_normal([2], stddev=0.1))
b2 = tf.Variable(tf.constant(0.1, shape=[10]))

# 暂时将输入定义一个常量。1*2 的矩阵

x = tf.constant([[0.7,0.9]])

# 计算神经网络的输出
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
# page55
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    # print(sess.run(y))
    # print(b2.eval())
    # plt.plot(np.transpose(w3.eval()))
    # plt.show()
    print(8)



