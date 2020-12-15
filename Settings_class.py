from tkinter import *
from Option_class import Option
from tkinter import filedialog

player_avatar = 'images for spidergame//images//spider.png'
bot_avatar = 'images for spidergame//images//bot.png'
map1_lives = 3
map2_lives = 2
map3_lives = 1


class Settings(Toplevel):
    def __init__(self, **kw):
        super().__init__()
        self.title('Настройки')
        self.geometry('600x700')
        self.resizable(False, False)

        def b1():
            def open_picture():
                global player_avatar
                player_avatar = filedialog.askopenfile()

            form = Option(title='Персонаж')
            form.but1 = Button(form, text='выбрать картинку для персонажа', font='Tahoma 18', width=30, command=open_picture)
            form.but1.place(relx=0.15, rely=0.4)

        def b2():
            def open_picture():
                global bot_avatar
                bot_avatar = filedialog.askopenfile()

            form = Option(title='Бот')
            form.but1 = Button(form, text='выбрать картинку для бота', font='Tahoma 18', width=30, command=open_picture)
            form.but1.place(relx=0.15, rely=0.4)

        def b3():
            form = Option(title='Жизни')
            form.l1 = Label(form, text='Жизней для уровня 1', font='Tahoma 18,')  # дописать

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