from tkinter import *

rot =Tk()
rot.title('translat')
rot.geometry('500x500')

lan = StringVar(rot)
enter = Entry(rot , width=22)
enter.grid(row=1 , column=3)



ad = Button(rot , text='add' ).grid(row=3 , column=12)

rot.mainloop()