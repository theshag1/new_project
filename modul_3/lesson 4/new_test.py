import tkinter as tk
import csv

from datetime import *
from tkinter import ttk

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

task_name3 = tk.Label(toot, text='DOB')
task_name3.place(x=20, y=70)

task_entr3 = tk.Entry(toot, width=22)
task_entr3.place(x=100, y=70)

task_name4 = tk.Label(toot, text='Gander')
task_name4.place(x=20, y=100)

task_entr4 = tk.Entry(toot, width=22)
task_entr4.place(x=100, y=100)

task_name5 = tk.Label(toot, text='Phone')
task_name5.place(x=20, y=130)

task_entr5 = tk.Entry(toot, width=22)
task_entr5.place(x=100, y=130)

task_name6 = tk.Label(toot, text='Course')
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


add_btn = tk.Button(text='SAVE', command=save).place(x=50, y=200)
add_btn2 = tk.Button(text='Add', command=save).place(x=100, y=200)
add_btn3 = tk.Button(text='Clear', ).place(x=150, y=200)
add_btn4 = tk.Button(text='Exit', command=toot.destroy).place(x=200, y=200)

if __name__ == '__main__':
    toot.mainloop()
