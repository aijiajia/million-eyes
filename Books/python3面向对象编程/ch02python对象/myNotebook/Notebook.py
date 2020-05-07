#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm
@file: Notebook.py
@time: 2019/6/13 14:00
"""
# 类级别公用
last_id = 0


class Note:

    def __init__(self, memo, tag=''):
        global last_id
        last_id += 1
        self.id = last_id
        self.memo = memo
        self.tag = tag

    def modify_memo(self, memo):
        self.memo = memo

    def match(self, filter_str):
        return filter_str in self.memo or filter_str in self.id


class Notebook:

    def __init__(self):
        self._notes = []

    def add_note(self, memo):
        self._notes.append(Note(memo))

    def modify_note(self, note_id, memo):
        self._find_note_by_id(note_id).memo = memo

    def _find_note_by_id(self, note_id):
        for note in self._notes:
            if note.id == note_id:
                return note
            else:
                return None

    def search_note(self, filter_str):
        return [note for note in self._notes if note.match(filter_str)]

    def get_notes(self):
        return self._notes


if __name__ == '__main__':
    n1 = Notebook()
    n1.add_note("hello--1")
    n1.add_note("hello--2")
    print(n1.get_notes())
