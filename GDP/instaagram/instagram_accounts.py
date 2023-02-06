# import csv
#
#
# class Instagram:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def get_country(self):
#         lst = []
#         try:
#             with open(self.file_path) as f:
#                 lines = csv.DictReader(f)
#                 for line in lines:
#                     country = line.get('Country/Continent')
#                     if country not in lst:
#                         lst.append(country)
#         except Exception as e:
#             return e
#         return lst
#
#     def get_instagram(self):
#         for line in self.get_country()
#
#
#
#
# instagram = Instagram('List of most-followed Instagram accounts.csv')
# print(instagram.get_country())
#
