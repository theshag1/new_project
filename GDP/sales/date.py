import csv

try:
    with open('date.txt') as f:
        lines = csv.DictReader(f)
        for line in lines:
            date = line.get('Order Date')
            product = line.get('Product')
            if date >= '04/10/19 ':
                file = open('sale.txt', 'a')
                file.write(f"{product}:{date}\n")
                file.close()
except Exception as e:
    print(e)
