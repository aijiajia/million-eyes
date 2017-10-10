#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: 0105实现优先级队列.py
@time: 2017/10/8 9:45
"""
# 问题：想要实现一个队列，它能够以给定的优先级来对元素排序，且每次pop操作时都会返回优先级最高的元素。
# 解决：heapq;
# 优先级相同时，返回顺序按照插入顺序
import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def size(self):
        return len(self._queue)


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # !r 为占位内容添加单引号包裹
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 4)
    q.push(Item('spam'), 1)
    for i in range(q.size()):
        print(q.pop())