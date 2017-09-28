#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: ch04-demo.py
@time: 2017/9/20 11:10
"""

import tensorflow as tf
from numpy.random import RandomState
import matplotlib.pyplot as plt
# a = tf.constant([[1.0, 2.0],[6.0, 7.0]], name="a")
# # b = tf.constant([2.0, 3.0], name="b")
# c = tf.reduce_mean(a)

batch_size = 8
x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')
w1 = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w1)
loss_less = 1
loss_more = 10
loss = tf.reduce_sum(tf.where(tf.greater(y, y_),
                              (y - y_) * loss_more,
                              (y_ - y) * loss_less))
train_step = tf.train.AdamOptimizer(0.001).minimize(loss)

# 模拟数据集
rdm = RandomState(1)
dataset_size = 4
X = rdm.rand(dataset_size, 2)
#每一个元素是一个列表
Y = [[x1 + x2 + rdm.rand() / 10.0 - 0.05] for (x1, x2) in X]
#就一个列表
# Y2 = [x1 + x2 + rdm.rand() / 10.0 - 0.05 for (x1, x2) in X]
where_v = tf.where(1==2,2,3)

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    STEPS = 5000
    print(sess.run(where_v))

    # for i in range(STEPS):
    #     start = (i * batch_size) % dataset_size
    #     # start = i * batch_size
    #     end = min(start + batch_size, dataset_size)
    #     sess.run(train_step,
    #              feed_dict={x: X[start:end], y_: Y[start:end]})
    #     # print(w1.eval())
    #     # print("-------")
    #     print(sess.run(w1))
    #     # print(w1.eval())
    #




