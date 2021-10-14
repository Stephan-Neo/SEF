import tkinter as tk
import random as ran
import time
import webbrowser

win = tk.Tk()
win.title("Камень-Ножницы-Бумага")
win.geometry("500x700+300+100")
win.resizable(False, False)

# переменные
paper = tk.PhotoImage(file="image/inst/paper.png")
kulak = tk.PhotoImage(file="image/inst/kulak.png")
noj = tk.PhotoImage(file="image/inst/noj.png")
otjim = tk.PhotoImage(file='image/tasks/otjim.png')
nog = tk.PhotoImage(file='image/tasks/nog.png')
rast = tk.PhotoImage(file='image/tasks/rast.png')
suprast = tk.PhotoImage(file='image/tasks/suprast.png')
palec = tk.PhotoImage(file='image/tasks/palec.png')
pod = tk.PhotoImage(file='image/tasks/podt.png')
almaz = tk.PhotoImage(file='image/tasks/almaz.png')
tai = True
count = 0
wan_vs_obj = ''
wan_obj = ''
num_1 = 0
num_2 = 0

win.iconphoto(False, almaz)


def paper_f():
    global tai, wan_obj
    label_paper = tk.Label(win, image=paper,
                           background='cyan').place(x=10, y=250)
    wan_obj = 'paper'
    disabled()
    # tai = False


def kulak_f():
    global tai, wan_obj
    locals()
    label_paper = tk.Label(win, image=kulak,
                           background='cyan').place(x=10, y=250)
    wan_obj = 'kulak'
    disabled()
    # tai = False


def noj_f():
    global tai, wan_obj
    locals()
    label_paper = tk.Label(win, image=noj,
                           background='cyan').place(x=10, y=250)
    wan_obj = 'noj'
    disabled()
    # tai = False


def random_object():
    global wan_vs_obj, vs_obj
    list_obj = [kulak, noj, paper]
    list_wan = ['kulak', 'noj', 'paper']
    num = ran.randint(0, 2)
    vs_obj = list_obj[num]
    wan_vs_obj = list_wan[num]


def print_vs_obj():
    locals()
    label_obj = tk.Label(win, image=vs_obj,
                         background='red').place(x=335, y=250)


def print_number():
    locals()
    for i in range(0, 4).__reversed__():
        label_num = tk.Label(win, text=i,
                             font=('Arial', 50, 'bold'), ).place(x=380, y=270)
        time.sleep(0.8)
        win.update()
    print_vs_obj()
    label_ag = tk.Button(win, text="Заново",
                         command=again,
                         font=('Arial', 20, 'bold'),
                         background='cyan',
                         activebackground='cyan',
                         cursor="hand2",).place(x=10, y=630)
    # вызов фнкции результата
    winter()


def again():
    for w in win.winfo_children():
        if w.winfo_class() == 'Label' or w.winfo_class() == 'Button':
            w.destroy()
    game()


def print_rez(string):
    locals()
    label_rez = tk.Label(win, text=string,
                         font=('Arial', 20, 'bold'), background=bg_rez).place(x=160, y=420)


def lose_task():
    global num_1
    tasks('Ты с треском провалился,\n'
          'так что выполняй задание:')
    list_lose_img = [nog, otjim, rast, suprast, pod]
    r = ran.randint(0, 4)
    print_lose_img = list_lose_img[r]
    label_task = tk.Label(win, image=print_lose_img).place(x=300, y=490)
    if r == 0:
        num_1 = 15
    if r == 1:
        num_1 = 20
    if r == 2:
        num_1 = 10
    if r == 3:
        num_1 = 15
    if r == 4:
        num_1 = 10
    label_num = tk.Label(win, text='x' + str(num_1), font=('Arial', 20, 'bold')).place(x=60, y=560)


