def excahnge(a, s):
    b = 11400
    sums = a / s
    sumssss = sums*b
    sumssss = str(sumssss)
    empy = ''
    c =0
    for i in sumssss:
        empy+=i
        c+=1
        if c==3:
            empy+=' '
    return f'{empy} ming  som kwi bowiga '




def exchange2(narx ,odam):
    dollr =11400
    gandon_makler = narx*50/100
    sum1 =narx+gandon_makler
    sum2 = sum1/odam
    sumsss=sum2*dollr
    sumsss =str(sumsss)
    c=0
    empy = ''
    for i in sumsss:
        empy+=i
        c+=1
        if c==1:
            empy+=' '
        if c==4:
            empy+=' '
    return f'{empy} ming som '

a = int(input('kvartira narxni krintg(dollrda) :'))
s = int(input('odam sonini kriting : '))
d = input('makler xzmati bomi yoqmi ? y/n : ' )
if d == 'n':
    print(excahnge(a,s))
else:
    print(exchange2(a,s))
