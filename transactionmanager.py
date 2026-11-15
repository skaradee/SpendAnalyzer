import csv
import sys
import copy
#import statistics

import numpy

# citi.csv                            download-busey.csv
# Discover-AllAvailable-20190203.csv  new-amex.csv
# Discover-Search-20201228.csv        Transactions.csv

class Expense:

    def __init__(self):
        self.date = []
        self.expense = 0
        self.reason = ""
        self.category = ""
        self.weight = 0

    def __init__(self, row, option):

        if option == 1 :
            # Code for AmeX expense item
            self.date = convertToDateAmeX(row[0])
            self.expense = float(row[7])
            self.reason = row[11]
            self.category = "unclassified"
            self.account = 1
            self.weight = self.date[2]*10000 + self.date[0]*100 + self.date[1] # easy to access and sort entries.
            # print(str(date) + " - " + str(amount) + " - " + reason)
            # print(expense(date,amount,reason))
            # transaction += [Expense(date,amount,reason)]

        if option == 4 :
            # Code for new AmeX expense item
            self.date = convertToDateAmeX(row[0])
            self.expense = float(row[2])
            self.reason = row[10]
            self.category = "unclassified"
            self.account = 1
            self.weight = self.date[2]*10000 + self.date[0]*100 + self.date[1] # easy to access and sort entries.
            # print(str(date) + " - " + str(amount) + " - " + reason)
            # print(expense(date,amount,reason))
            # transaction += [Expense(date,amount,reason)]

            
        if option == 2 :
            # Code for Discover expensve item
            self.date = convertToDateDiscover(row[0])
            self.expense = float(row[3])
            self.reason = row[4]
            self.category = "unclassified"
            self.account = 2
            self.weight = self.date[2]*10000 + self.date[0]*100 + self.date[1] # easy to access and sort entries.            
            # print(str(date) + " - " + str(amount) + " - " + reason)
            # transaction += [Expense(date,amount,reason)]
            
        if option == 3 :
            # Code for citi expense item
            self.date = convertToDateCiti(row[1])
            if row[3] != '':
                # transaction += [Expense(convertToDateCiti(row[1]), float(row[3]), row[2])]
                # print(Expense(convertToDateCiti(row[1]), float(row[3]), row[2]))
                self.expense = float(row[3])
            elif row[4] != '' :
                self.expense = float(row[4])
                # transaction += [Expense(convertToDateCiti(row[1]), float(row[4]), row[2])]
            else:
                self.expense = 0

            self.reason = row[2]
            # print(str(date) + " - " + str(amount) + " - " + reason)
            # transaction += [Expense(date,amount,reason)]
            self.category = "unclassified"
            self.account = 3
            self.weight = self.date[2]*10000 + self.date[0]*100 + self.date[1] # easy to access and sort entries.            

    # def __init__(self, date, expense, reason):
    #     self.date = date.copy()
    #     self.expense = expense
    #     self.reason = reason
    #     self.category = ""
    #     self.weight = date[2]*10000 + date[0]*100 + date[1] # easy way to access and sort all entries.

        
    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return str(self.date) + " - " + str(self.expense) + " - " + self.reason

    def inMonthYear(self, month, year):
        if self.date[0] == month and self.date[2] == year :
            return True
        else:
            return False

def convertToDateCiti(date):
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    array = [month,day,year]
    return array

def convertToDateDiscover(date):
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    array = [month,day,year]
    return array
    
def convertToDateAmeX(date):
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    array = [month,day,year]
    return array
    # print("month - "+str(month)+"- / - day - "+str(day)+" - / - year - "+str(year))
    # print(date)



files = [["./transactions/amex1.csv", 1, 0], ["./transactions/amex2.csv", 4, 1], ["./transactions/disc1.csv", 2, 1], ["./transactions/disc2.csv", 2, 1], ["./transactions/citi1.csv", 3, 1]]
    
transaction = []

transactions = []

newNumTrans = 0

skipone = 0
for element in files:
    filereader = open(element[0], 'rt')
    reader = csv.reader(filereader)
    entryType = element[1]

    if element[2] == 1 :
        skipone = 1

    for row in reader:
        newNumTrans+=1
        # print(newNumTrans)
        if skipone == 1 :
            skipone = 0
            print("is it skipping?")
            continue
        transactions += [Expense(row,entryType)]

transactions.sort(key = lambda x : x.weight)

# for entries in transactions:
#     print(entries)
# print(transactions)

print(newNumTrans)

years = range(2017, 2021)
months = range(1, 13)
expenses = []

for year in years :
    monthly = []
    for month in months :
        sum = 0
        for entries in transactions :
            if entries.inMonthYear(month, year) :
                if entries.expense >= 0 :
                    sum += entries.expense
        monthly += [sum]
        print(str(year) + " - " + str(month) + " - " + str(sum))
    expenses += [monthly]

# for i in expenses :
#     print(i)
# print(expenses)
