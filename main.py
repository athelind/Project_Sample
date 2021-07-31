import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#TRY TO INSTALL THIS
import openpyxl

file = "Project_File.xlsx"
xls = pd.ExcelFile(file)

# Parse the first column of the second sheet and rename the column: df2
#df2 = xls.parse(1, usecols=[0], skiprows=[0], names=["Country"])

dataFrame = xls.parse(0, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                      names=["Year","Brunei Darussalam","Indonesia","Malaysia","Philippines","Thailand","Viet Nam","Myanmar","Japan","Hong Kong","China","Taiwan","Korea, Republic Of","India","Pakistan","Sri Lanka"])
#print(dataFrame.head())
#print(dataFrame.info())
#print(dataFrame["Year"])

dataFrame = dataFrame.replace([" na "], [0])
countryList = ["Brunei Darussalam","Indonesia","Malaysia","Philippines","Thailand","Viet Nam","Myanmar","Japan","Hong Kong","China","Taiwan","Korea, Republic Of","India","Pakistan","Sri Lanka"]

for year in range(2017):
    plt.title("Visitors in " + str(year))
    plt.xlabel("Year")
    plt.ylabel("Country")

    if year > 1977 and year < 1988:
    #if year == 1978:
        targetRows = dataFrame[dataFrame["Year"].str.contains(str(year))]

        print(targetRows)
        for country in countryList:
            plt.plot(targetRows["Year"], targetRows[country], label=country)

        plt.legend()
        plt.show()








