import csv


def get_info():
    lst = []
    try:
        with open('netflix_titles.csv', encoding='utf-8') as f:
            lines = csv.DictReader(f)
            for line in lines:
                year = line.get('release_year')
                if year >= '2020':
                    lst.append(line)


    except Exception as e:
        return e
    return lst


fileee = get_info()
header = get_info()[0]
try:
    with open('new.csv', "w", encoding="utf8") as f:
        file = csv.DictWriter(f, header)
        file.writeheader()
        file.writerows(fileee)

except FileNotFoundError as e:
    print(e)
