from tkinter import *
from Option_class import Option
from tkinter import filedialog
import os

player_avatar = 'images for spidergame//images//spider.png'
bot_avatar = 'images for spidergame//images//bot.png'
map1_lives = 3
map2_lives = 2
map3_lives = 1
map1_timer = None  # так впадлу в класс пихать ваще жесть)
map2_timer = None
map3_timer = None
bot_timer = 1
bomb_timer = 1


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
            def set_health():
                global map1_lives
                global map2_lives
                global map3_lives
                map1_lives = int(form.e1.get())
                map2_lives = int(form.e2.get())
                map3_lives = int(form.e3.get())

            form = Option(title='Жизни')
            form.l1 = Label(form, text='Жизней для уровня 1', font='Tahoma 18')
            form.l1.place(relx=0.15, rely=0.3)
            form.e1 = Entry(form)
            form.e1.place(relx=0.6, rely=0.32)

            form.l2 = Label(form, text='Жизней для уровня 2', font='Tahoma 18')
            form.l2.place(relx=0.15, rely=0.4)
            form.e2 = Entry(form)
            form.e2.place(relx=0.6, rely=0.42)

            form.l3 = Label(form, text='Жизней для уровня 3', font='Tahoma 18')
            form.l3.place(relx=0.15, rely=0.5)
            form.e3 = Entry(form)
            form.e3.place(relx=0.6, rely=0.52)

            form.b = Button(form, text='Задать', font='Tahoma 18', width=10, command=set_health)
            form.b.place(relx=0.4, rely=0.7)

        def b4():
            def set_time():
                global map1_timer
                global map2_timer
                global map3_timer
                map1_timer = int(form.e1.get())
                map2_timer = int(form.e2.get())
                map3_timer = int(form.e3.get())

            form = Option(title='Время прохождения')
            form.l1 = Label(form, text='Время для уровня 1', font='Tahoma 18')
            form.l1.place(relx=0.15, rely=0.3)
            form.e1 = Entry(form)
            form.e1.place(relx=0.6, rely=0.32)

            form.l2 = Label(form, text='Время для уровня 2', font='Tahoma 18')
            form.l2.place(relx=0.15, rely=0.4)
            form.e2 = Entry(form)
            form.e2.place(relx=0.6, rely=0.42)

            form.l3 = Label(form, text='Время для уровня 3', font='Tahoma 18')
            form.l3.place(relx=0.15, rely=0.5)
            form.e3 = Entry(form)
            form.e3.place(relx=0.6, rely=0.52)

            form.b = Button(form, text='Задать', font='Tahoma 18', width=10, command=set_time)
            form.b.place(relx=0.4, rely=0.7)

        def b5():
            def open_map1():
                command_string = 'notepad.exe Map1.txt'
                os.system(command_string)

            def open_map2():
                pass

            def open_map3():
                pass

            form = Option(title='Карта')
            form.but1 = Button(form, text='Задать карту 1', font='Tahoma 18', width=30,
                               command=open_map1)
            form.but1.place(relx=0.15, rely=0.3)

            form.but2 = Button(form, text='Задать карту 2', font='Tahoma 18', width=30,
                               command=open_map2)
            form.but2.place(relx=0.15, rely=0.4)

            form.but3 = Button(form, text='Задать карту 3', font='Tahoma 18', width=30,
                               command=open_map3)
            form.but3.place(relx=0.15, rely=0.5)

        def b6():
            def set_bot_timer():
                global bot_timer
                bot_timer = float(form.e2.get())

            form = Option(title='Движение бота')
            form.l2 = Label(form, text='Время передвижения бота', font='Tahoma 18')
            form.l2.place(relx=0.1, rely=0.4)
            form.e2 = Entry(form)
            form.e2.place(relx=0.62, rely=0.42)

            form.b = Button(form, text='Задать', font='Tahoma 18', width=10, command=set_bot_timer)
            form.b.place(relx=0.4, rely=0.6)

        def b7():
            def set_bomb_timer():
                global bomb_timer
                bomb_timer = float(form.e2.get())

            form = Option(title='Бомба')
            form.l2 = Label(form, text='Время взрыва бомбы', font='Tahoma 18')
            form.l2.place(relx=0.1, rely=0.4)
            form.e2 = Entry(form)
            form.e2.place(relx=0.62, rely=0.42)

            form.b = Button(form, text='Задать', font='Tahoma 18', width=10, command=set_bomb_timer)
            form.b.place(relx=0.4, rely=0.6)

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