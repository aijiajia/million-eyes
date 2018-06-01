#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: notebook.py
@time: 18-5-31 下午5:18
"""
import datetime

# 为所有新的备注存储下一个可用的id
last_id = 0


class Note:
    """Represent a note in the notebook. Match against a string in searches and store tags for each note."""

    def __init__(self, memo, tags=''):
        """initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter text. Return True if it matches,False otherwise.
        Search is case sensitive and matches both text and tags."""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes that canbe tagged,modified ,and searched"""

    def __init__(self):
        """Initialize a note book with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(self, Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its mem to the given value"""
        for note in self.notes:
            if note_id == note.id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note_id == note.id:
                note.tags = tags
                break

    def search(self, filter):
        """Find all notes that match the given filter string"""
        return [note for note in self.notes if note.match(filter)]


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    n = Notebook
    n.new_note("hello world")
    # n.new_note("hello again", '')
    # print(n.notes[0].id)

