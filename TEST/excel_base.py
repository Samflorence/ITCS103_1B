import openpyxl as xl

book = xl.Workbook()
sheet = book.active

sheet["A1"] = "ID"
sheet["B1"] = "Last Name"
sheet["C1"] = "First Name"
sheet["D1"] = "Middle Name"
sheet["E1"] = "Birthyear"
sheet["F1"] = "Age"

sheet["A2"] = "1"
sheet["B2"] = "Sio"
sheet["C2"] = "Sam"
sheet["D2"] = " "
sheet["E2"] = "2006"
sheet["F2"] = "20"

book.save("excelDb.xlsx")