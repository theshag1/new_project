from tkinter import *
from datetime import *
from translate import Translator
import csv


def translate():
    transaltor = Translator(from_lang=lan1.get(), to_lang=lan2.get())
    transalation = transaltor.translate(var1.get())
    var2.set(transalation)
    with open('new_data_transllate.csv', 'a') as f:
        lst = [var1.get(), var2.get(), datetime.now()]
        file = csv.writer(f)
        file.writerow(lst)

def clouse():
    target.destroy()



target = Tk()
target.title('Translate ')
target['background'] = 'black'


main = Frame(target)
main.grid(column=0, row=0, sticky=(N, W, E, S))
main.columnconfigure(0, weight=4)
main.rowconfigure(0, weight=1)
main.pack(pady=50, padx=90)




lan1 = StringVar(target)
lan2 = StringVar(target)

chose = {'English', 'Afrikaans', 'Arabic', 'Armenian', 'Uzbek' , 'Tajik' , 'Tatar', 'Hindi' , 'Gujarati' ,'Korean' , 'Chinese' ,'Russian' ,'Japanese' , 'Kannada',
         'Italian' ,'Indonesian' ,'Sanskirt', 'Kazakh' , 'Khmer' , 'Turkish' ,'Turkmen' , 'Portuguese' ,'Kurdish' , 'Dutch' ,'Odia' ,'Ukrainian' ,'Urdu'}
lan1.set('English')

lan1menu = OptionMenu(main, lan1, *chose)
Label(main, text="Select a language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)

lan2menu = OptionMenu(main, lan2, *chose)
Label(main, text='').grid(row=2, column=1)
lan2menu.grid(row=1, column=2)

Label(main, text='enter text :').grid(row=2, column=0)
var1 = StringVar()
enterr = Entry(main, textvariable=var1).grid(row=2, column=1)

Label(main, text='out pout').grid(row=2, column=2)
var2 = StringVar()
enter = Entry(main, textvariable=var2).grid(row=2, column=3)
a = Button(main, text='Translate ', command=translate).grid(row=3, column=1, columnspan=3)
b =Button(main , text='Exit',command=clouse ,width=10).grid(row=5 , column=12 , columnspan=5)

target.mainloop()
