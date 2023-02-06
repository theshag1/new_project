from tkinter import *
import json
import requests


def hourly():
    new_key = ''
    new_key = var1.get()
    KEY = 'ZQ48KUlOHW4H7bnsvgNlF02Z06kwKvoB'
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={new_key}&apikey={KEY}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers)
    with open('weather.json', 'w') as f:
        json.dump(json.loads(response.text), f)

    with open('weather.json') as f:
        a = json.load(f)
        nmadr = a.get('timelines')
        b = nmadr.get('hourly')

        data1 = b[0].get('time')
        data_time.set(data1)
        val = b[0].get('values')
        tem1 = val.get('temperature')
        temp_entr.set(tem1)

        data2 = b[1].get('time')
        data_time2.set(data2)
        val = b[1].get('values')
        tem2 = val.get('temperature')
        temp_entr2.set(tem2)

        data3 = b[2].get('time')
        data_time3.set(data3)
        val = b[2].get('values')
        tem3 = val.get('temperature')
        temp_entr3.set(tem3)

        data4 = b[3].get('time')
        data_time4.set(data4)
        val = b[3].get('values')
        tem4 = val.get('temperature')
        temp_entr4.set(tem4)

        data5 = b[4].get('time')
        data_time5.set(data5)
        val = b[4].get('values')
        tem5 = val.get('temperature')
        temp_entr5.set(tem5)

        data6 = b[5].get('time')
        data_time6.set(data6)
        val = b[5].get('values')
        tem6 = val.get('temperature')
        temp_entr6.set(tem6)

        data7 = b[6].get('time')
        data_time7.set(data7)
        val = b[6].get('values')
        tem7 = val.get('temperature')
        temp_entr7.set(tem7)

        data8 = b[7].get('time')
        data_time8.set(data8)
        val = b[7].get('values')
        tem8 = val.get('temperature')
        temp_entr8.set(tem8)

        data9 = b[8].get('time')
        data_time9.set(data9)
        val = b[8].get('values')
        tem9 = val.get('temperature')
        temp_entr9.set(tem9)

        data10 = b[9].get('time')
        data_time10.set(data10)
        val = b[9].get('values')
        tem10 = val.get('temperature')
        temp_entr10.set(tem10)

        data11 = b[10].get('time')
        data_time11.set(data11)
        val = b[10].get('values')
        tem11 = val.get('temperature')
        temp_entr11.set(tem11)

        data12 = b[11].get('time')
        data_time12.set(data12)
        val = b[11].get('values')
        tem12 = val.get('temperature')
        temp_entr12.set(tem12)

        data13 = b[12].get('time')
        data_time13.set(data13)
        val = b[12].get('values')
        tem13 = val.get('temperature')
        temp_entr13.set(tem13)

        data14 = b[13].get('time')
        data_time14.set(data14)
        val = b[13].get('values')
        tem14 = val.get('temperature')
        temp_entr14.set(tem14)

        data15 = b[14].get('time')
        data_time15.set(data15)
        val = b[14].get('values')
        tem15 = val.get('temperature')
        temp_entr15.set(tem15)

        data16 = b[15].get('time')
        data_time16.set(data16)
        val = b[15].get('values')
        tem16 = val.get('temperature')
        temp_entr16.set(tem16)

        data17 = b[16].get('time')
        data_time17.set(data17)
        val = b[16].get('values')
        tem17 = val.get('temperature')
        temp_entr17.set(tem17)

        data18 = b[17].get('time')
        data_time18.set(data18)
        val = b[17].get('values')
        tem18 = val.get('temperature')
        temp_entr18.set(tem18)

        data19 = b[18].get('time')
        data_time19.set(data19)
        val = b[18].get('values')
        tem19 = val.get('temperature')
        temp_entr19.set(tem19)

        data20 = b[19].get('time')
        data_time20.set(data20)
        val = b[19].get('values')
        tem20 = val.get('temperature')
        temp_entr20.set(tem20)

        data21 = b[20].get('time')
        data_time21.set(data21)
        val = b[20].get('values')
        tem21 = val.get('temperature')
        temp_entr21.set(tem21)

        data22 = b[21].get('time')
        data_time22.set(data22)
        val = b[21].get('values')
        tem22 = val.get('temperature')
        temp_entr22.set(tem22)

        data23 = b[22].get('time')
        data_time23.set(data23)
        val = b[22].get('values')
        tem23 = val.get('temperature')
        temp_entr23.set(tem23)

        data24 = b[23].get('time')
        data_time24.set(data24)
        val = b[23].get('values')
        tem24 = val.get('temperature')
        temp_entr24.set(tem24)


target = Tk()
target.title('Weather')
target.geometry('1600x1600')
# arget.config(background='black')
target.config(background='#FFF8DC')

nameaaaa = Label(target, text='Input city : ').place(x=500, y=100)
var1 = StringVar()
entry1 = Entry(target, textvariable=var1, width=44).place(x=590, y=100)
lan1 = StringVar()
chose = {'Tashkent', 'Samarkand'}
menu1 = OptionMenu(target, lan1, *chose).place(x=900, y=100)
# add = Button(target, text='FIND(MINUTLY) 🔍', width=15, command=get_var1).place(x=710, y=150)
add2 = Button(target, text='FIND(HOURLY) 🔍', width=15, command=hourly).place(x=580, y=150)

