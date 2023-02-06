import csv

#
# class Department:
#     def __init__(self, file_path):
#         self.file_path = file_path

# def get_info(self):
try:
    with open('empoly_information.csv', encoding='utf-8') as f:
         lines = csv.DictReader(f)

        for line in f:
            print(line.split('t')[0])
            # a = line.split('t')
            for linee in lines:
                print(linee)
            # print(a)
except Exception as e:
    print(e)
