import csv

with open('high.txt') as f:
    try:

        lines = csv.DictReader(f)
        for line in lines:
            product = line.get('Product')
            preach = float(line.get('Price Each'))
            if preach >= 300:
                file = open('writepreach.txt', 'a')
                file.write(f"{product} : {preach}\n")

    except Exception as e:
        print(e)


