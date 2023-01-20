import csv


def get_c():
    try:
        with open('changefile.txt ', encoding="utf-8") as f:
            lines = csv.DictReader(f)
            lst = []
            for line in lines:
                country = line.get('country')

                if country == 'Uzbekistan':
                    a = line.get('city')
                    lst.append(a)

            return lst
    except Exception as e:
        print(e)


print(get_c())
