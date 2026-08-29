import openpyxl

wb = openpyxl.load_workbook("students_copy.xlsx")
sheet = wb["Students"]
print(sheet["B19"].value)
wb.close()

     

