from tkinter import *
from pytube import YouTube

def saver():
    YouTube(var1.get()).streams.first().download()


target = Tk()
target.title('You tube saver')
target.geometry(f'500x500')

name = Label(target , text='Entr link ')
name.place(x=12 , y=1)


var1 = StringVar()
enter = Entry(target , width=55 , textvariable=var1)
enter.place(x=92 , y=1)

ad_btn = Button(target,text='↓', command=saver , width=3)
ad_btn.place(x=460 , y=1)




if __name__ == '__main__':
    target.mainloop()

