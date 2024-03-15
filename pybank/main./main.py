# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:55:59 2024

@author: pauld
"""

import csv



# Read resources from the csv file that was provided (budget_data.csv)

csv_path = "pybank/resources/budget_data.csv"

#initialize variables

total_months = 0
total_profit_or_loss = 0
prev_profit_loss = 0
changes = []
month = []

#main loop which iterates through each row in the csv file
#updates total_months and total_profit_or_loss variables
#stores the values calculated in changes and month variables

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        total_profit_or_loss += int(row[1])
        if month:
            changes.append(int(row[1]) - prev_profit_loss)
        month.append(row[0])
        prev_profit_loss = int(row[1])

average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

# Find the dates for greatest increase and decrease in profit or loss
increase_date = month[changes.index(greatest_increase) + 1]
decrease_date = month[changes.index(greatest_decrease) + 1]

# Print and export results
#set output equal to the file location
output = f"""

Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_or_loss}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_date} (${greatest_increase})
Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})
"""

print(output)

#exports to the txt file
with open("budget_data.txt", "w") as output_file:
    output_file.write(output)
