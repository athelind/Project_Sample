import pandas as pd

#TRY TO INSTALL THIS
import openpyxl

file = "Project_File.xlsx"
xls = pd.ExcelFile(file)
print(xls.sheet_names)


