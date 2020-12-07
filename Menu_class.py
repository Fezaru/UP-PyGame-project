from tkinter import *
from Settings_class import Settings
import Game_class


class Menu(Toplevel):
    def __init__(self, **kw):
        super().__init__()

        def viiti():
            self.master.destroy()

        def nastroiki():
            Settings()

        def igrat():
            Game_class.Game((300, 300)) # Пока что 6x6, потом добавить настройку этого

        self.title('Меню')
        self.geometry('600x500')
        self.resizable(False, False)
        self.play = Button(self, text='Играть', justify=CENTER, font='Tahoma 24', width=26, command=igrat)
        self.play.place(relx=0.1, rely=0.1)

        self.settings = Button(self, text='Настройки', justify=CENTER, font='Tahoma 24', width=26, command=nastroiki)
        self.settings.place(relx=0.1, rely=0.3)

        self.exit = Button(self, text='Выйти', justify=CENTER, font='Tahoma 24', width=26, command=viiti)
        self.exit.place(relx=0.1, rely=0.7)