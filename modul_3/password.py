from random import *
import os

u_pswd = input('enter password :')
pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', '1', '2', '3', '4', '5', '6']
pw = ''

while (pw != u_pswd):
    pw =''
    for latter in range(len(u_pswd)):
        gues_pwd = pwd[randint(0,17)]
        pw =str(gues_pwd)+str(pw)
        print(pw)
        print('creak passwod...........plase wait.......')
        os.system('cls')
print(f'your password is {pw}')
