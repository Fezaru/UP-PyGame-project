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
            self.destroy()
            Game_class.Game((300, 300))  # Пока что 6x6, потом добавить настройку этого

        self.title('Меню')
        self.geometry('600x500')
        self.resizable(False, False)

        self.background_image = PhotoImage(file=r'images for spidergame/images/menuBG.png')
        self.background_fil = PhotoImage(file=r'images for spidergame/images/gameBGfilled.png')

        background_label = Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.play = Button(self, text='Играть', justify=CENTER, font='Tahoma 24', width=26, background='#B6A99C',
                           command=igrat)
        self.play.place(relx=0.1, rely=0.1)

        self.settings = Button(self, text='Настройки', justify=CENTER, font='Tahoma 24', width=26, background='#B6A99C',
                               command=nastroiki)
        self.settings.place(relx=0.1, rely=0.3)

        self.exit = Button(self, text='Выйти', justify=CENTER, font='Tahoma 24', width=26, background='#B6A99C',
                           command=viiti)
        self.exit.place(relx=0.1, rely=0.7)
