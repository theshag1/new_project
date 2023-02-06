import csv

# def get_base():
try:
    with  open('most_popular.csv', encoding='utf-8') as f:
        lines = csv.DictReader(f)
        lst = []
        all_lst = []
        flag = True
        c = 0

        for line in lines:
            date = line.get('Date')
            python = float(line.get('Python'))
            target_year = int(date[-4:])
            if target_year == 2004:
                c +=python
                lst.append(f'{target_year} : {c}')
    print(lst)

except Exception as e:
    print(e)
