import csv


def get_city():
    try:
        with open('file.txt', encoding='utf-8') as f:
            lst = []
            lines = csv.DictReader(f)
            for line in lines:
                region = line.get('country')
                if region == 'Uzbekistan':
                    lst.append(line)

    except Exception as e:
        return e
    return lst


try:
    lst = []
    for line in get_city():
        lat = line.get('lat')
        lng = line.get('lng')
        city = line.get('city')
        lst.append(f"https://my{city}.orq/?lat={lat}&lng={lng}")
    print(lst)
# https://my-location.org/?lat=41.284067&lng=69.147750
except Exception as e:
    print(e)
