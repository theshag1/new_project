import csv
def get_c_country():
    with open('wold.csv') as f:
        lines = f.readlines()
        lst = []
        for line in lines:
            a = line.split(',')[0]
            if a[0] == 'C':
                lst.append(a)
    return lst

    # print(get_c_country())
    # def get_gdp():


def get_gdp():
    with open('wold.csv') as f:
        lines = csv.DictReader(f)
        print(lines)
        lst = []
        for line in lines:
            try:
                int(line.get("GDP ($ per capita)"))
            except ValueError as e:
                print(e)
            else:
                if int(line.get("GDP ($ per capita)")) > 1000:
                    lst.append(f"{line.get('Country')}, {line.get('GDP ($ per capita)')}")

    return lst
print(get_gdp())



