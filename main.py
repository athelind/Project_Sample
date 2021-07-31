import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#TRY TO INSTALL THIS
import openpyxl

sno = 1

region = "Asia"
#region = "Europe"
#region = "Others"

if sno == 1:
    yearStart = 1978
elif sno == 2:
    yearStart = 1988
elif sno == 3:
    yearStart = 1998
elif sno == 4:
    yearStart = 2008

if region == "Asia":
    colNo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    colsNames = ["Year", "Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar",
                 "Japan", "Hong Kong", "China", "Taiwan", "Korea, Republic Of"]
    countryList = ["Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar",
                   "Japan", "Hong Kong", "China", "Taiwan", "Korea, Republic Of"]
elif region == "Europe":
    colNo = [0, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    colsNames = ["Year","United Kingdom","Germany","France","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe"]
    countryList = ["United Kingdom", "Germany", "France", "Italy", "Netherlands", "Greece",
                   "Belgium & Luxembourg", "Switzerland", "Austria", "Scandinavia", "CIS & Eastern Europe"]
elif region == "Others":
    colNo = [0, 13, 14, 15, 16, 17, 18, 30, 31, 32, 33, 34]
    colsNames = ["Year", "India", "Pakistan", "Sri Lanka", "Saudi Arabia", "Kuwait", "UAE", "USA", "Canada",
                 "Australia", "New Zealand", "Africa"]
    countryList = ["India", "Pakistan", "Sri Lanka", "Saudi Arabia", "Kuwait", "UAE", "USA", "Canada",
                   "Australia", "New Zealand", "Africa"]

yearEnd = yearStart + 9
file = "Project_File.xlsx"
xls = pd.ExcelFile(file)

dataFrame = xls.parse(0, usecols=colNo, names=colsNames)
dataFrame = dataFrame.replace([" na "], [0])

######  Charting by Month/Year ######

for year in range(yearStart,  yearEnd + 1):
    if year >= yearStart and year <= yearEnd:
        targetRows = dataFrame[dataFrame["Year"].str.contains(str(year))]

        for country in countryList:
            if country == "Japan":
                plt.plot(targetRows["Year"], targetRows[country], label=country, marker="x")
            else:
                plt.plot(targetRows["Year"], targetRows[country], label=country)

        plt.title("Visitors in " + str(year))
        plt.xlabel("Year")
        plt.ylabel("Visitor No")
        plt.style.use("dark_background")
        plt.legend()
        plt.show()

###### Charting by Country ######

# dataFrame["Year"] = dataFrame["Year"].str[:5]
# for country in countryList:
#     currCountry = dataFrame[["Year", country]]
#     targetRows = currCountry[(currCountry["Year"].astype(int) >= yearStart) & (currCountry["Year"].astype(int) <= yearEnd)]
#
#     plt.plot(targetRows["Year"], targetRows[country], label=country)
#
#     plt.title("Visitors from " + country)
#     plt.xlabel("Year")
#     plt.ylabel("Visitor No.")
#     plt.style.use("dark_background")
#
#     plt.show()

###### Overall Statistics ######

overall = xls.parse(0, usecols=colNo,
                      names=colsNames)
overall = overall.replace([" na "], [0])
overall["Year"] = overall["Year"].str[:5]
targetRows = overall[(overall["Year"].astype(int) >= yearStart) & (overall["Year"].astype(int) <= yearEnd)]

finalTarget = targetRows[countryList]

topThree = []
topCountry = []

def update_top_three(country, total):
    if len(topThree) == 3:
        if total > min(topThree):
            index = topThree.index(min(topThree))
            topThree.remove(min(topThree))
            topThree.append(total)
            topCountry.remove(topCountry[index])
            topCountry.append(country)
    else:
        topThree.append(total)
        topCountry.append(country)

for country in countryList:
    update_top_three(country, finalTarget[country].sum())

print("\nThe top 3 countries for " + str(yearStart) + " - " + str(yearEnd) + " from Asia was:\n")

for index in range(len(topThree)):
    print(topCountry[index] + " (" + str(topThree[index]) + ") ")



# dataFrame["Year"] = dataFrame["Year"].str[:5]
# jpDataFrame = dataFrame[["Year", "Japan"]]
# targetRows = jpDataFrame[(jpDataFrame["Year"].astype(int) > 1977) & (jpDataFrame["Year"].astype(int) < 1988)]
# print(targetRows)
#
# plt.scatter(targetRows.Year, targetRows.Japan, marker="s", alpha=0.7)
# plt.show()

