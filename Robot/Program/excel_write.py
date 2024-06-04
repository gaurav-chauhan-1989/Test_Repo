import openpyxl

wb = openpyxl.Workbook()
sh = wb.active
sh['A1'].value = "Gaurav"
sh['B1'].value = "Chauhan"
sh['A2'].value = "Gaurav"
sh['B2'].value = "Chauhan"
wb.save("E:\\Sheet\\sh1.xlsx")

