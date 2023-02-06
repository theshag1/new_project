from tkinter import *
import json
import requests
from time import strftime
import csv
from datetime import datetime
from tkinter import messagebox
import tkinter as tk

KEY = 'gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR'
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"

resp = requests.get(url)

target = Tk()
target.title('Exchange')
target.geometry('500x300')
target.config(background='#ADD8E6')

lan1 = StringVar()
lan2 = StringVar()

with open('new_test.json', 'w') as f:
    json.dump(json.loads(resp.text), f)

with open('new_test.json') as f:
    a = json.load(f)
    chose = a.get('data')


def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)


def exchange():
    if lan1.get() == 'USD':
        a = lan2.get()
        d = chose.get(a)
        s = var1.get()
        s = int(s)
        all = s * d
        all = str(all)
        var2.set(all)
    else:
        a = lan1.get()  # AUD
        d = chose.get(a)  # 1.444
        s = var1.get()  # 100
        s = float(s)
        all = s / d
        all = str(all)
        var2.set(all)


def exitt():
    target.destroy()


def clear():
    name.delete(0, END)


def save():
    with open('saveexchange.csv', 'a') as f:
        lst = [var1.get(), lan1.get(), '->', var2.get(), lan2.get(), datetime.now()]
        file = csv.writer(f)
        file.writerow(lst)


def warning():
    answer = messagebox.askyesno('eror', 'you are under 18 years of age ?')
    if answer:
        toot = tk.Tk()
        toot.title('registiration')
        w, h = 400, 500
        toot.geometry(f'{w}x{h}')

        task_name = tk.Label(toot, text='Fullname')
        task_name.place(x=20, y=10)

        task_entr = tk.Entry(toot, width=22)
        task_entr.place(x=100, y=10)

        task_name2 = tk.Label(toot, text='Email')
        task_name2.place(x=20, y=40)

        task_entr2 = tk.Entry(toot, width=22)
        task_entr2.place(x=100, y=40)

        task_name3 = tk.Label(toot, text='AGE')
        task_name3.place(x=20, y=70)

        task_entr3 = tk.Entry(toot, width=22)
        task_entr3.place(x=100, y=70)

        task_name4 = tk.Label(toot, text='Gander')
        task_name4.place(x=20, y=100)

        task_entr4 = tk.Entry(toot, width=22)
        task_entr4.place(x=100, y=100)

        task_name5 = tk.Label(toot, text='Phone')
        task_name5.place(x=20, y=130)
        var12 = StringVar()
        task_entr5 = tk.Entry(toot, width=22, textvariable=var12)
        var12.set(lan2.get())
        task_entr5.place(x=100, y=130)

        task_name6 = tk.Label(toot, text='Exchange ')
        task_name6.place(x=20, y=160)

        task_entr6 = tk.Entry(toot, width=22)
        task_entr6.place(x=100, y=160)

        def save():
            with open('new_save.csv', 'a') as f:
                header = ['name', 'email', 'dob', 'gander', 'phone', 'course', 'data joined']
                lst = [task_entr.get(),
                       task_entr2.get(),
                       task_entr3.get(),
                       task_entr4.get(),
                       task_entr5.get(),
                       task_entr6.get(),
                       datetime.now()]
                file = csv.writer(f)
                file.writerow(header)
                file.writerow(lst)

        def clear():
            task_entr.delete(0, END)
            task_entr2.delete(0, END)
            task_entr3.delete(0, END)
            task_entr4.delete(0, END)
            task_entr5.delete(0, END)
            task_entr6.delete(0, END)

        add_btn = tk.Button(toot, text='SAVE', command=save).place(x=50, y=200)
        add_btn2 = tk.Button(toot, text='Add', command=save).place(x=100, y=200)
        add_btn3 = tk.Button(toot, text='Clear', command=clear).place(x=150, y=200)
        add_btn4 = tk.Button(toot, text='Exit', command=toot.destroy).place(x=200, y=200)


lbl = Label(target, font=('calibri', 20, 'bold'),
            background='#FFA07A',
            foreground='white')

lbl.pack(anchor='center')

menu = OptionMenu(target, lan1, *chose).place(x=70, y=60, width=140)
lan1.set('From')
menu2 = OptionMenu(target, lan2, *chose).place(x=300, y=60, width=140)
lan2.set('To')
var1 = StringVar()
name = Entry(target, textvariable=var1, width=22)
name.place(x=70, y=100)

var2 = StringVar()
name2 = Entry(target, textvariable=var2, width=22).place(x=300, y=109)

ad_btn = Button(target, text='↹', width=10, command=exchange, ).place(x=200, y=140)
exiT_bt = Button(target, text='Exit', command=exitt).place(x=300, y=250)
clear_btn = Button(target, text='Clear', command=clear).place(x=450, y=100)
save.info = Button(target, text='Save(info)', command=save).place(x=200, y=250)
WARNING = Button(target, text='Exchange', command=warning).place(x=100, y=250)
time()
if __name__ == '__main__':
    target.mainloop()
