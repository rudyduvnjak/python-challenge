# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..','Resources','budget_data.csv' )



# Reading using CSV module

with open(r"C:\Git\ClassWork_HomeWork\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
# our task is to create a Python script that analyzes the records to calculate each of the following:

#* The total number of months included in the dataset
#* The net total amount of "Profit/Losses" over the entire period
#* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#* The greatest increase in profits (date and amount) over the entire period
#* The greatest decrease in profits (date and amount) over the entire period*
# As an example, your analysis should look similar to the one below:


# Financial Analysis
  #----------------------------
  ##Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)

#Declare Variables##
total_months = 0
total_profit = 0
average_profit_change = 0
maximum_profit = 0
minimum_profit = 0
maximum_month = 0
minimum_month = 0




#Declare Lists for two columns
profit_losses = []
month = []
profit_change = []

#Read each row of data after the header
#Opening data path again for the calculations
with open(r"C:\Git\ClassWork_HomeWork\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
#Import rows into lists
    for row in csvreader:
        profit_losses.append(int(row[1]))
        month.append(row[0])
#Calculate total P&L and count number of months
        total_profit = sum(profit_losses)
        total_months = len(month)
#Go through profit_losses list and calculate profit changes month to month
    for i in range(1, len(profit_losses)):
        profit_change.append(profit_losses[i] - profit_losses[i-1])
#Calculate average profit change
        average_profit_change = round(sum(profit_change) / len(profit_change))
#Find Maximum profit and month it occured
        profit_maximum = str(max(profit_change))
        max_profit_date = str(month[profit_change.index(max(profit_change))])
#Find Minimum profit and date it occured
        profit_minimum = str(min(profit_change))
        min_profit_date = str(month[profit_change.index(min(profit_change))])
#Print data to verify code functionality
    print("Total Profit: " + str(total_profit))
    print("Number of months: " + str(total_months))
    print("Average Profit Change:" + str(average_profit_change))
    print("Greatest Profits Increase Occured on:" + str(max_profit_date) + "," +   "($" + (profit_maximum) + ")")
    print("Greatest profit decrease Occured on:" + str(min_profit_date + "," + "($" + profit_minimum +")" ))
#Create path for output text file and write new found data
with open(r"C:\Git\ClassWork_HomeWork\python-challenge\PyBank\Analysis\outputPyBank.txt", "w") as file:
    file.write(f"\n_________________________________")
    file.write(f"\nBank Financial Analysis")
    file.write(f"\nTotal_Profit: ${sum(profit_losses)}")
    file.write(f"\nTotal_Months: ${(total_months)}")
    file.write(f"\nAverage_Profit_Change: ${average_profit_change}")
    file.write(f"\nGreatest_Profit_Increase: " + str(max_profit_date) + ", " + "$" + str(profit_maximum))
    file.write(f"\nGreatest_Profit_Decrease: " + str(min_profit_date) + ", " + "$" + str(profit_minimum))