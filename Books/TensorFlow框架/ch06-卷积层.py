#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: ch06-卷积层.py
@time: 2017/10/13 12:10
"""
import tensorflow as tf

if __name__ == '__main__':
    # case 2
    input = tf.Variable(tf.random_normal([1, 3, 3, 1]))
    # filter = tf.Variable(tf.random_normal([1, 1, 5, 1]))
    # op2 = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='VALID')

    # op5 = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='SAME')
    # input = tf.Variable(tf.random_normal([1, 5, 5, 5]))
    # filter = tf.Variable(tf.random_normal([3, 3, 5, 7]))

    input = tf.constant([0, 2, 0, 2, 2, 0, 0, 1, 0], shape=[1, 3, 3, 1], dtype=tf.float32)
    filter = tf.constant([-1, -1, 1, -1, 0, 1, 1, 1, -1], shape=[3, 3, 1, 1], dtype=tf.float32)
    op3 = tf.nn.conv2d(input, filter, strides=[1, 1, 1, 1], padding='VALID')

    # 创建会话运行TensorFlow程序
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        # 初始化变量
        sess.run(init_op)
        # print("case 2")
        # print(input.get_shape)
        # print(sess.run(op2))
        # print(sess.run(input))
        # print(sess.run(filter))
        # print("case 5")
        print(sess.run(op3))
        print(sess.run(op3).shape)
