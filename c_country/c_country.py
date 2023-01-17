def get_c_country():
    with open('wold.csv') as f:
        lines = f.readlines()
        lst = []
        for line in lines:
            a = line.split(',')[0]
            if a[0]=='C':
                lst.append(a)
    return lst

print(get_c_country())