def nic_task():
    global num_2
    tasks('Хорошо, но не отлично,\n'
          'так что выполняй задание:\n'
          '(на 5 меньше чем при проигроше)')
    list_lose_img = [nog, otjim, rast, suprast, pod]
    r = ran.randint(0, 4)
    print_lose_img = list_lose_img[r]
    label_task = tk.Label(win, image=print_lose_img).place(x=300, y=490)
    if r == 0:
        num_2 = 10
    if r == 1:
        num_2 = 15
    if r == 2:
        num_2 = 5
    if r == 3:
        num_2 = 10
    if r == 4:
        num_2 = 5
    label_num = tk.Label(win, text='x' + str(num_2), font=('Arial', 20, 'bold')).place(x=60, y=560)


def win_task():
    label_task = tk.Label(win, image=palec).place(x=300, y=490)
    label_g = tk.Label(win, text='Так держать!!!', font=('Arial', 30, 'bold')).place(x=10, y=500)


def winter():
    global bg_rez, rew
    bg_rez = ''
    # логика бумаги
    if wan_obj == 'paper' and wan_vs_obj == 'paper':
        bg_rez = 'yellow'
        print_rez("Ничья :)")
        nic_task()

    if wan_obj == 'paper' and wan_vs_obj == 'kulak':
        bg_rez = 'cyan'
        print_rez('Победа!!! :)')
        win_task()

    if wan_obj == 'paper' and wan_vs_obj == 'noj':
        bg_rez = 'red'
        print_rez('Вы проиграли :(')
        lose_task()

    # логика камня
    if wan_obj == 'kulak' and wan_vs_obj == 'kulak':
        bg_rez = 'yellow'
        print_rez('Ничья :)')
        nic_task()

    if wan_obj == 'kulak' and wan_vs_obj == 'noj':
        bg_rez = 'cyan'
        print_rez('Победа!!! :)')
        win_task()

    if wan_obj == 'kulak' and wan_vs_obj == 'paper':
        bg_rez = 'red'
        print_rez('Вы проиграли :(')
        lose_task()

    # логика ножниц
    if wan_obj == 'noj' and wan_vs_obj == 'noj':
        bg_rez = 'yellow'
        print_rez('Ничья :)')
        nic_task()

    if wan_obj == 'noj' and wan_vs_obj == 'paper':
        bg_rez = 'cyan'
        print_rez('Победа!!! :)')
        win_task()

    if wan_obj == 'noj' and wan_vs_obj == 'kulak':
        bg_rez = 'red'
        print_rez('Вы проиграли :(')
        lose_task()


def disabled():
    global count
    locals()
    random_object()
    count += 1
    if count >= 1:
        btn_paper['state'] = tk.DISABLED
        btn_kulak['state'] = tk.DISABLED
        btn_noj['state'] = tk.DISABLED
        label_vs = tk.Label(win, text='VS', font=('Arial', 30, 'bold')).place(x=225, y=280)
        win.after(10, print_number)


def tasks(rew):
    label_tasks = tk.Label(win, text=rew, font=('Arial', 13, 'bold')).place(x=10, y=500)


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


def game():
    global btn_paper, btn_kulak, btn_noj
    locals()
    while tai:
        label_m = tk.Label(win, text='Выберете оружие', font=('Arial', 20, 'bold'), ).pack()
        label_y = tk.Label(win, text=r'https://gtsk.site/', font=('Arial', 15, 'bold'),
                           foreground='cyan', cursor="hand2")
        label_y.place(x=330, y=660)
        label_y.bind("<Button-1>", callback)
        btn_paper = tk.Button(win, text='',
                              command=paper_f,
                              image=paper,
                              cursor="hand2",
                              )

        btn_kulak = tk.Button(win, text='',
                              image=kulak,
                              command=kulak_f,
                              cursor="hand2",
                              )

        btn_noj = tk.Button(win, text='',
                            image=noj,
                            command=noj_f,
                            cursor="hand2",
                            )
        btn_paper.place(x=10, y=50)
        btn_kulak.place(x=175, y=50)
        btn_noj.place(x=335, y=50)

        win.mainloop()


game()
