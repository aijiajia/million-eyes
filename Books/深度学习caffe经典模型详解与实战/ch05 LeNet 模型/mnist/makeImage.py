#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: makeImage.py
@time: 17-9-16 下午8:20
"""

from PIL import Image
import PIL.ImageOps
im = Image.open("/home/herbert/Pictures/81.jpg")
im = im.resize((28,28))
im = im.convert("1")
im = im.convert("RGB")
im = PIL.ImageOps.invert(im)
im = PIL.ImageOps.invert(im)
print im.format, im.size, im.mode
im.save("81.bmp","bmp")