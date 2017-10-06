#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: mnistTrain.py
@time: 2017/9/18 10:42
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST数据集相关的常数
INPUT_NODE = 784
OUTPUT_NODE = 10

# 配置神经网络的参数
LAYER1_NODE = 500

BATCH_SIZE = 100  # 一个训练BATCH中的训练数据个数，数字越小越接近随机梯度下降，越大越接近梯度下降。
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99  # 学习率的衰减率
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 30000  # 训练轮数
MOVING_AVERAGE_DECAY = 0.99  # 滑动平均衰减率


# 一个辅助函数，给定神经网络的输入和所有参数，计算神经网络的前向传播结果。
# 定义ReLU激活函数实现了去线性化。
# 在这个函数中也支持传入用于计算参数平均值的类，这样方便在测试时使用滑动平均模型。


def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    # 当没有提供滑动平均类时，直接使用参数当前的取值。
    if avg_class is None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)
        return tf.matmul(layer1, weights2) + biases2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(weights1)) + avg_class.average(biases1))
        return tf.matmul(layer1, avg_class.average(weights2)) + avg_class.average(biases2)


def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')
    # 生成隐藏层的参数
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    # 784个0.1
    biases1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
    # 784*10 的矩阵
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    # 10个 0.1
    biases2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))

    # 计算在当前参数下神经网络向前传播的结果
    # 进行模型计算，y是预测，y_ 是实际
    y = inference(x, None, weights1, biases1, weights2, biases2)

    # 定义存储训练轮数的变量。这个变量不需要计算滑动平均值，所以这里指这个变量为不可训练的变量（Trainable=False)。
    # 在使用TensorFlow训练网络时，一般会将代表训练轮数的变量指定为不可训练的参数。
    global_step = tf.Variable(0, trainable=False)

    #
    variable_average = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)

    # 在所有代表神经网络参数的变量上使用滑动平均。其他辅助变量（比如global_step)就不需要了。
    # tf.trainable_variables返回的就是图上集合GraphKeys.TRAINABLE_VARIABLES中的元素，这个集合的元素就是所有没有指定trainable=False的参数。
    variable_average_op = variable_average.apply(tf.trainable_variables())

    # 计算使用了滑动平均之后的前向传播结果。（参见第四章）
    average_y = inference(x, variable_average, weights1, biases1, weights2, biases2)

    # 计算交叉熵作为刻画预测值和真实值之间差距的损失函数。
    # 这里使用TF提供的sparse_softmax_cross_entropy_with_logits函数来计算交叉熵。
    # 当分类问题只有一个正确答案时，可以使用这个函数来加速交叉熵的计算。
    # MNIST问题的图片中只包含了0-9中的一个数字，所以可以使用这个函数来计算交叉熵的损失。
    # 这个函数的第一个参数是神经网络不包括softmax层的前向传播结果，第二个则是训练数据的正确答案。
    # 因为标准答案是一个长度为10的一维数组，而该函数需要提供的是一个正确答案的数字，所以需要使用tf.argmax函数来得到正确答案对应的类别编号。
    # [[1.  2.]
    #  [2.  3.]]
    # 返回 [1 1] 也就是索引号

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))

    # 计算在当前batch中所有样例的交叉熵平均值

    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    # 计算L2正则化损失函数
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)

    # 计算模型的正则化损失。一般只计算神经网络边上权重的正则化损失，而不使用偏置项。
    regularization = regularizer(weights1) + regularizer(weights2)

    # 总损失等于交叉熵损失和正则化损失的和
    loss = cross_entropy_mean + regularization

    # 设置指数衰减的学习率 exponential:指数
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE, global_step, mnist.train.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY)

    # 使用tf.train.GradientDescentOptimizer优化算法来优化损失函数
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

    # 在训练神经网络模型时，每过一遍数据即需要通过反向传播来更新神经网络中的参数
    # 又要更新每一个参数的滑动平均值，为了一次完成多个操作，TF提供了 tf.control_dependencies 和 tf.group 两种机制
    # 下面两行程序和train_op = tf.gourp(train_step, variables_averages_op) 是等价的。
    with tf.control_dependencies([train_step, variable_average_op]):
        train_op = tf.no_op(name='train')

    # 检验使用了滑动平均模型的神经网络前向传播结果是否正确。
    # tf.argmax(average_y, 1) 计算每一个样本的预测答案，其中average_y是一个batch_size * 10 的二维数组
    # 每一行表示一个样例的前向传播结果。tf.argmax的第二个参数“1”表示选取最大值的操作仅在第一个维度中进行，也就是说，只在每一行选取最大值对应的下标。
    # 于是得到一个长度为batch的一维数组。这个一维数组中的值就表示了每一个样例对应的数字识别结果。
    # tf.equal判断两个张量的每一维是否相等，相等返回True，不等返回False.

    # tf.reduce_mean(x) == > 2.5  # 如果不指定第二个参数，那么就在所有的元素中取平均值
    # tf.reduce_mean(x, 0) == > [2., 3.]  # 指定第二个参数为0，则第一维的元素取平均值，即每一列求平均值
    # tf.reduce_mean(x, 1) == > [1.5, 3.5]  # 指定第二个参数为1，则第二维的元素取平均值，即每一行求平均值

    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 初始化会话并开始训练过程
    with tf.Session() as sess:
        # tf.initialize_all_variables().run()
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        # 准备验证数据。一般在神经网络训练过程中会通过验证数据来大致判断停止的条件和评判训练的结果。
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}

        test_feed = {x: mnist.test.images,
                     y_: mnist.test.labels}

        # 迭代训练
        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print("After %d training step(s),validation accuracy"
                      "using average model is %g " % (i, validate_acc))

            # 产生这一轮使用的一个batch的训练数据，并运行训练过程。
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})

        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print("After %d training step(s),test accuracy"
              "using average model is %g " % (TRAINING_STEPS, test_acc))


def main(argv=None):
    mnist = input_data.read_data_sets("./data/MNIST_data/", one_hot=True)
    train(mnist)


if __name__ == '__main__':
    tf.app.run()
