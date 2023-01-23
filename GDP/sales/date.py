import csv

try:
    with open('date.csv') as f:
        lines = csv.DictReader(f)

        for line in lines:
            print(line)
            date = line.get('Order Date')
            product = line.get('Product')
            if date >= '04/10/19 ':
                file = open('sale.csv', 'w')
                file.write(f"{product}:{date}\n")
                file.close()
except Exception as e:
    print(e)
