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
            "1": self.show_notes
            # "2": self.search_notes,
            # "3": self.add_note,
            # "4": self.modify_note,
            # "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Memu
        
        
        
        1.Show all Notes
        2.Search Notes
        3.Add Note
        4.Modify Note
        5.Quit  
        """)

    def run(self):
        """Display the menu and repond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        return None

    def add_note(self):
        return None

    def modify_note(self):
        return None

    def quit(self):
        return None


if __name__ == "__main__":
    Memu().run()

    # choice = input("Enter an option: ")
    # choices = {
    #     "1": "a",
    #     "2": "b"
    # }
    # print(choices.get(choice))
