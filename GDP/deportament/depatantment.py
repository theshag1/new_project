import csv


try:
    with open('department.csv') as f:
        lines = csv.DictReader(f)
        for line in lines:
            print(line.get('Department_ID'))
except Exception as e:
    print(e)