import openpyxl
import openpyxl.reader.excel


def get_row_count(file, sheet_name):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return sheet.max_row


def get_column_count(file, sheet_name):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    return sheet.max_column


def read_data():
    final_list = []
    workbook = openpyxl.load_workbook(".\\Test_Data\\Test_Data_for_DDT.xlsx")
    sheet = workbook["Login_Data"]
    total_rows = sheet.max_row
    total_columns = sheet.max_column
    for row in range(2, total_rows+1):
        row_list = []
        for col in range(2, total_columns+1):
            row_list.append(sheet.cell(row=row, column=col).value)
        final_list.append(row_list)
    return final_list


def write_data(file, sheet_name, row_num, column_num, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet_name]
    sheet.cell(row=row_num, column=column_num).value=data
    workbook.save(file)
