from openpyxl import Workbook
import datetime


def write_data_in_excel(sheet_name ,data_list = []):
    wb = Workbook()
    
    test_ws = wb.create_sheet(sheet_name)
    
    for data in data_list:
        index = "A"+str(data_list.index(data)+1)
        print(index)
        test_ws[index] = data

    current_date = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    wb.save(f"{current_date}_danawa.xlsx")

if __name__ == "__main__":
    test_data_list =['가','나','다']
    test_sheer_name = "test1458"
    write_data_in_excel(test_sheer_name,test_data_list)
