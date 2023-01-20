import csv


def get_mac_():
    try:
        with open('salemac.csv') as f:
            lst = []
            lines = csv.DictReader(f)
            for line in lines:
                number = line.get('Product')
                if number == 'Macbook Pro Laptop':
                    lst.append(line)


    except Exception as e:
        return e
    return lst


try:
    all_number = 0
    for line in get_mac_():
        count = int(line.get('Quantity Ordered'))
        all_number += count
    print(f"all saled MACBOOK PRO : {all_number}")

except Exception as e:
    print(e)
