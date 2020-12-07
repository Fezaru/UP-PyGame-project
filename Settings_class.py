from tkinter import *
from Option_class import Option


class Settings(Toplevel):
    def __init__(self, **kw):
        super().__init__()
        self.title('Настройки')
        self.geometry('600x700')
        self.resizable(False, False)

        def b1():
            Option(title='Персонаж')

        def b2():
            Option(title='Бот')

        def b3():
            Option(title='Жизни')

        def b4():
            Option(title='Время прохождения')

        def b5():
            Option(title='Карта')

        def b6():
            Option(title='Движение бота')

        def b7():
            Option(title='Бомба')

        buts = [Button(self, justify=CENTER, font='Tahoma 24', width=26) for i in range(7)]
        x = 0.1
        y = 0.05
        for i in range(7):
            buts[i].place(relx=x, rely=y)
            y += 0.13
        buts[0]['text'] = 'Персонаж'
        buts[0]['command'] = b1
        buts[1]['text'] = 'Бот'
        buts[1]['command'] = b2
        buts[2]['text'] = 'Жизни'
        buts[2]['command'] = b3
        buts[3]['text'] = 'Время прохождения'
        buts[3]['command'] = b4
        buts[4]['text'] = 'Карта'
        buts[4]['command'] = b5
        buts[5]['text'] = 'Движение бота'
        buts[5]['command'] = b6
        buts[6]['text'] = 'Бомба'
        buts[6]['command'] = b7