data_time = StringVar()
name1 = Label(target, text='Date : ').place(x=10, y=200)
data_enery1 = Entry(target, textvariable=data_time, width=18).place(x=50, y=200)
temp = Label(target, text='Average temperature').place(x=170, y=200)
temp_entr = StringVar()
tempentry = Entry(target, textvariable=temp_entr, width=6).place(x=300, y=200)

data_time2 = StringVar()
name2 = Label(target, text='Date : ').place(x=10, y=300)
data_enery2 = Entry(target, textvariable=data_time2, width=18).place(x=50, y=300)
temp2 = Label(target, text='Average temperature').place(x=170, y=300)
temp_entr2 = StringVar()
tempentry2 = Entry(target, textvariable=temp_entr2, width=6).place(x=300, y=300)

data_time3 = StringVar()
name3 = Label(target, text='Date : ').place(x=10, y=400)
data_enery3 = Entry(target, textvariable=data_time3, width=18).place(x=50, y=400)
temp3 = Label(target, text='Average temperature').place(x=170, y=400)
temp_entr3 = StringVar()
tempentry3 = Entry(target, textvariable=temp_entr3, width=6).place(x=300, y=400)

data_time4 = StringVar()
name4 = Label(target, text='Date : ').place(x=10, y=500)
data_enery4 = Entry(target, textvariable=data_time4, width=18).place(x=50, y=500)
temp4 = Label(target, text='Average temperature').place(x=170, y=500)
temp_entr4 = StringVar()
tempentry4 = Entry(target, textvariable=temp_entr4, width=6).place(x=300, y=500)

data_time5 = StringVar()
name5 = Label(target, text='Date : ').place(x=10, y=600)
data_enery5 = Entry(target, textvariable=data_time5, width=18).place(x=50, y=600)
temp5 = Label(target, text='Average temperature').place(x=170, y=600)
temp_entr5 = StringVar()
tempentry5 = Entry(target, textvariable=temp_entr5, width=6).place(x=300, y=600)

data_time6 = StringVar()
name6 = Label(target, text='Date : ').place(x=10, y=700)
data_enery6 = Entry(target, textvariable=data_time6, width=18).place(x=50, y=700)
temp6 = Label(target, text='Average temperature').place(x=170, y=700)
temp_entr6 = StringVar()
tempentry6 = Entry(target, textvariable=temp_entr6, width=6).place(x=300, y=700)

# data : 390  , entr  : 400 , aragave temp : 400 , entr : 400

data_time7 = StringVar()
name7 = Label(target, text='Date : ').place(x=400, y=200)
data_enery7 = Entry(target, textvariable=data_time7, width=18).place(x=450, y=200)
temp7 = Label(target, text='Average temperature').place(x=570, y=200)
temp_entr7 = StringVar()
tempentry7 = Entry(target, textvariable=temp_entr7, width=6).place(x=700, y=200)

data_time8 = StringVar()
name8 = Label(target, text='Date : ').place(x=400, y=300)
data_enery8 = Entry(target, textvariable=data_time8, width=18).place(x=450, y=300)
temp8 = Label(target, text='Average temperature').place(x=570, y=300)
temp_entr8 = StringVar()
tempentry8 = Entry(target, textvariable=temp_entr8, width=6).place(x=700, y=300)

data_time9 = StringVar()
name9 = Label(target, text='Date : ').place(x=400, y=400)
data_enery9 = Entry(target, textvariable=data_time9, width=18).place(x=450, y=400)
temp9 = Label(target, text='Average temperature').place(x=570, y=400)
temp_entr9 = StringVar()
tempentry9 = Entry(target, textvariable=temp_entr9, width=6).place(x=700, y=400)

data_time10 = StringVar()
name10 = Label(target, text='Date : ').place(x=400, y=500)
data_enery10 = Entry(target, textvariable=data_time10, width=18).place(x=450, y=500)
temp10 = Label(target, text='Average temperature').place(x=570, y=500)
temp_entr10 = StringVar()
tempentry10 = Entry(target, textvariable=temp_entr10, width=6).place(x=700, y=500)

data_time11 = StringVar()
name11 = Label(target, text='Date : ').place(x=400, y=600)
data_enery11 = Entry(target, textvariable=data_time11, width=18).place(x=450, y=600)
temp11 = Label(target, text='Average temperature').place(x=570, y=600)
temp_entr11 = StringVar()
tempentry11 = Entry(target, textvariable=temp_entr11, width=6).place(x=700, y=600)

data_time12 = StringVar()
name12 = Label(target, text='Date : ').place(x=400, y=700)
data_enery12 = Entry(target, textvariable=data_time12, width=18).place(x=450, y=700)
temp12 = Label(target, text='Average temperature').place(x=570, y=700)
temp_entr12 = StringVar()
tempentry12 = Entry(target, textvariable=temp_entr12, width=6).place(x=700, y=700)

