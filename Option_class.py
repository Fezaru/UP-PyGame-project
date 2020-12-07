from tkinter import *


class Option(Toplevel):
    def __init__(self, **kw):
        super().__init__()
        self.title(kw['title'])
        self.geometry('600x500')
        self.resizable(False, False)