#!/usr/bin/env python
# encoding: utf-8


"""
@version: v1.0
@author: Lieb
@license: Apache Licence 
@software: PyCharm
@file: menu.py
@time: 18-5-31 下午5:19
"""

import sys
import os
from notebook import Notebook, Note


class Memu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_memu(self):
        print("""
        Notebook Memu
        
        
        
        1.Show all Notes
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit  
        """)


def show_notes():
    pass


def search_notes():
    pass


def add_note():
    pass


def modify_note():
    pass


def quit():
    pass

class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    m = Memu()
    m.display_memu()
    print(os.getcwd())
