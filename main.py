import pandas as pd
from matplotlib import pyplot as plt

class Visitors:

    topThree = []
    topCountry = []

    sno = 1
    showChartA = False
    showChartB = False
    top = ""
    topNo = 0

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

    yearEnd = yearStart + 9

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

    def makeCharts(self):

        file = "Project_File.xlsx"
        xls = pd.ExcelFile(file)

        dataFrame = xls.parse(0, usecols=colNo, names=colsNames)
        dataFrame = dataFrame.replace(["na"], [0])

        ######  Charting by Month/Year ######

        if(showChartA):
            for year in range(yearStart,  yearEnd + 1):
                if year >= yearStart and year <= yearEnd:
                    #targetRows = dataFrame[dataFrame["Year"] == " 1979 Apr "]
                    targetRows = dataFrame[dataFrame["Year"].str.contains(str(year))]

                    #print(targetRows)

                    #test = dataFrame["Year"]

                    #dataFrame[["YearP", " MonthP"]] = test.str.split(" ", n=1, expand=True)
                    #print(dataFrame)

                    #targetRows = dataFrame[dataFrame.YearP == year]
                    #print(targetRows)

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

        if(showChartB):
            dataFrame["Year"] = dataFrame["Year"].str[:5]
            for country in countryList:
                currCountry = dataFrame[["Year", country]]
                targetRows = currCountry[(currCountry["Year"].astype(int) >= yearStart) & (currCountry["Year"].astype(int) <= yearEnd)]

                plt.plot(targetRows["Year"], targetRows[country], label=country)

                plt.title("Visitors from " + country)
                plt.xlabel("Year")
                plt.ylabel("Visitor No.")
                plt.style.use("dark_background")

                plt.show()


    def showStatistics(self):
        ###### Overall Statistics ######
        file = "Project_File.xlsx"
        xls = pd.ExcelFile(file)

        overall = xls.parse(0, usecols=self.colNo,
                              names=self.colsNames)
        overall = overall.replace(["na"], [0])
        #overall["Year"] = "TEST"
        #print(overall)
        overall["Year"] = overall["Year"].str[:5]
        targetRows = overall[(overall["Year"].astype(int) >= self.yearStart) & (overall["Year"].astype(int) <= self.yearEnd)]

        finalTarget = targetRows[self.countryList]

        for country in self.countryList:
            self.update_top_three(country, finalTarget[country].sum())

        print("\nThe top 3 countries for " + str(self.yearStart) + " - " + str(self.yearEnd) + " from Asia was:\n")

        for index in range(len(self.topThree)):
            print(self.topCountry[index] + " (total: " + str(self.topThree[index]) + ", mean: " + str(finalTarget[self.topCountry[index]].mean()) + ") ")

        topPosition = self.topThree.index(max(self.topThree))
        self.top = self.topCountry[topPosition]
        self.topNo = self.topThree[topPosition]


    def update_top_three(self, country, total):
        if len(self.topThree) == 3:
            if total > min(self.topThree):
                index = self.topThree.index(min(self.topThree))
                self.topThree.remove(min(self.topThree))
                self.topThree.append(total)
                self.topCountry.remove(self.topCountry[index])
                self.topCountry.append(country)
        else:
            self.topThree.append(total)
            self.topCountry.append(country)


calculateVisitors = Visitors()
calculateVisitors.showStatistics()




    # dataFrame["Year"] = dataFrame["Year"].str[:5]
    # jpDataFrame = dataFrame[["Year", "Japan"]]
    # targetRows = jpDataFrame[(jpDataFrame["Year"].astype(int) > 1977) & (jpDataFrame["Year"].astype(int) < 1988)]
    # print(targetRows)
    #
    # plt.scatter(targetRows.Year, targetRows.Japan, marker="s", alpha=0.7)
    # plt.show()

