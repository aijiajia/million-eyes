#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: mnist.py
@time: 17-9-16 下午7:54
"""


import os
import sys
import numpy as np
import matplotlib.pyplot as plt


caffe_root = '/home/herbert/caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe
MODEL_FILE = '/home/herbert/caffe/examples/mnist/lenet.prototxt'
PRETRAINED = '/home/herbert/caffe/examples/mnist/lenet_iter_10000.caffemodel'
IMAGE_FILE = '81.bmp'
input_image = caffe.io.load_image(IMAGE_FILE,color=False)
net = caffe.Classifier(MODEL_FILE,PRETRAINED)
prediction = net.predict([input_image], oversample = False)
caffe.set_mode_cpu()
print 'predicted_class: ', prediction[0].argmax()












