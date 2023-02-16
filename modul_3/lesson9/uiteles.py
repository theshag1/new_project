from for_pdp import *

def save_registration(header , row):
    with open('Student_info.csv' , 'a' ,newline='\n',encoding="utf8") as f:
        csv_writer = csv.DictWriter(f , header)
        if os.path.getsize('Student_info.csv')==0:
            csv_writer.writeheader()
        csv_writer.writerow(row)
    print('Row add succesifully !')
#
# def write_row_to_csv(file_path, header, row):
#     with open(file_path, "a", newline="\n", encoding="utf8") as f:
#         csv_writer = csv.DictWriter(f, header)
#         if os.path.getsize(file_path) == 0:
#             csv_writer.writeheader()
#         csv_writer.writerow(row)
#     print("Row add successfully.")



def chek_id(chek):
    with open('Student_info.csv','r') as f:
        a = csv.DictReader(f)
        print(a.get(''))