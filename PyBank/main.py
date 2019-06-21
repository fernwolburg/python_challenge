import os
import csv

# open csv file path
budgetcsv = '/Users/fernandawolburg/Downloads/Budget_data.csv'

# open csv file
with open(budgetcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
# Declare all the variables that will be used in this code
    monthscount = 0
    net_proloss = 0
    avg_proloss = 0
    max_increase = 0
    max_decrease = 0
    last_month = 0
    change_month = 0
    tmonth_change = 0
    

# initialize loop to go through all of the rows and perform operations
    for row in csvreader:
        
        # calculate total number of months included in the dataset
        monthscount = monthscount + 1
        
        # calculate the net total amount of "Profit/Losses" over the entire period
        net_proloss = net_proloss + int(row[1])
        
        # calculate the average of the changes in "Profit/Losses" over the entire period
        avg_proloss = net_proloss/monthscount
        
        #turn row[1] into int, then subtract last month
        change_month = int(row[1]) - last_month
        #set last month to row[1]
        tmonth_change = tmonth_change + change_month
        #set last month to row[1]
        last_month = int(row[1])
        
        # calculate the greatest increase in profits (date and amount) over the entire period
        if max_increase < change_month:
            max_increase = change_month
            date1 = row[0]
    
        # calculate the greatest decrease in losses (date and amount) over the entire period
        if max_decrease > change_month:
            max_decrease = change_month
            date2 = row[0]

print("Financial Analysis")
print("------------------------------------------")       
print(f"Total Months are:    {monthscount} months")
print(f"Total profit/losses: ${net_proloss}")
print(f"Average:             ${avg_proloss}")
print(f"Greates increase:    ${max_increase} on {date1}")
print(f"Greatest decrease:   ${max_decrease} on {date2}")
pathlib.Path("main_PyBank.txt").write_text("Financial Analysis\n------------------------------------------\nTotal Months are:    86 months\nTotal profit/losses: $38382578\nGreates increase:    $1926159 on Feb-2012\nGreatest decrease:   $-2196167 on Sep-2013")