data_time13 = StringVar()
name13 = Label(target, text='Date : ').place(x=790, y=200)
data_enery13 = Entry(target, textvariable=data_time13, width=18).place(x=830, y=200)
temp13 = Label(target, text='Average temperature').place(x=950, y=200)
temp_entr13 = StringVar()
tempentry13 = Entry(target, textvariable=temp_entr13, width=6).place(x=1080, y=200)

# data : 390  , entr  : 400 , aragave temp : 400 , entr : 400


data_time14 = StringVar()
name14 = Label(target, text='Date : ').place(x=790, y=300)
data_enery14 = Entry(target, textvariable=data_time14, width=18).place(x=830, y=300)
temp14 = Label(target, text='Average temperature').place(x=950, y=300)
temp_entr14 = StringVar()
tempentry14 = Entry(target, textvariable=temp_entr14, width=6).place(x=1080, y=300)

data_time15 = StringVar()
name15 = Label(target, text='Date : ').place(x=790, y=400)
data_enery15 = Entry(target, textvariable=data_time15, width=18).place(x=830, y=400)
temp15 = Label(target, text='Average temperature').place(x=950, y=400)
temp_entr15 = StringVar()
tempentry15 = Entry(target, textvariable=temp_entr15, width=6).place(x=1080, y=400)

data_time16 = StringVar()
name16 = Label(target, text='Date : ').place(x=790, y=500)
data_enery16 = Entry(target, textvariable=data_time13, width=18).place(x=830, y=500)
temp16 = Label(target, text='Average temperature').place(x=950, y=500)
temp_entr16 = StringVar()
tempentry16 = Entry(target, textvariable=temp_entr16, width=6).place(x=1080, y=500)

data_time17 = StringVar()
name17 = Label(target, text='Date : ').place(x=790, y=600)
data_enery17 = Entry(target, textvariable=data_time17, width=18).place(x=830, y=600)
temp17 = Label(target, text='Average temperature').place(x=950, y=600)
temp_entr17 = StringVar()
tempentry17 = Entry(target, textvariable=temp_entr17, width=6).place(x=1080, y=600)

data_time18 = StringVar()
name18 = Label(target, text='Date : ').place(x=790, y=700)
data_enery18 = Entry(target, textvariable=data_time18, width=18).place(x=830, y=700)
temp18 = Label(target, text='Average temperature').place(x=950, y=700)
temp_entr18 = StringVar()
tempentry18 = Entry(target, textvariable=temp_entr18, width=6).place(x=1080, y=700)
# data : 390  , entr  : 400 , aragave temp : 400 , entr : 400


data_time19 = StringVar()
name19 = Label(target, text='Date : ').place(x=1190, y=200)
data_enery19 = Entry(target, textvariable=data_time18, width=18).place(x=1230, y=200)
temp19 = Label(target, text='Average temperature').place(x=1330, y=200)
temp_entr19 = StringVar()
tempentry19 = Entry(target, textvariable=temp_entr19, width=6).place(x=1450, y=200)

data_time20 = StringVar()
name20 = Label(target, text='Date : ').place(x=1190, y=300)
data_enery20 = Entry(target, textvariable=data_time20, width=18).place(x=1230, y=300)
temp20 = Label(target, text='Average temperature').place(x=1330, y=300)
temp_entr20 = StringVar()
tempentry20 = Entry(target, textvariable=temp_entr20, width=6).place(x=1450, y=300)

data_time21 = StringVar()
name21 = Label(target, text='Date : ').place(x=1190, y=400)
data_enery21 = Entry(target, textvariable=data_time21, width=18).place(x=1230, y=400)
temp21 = Label(target, text='Average temperature').place(x=1330, y=400)
temp_entr21 = StringVar()
tempentry21 = Entry(target, textvariable=temp_entr21, width=6).place(x=1450, y=400)

data_time22 = StringVar()
name22 = Label(target, text='Date : ').place(x=1190, y=500)
data_enery22 = Entry(target, textvariable=data_time22, width=18).place(x=1230, y=500)
temp22 = Label(target, text='Average temperature').place(x=1330, y=500)
temp_entr22 = StringVar()
tempentry22 = Entry(target, textvariable=temp_entr22, width=6).place(x=1450, y=500)

data_time23 = StringVar()
name23 = Label(target, text='Date : ').place(x=1190, y=600)
data_enery23 = Entry(target, textvariable=data_time23, width=18).place(x=1230, y=600)
temp23 = Label(target, text='Average temperature').place(x=1330, y=600)
temp_entr23 = StringVar()
tempentry23 = Entry(target, textvariable=temp_entr23, width=6).place(x=1450, y=600)

data_time24 = StringVar()
name24 = Label(target, text='Date : ').place(x=1190, y=700)
data_enery24 = Entry(target, textvariable=data_time24, width=18).place(x=1230, y=700)
temp24 = Label(target, text='Average temperature').place(x=1330, y=700)
temp_entr24 = StringVar()
tempentry24 = Entry(target, textvariable=temp_entr24, width=6).place(x=1450, y=700)

if __name__ == '__main__':
    target.mainloop()
