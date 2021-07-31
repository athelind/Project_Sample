import pandas as pd
import os
#conda install -c anaconda openpyxl

wd = os.getcwd()
print(os.listdir(wd))

file = "Project_File.xlsx"
xls = pd.ExcelFile(file)
print(xls.sheet_names)


