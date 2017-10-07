#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: ch04滑动平均模型.py
@time: 2017/10/7 14:21
"""

# shadow_variable = decay * shadow_variable + (1 - decay) * variable
# decay(衰减率) min{decay,(1 + num_updates)/(10 + num_updates)}

import tensorflow as tf

# 定义一个变量用于计算滑动平均，这个变量的初始值是0.注意这里手动指定了变量的
# 类型为 float32,因为所有需要计算滑动平均的变量必须是实数型。
v1 = tf.Variable(0, dtype=tf.float32)
# 定义step变量模拟神经网络迭代次数，可以用于动态控制衰减率。
step = tf.Variable(0, trainable=False)

# 定义一个滑动平均的类(class)，初始化时给定了衰减率(0.99)和控制衰减率的变量step。
ema = tf.train.ExponentialMovingAverage(0.99, step)
# 定义一个更新变量滑动平均的操作。这里需要给定一个列表，每次执行这个操作时
# 这个列表中的变量都会被更新
maintain_averages_op = ema.apply([v1])

with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    # 通过ema.average(v1) 获取滑动平均之后变量的取值。
    # 在初始化之后变量v1的值和v1的滑动平均都为0。
    # 输出：[0.0, 0.0]
    # print(sess.run([v1, ema.average(v1)]))

    # 更新v1的值到5
    sess.run(tf.assign(v1, 5))
    # print(sess.run([v1, ema.average(v1)]))

    # 更新v1的滑动平均值。
    # 衰减率为 min{0.99,(1 + step)/(10 + step)}=0.1
    # v1 的滑动平均值为 0.1 * 0 + 0.9 * 5 = 4.5
    sess.run(maintain_averages_op)
    # print(sess.run([v1, ema.average(v1)])) # 输出[5.0, 4.5]

    # 更新step值为10000
    sess.run(tf.assign(step, 10000))
    # 更新v1的值为10
    sess.run(tf.assign(v1, 10))
    # 此时衰减率 min{0.99,(1 + 10000)/(10 + 10000)}=0.99
    # 此时滑动平均  0.99 * 4.5 + 0.01 * 10 = 4.555
    sess.run(maintain_averages_op)
    # print(sess.run([v1, ema.average(v1)]))  # 输出[10.0, 4.5549998]

    # 再次更新滑动平均值
    sess.run(maintain_averages_op)
    print(sess.run([v1, ema.average(v1)])) # 输出[10.0, 4.6094499]
