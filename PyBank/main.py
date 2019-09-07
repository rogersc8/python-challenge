#import CSV and OS
import csv
import os

#declare path and create empty lists for appends
csvpath = os.path.join('budget_data.csv')
total_months = []
total_profit = []
monthly_change = []

#open csv/skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
#iterate through the rows
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
#append the monthly profit change  
    for p in range(len(total_profit)):
        monthly_change.append(total_profit[p] - total_profit[p-1])
#print(monthly_change)

#obtain the max/min of monthly profit change/correlate to right month 
max_value = max(monthly_change)
min_value = min(monthly_change)
max_change = monthly_change.index(max(monthly_change)) + 1
min_change = monthly_change.index(min(monthly_change)) + 1

#time to print this stuff out and see if it works
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_change]} (${(str(max_value))})")
print(f"Greatest Decrease in Profits: {total_months[min_change]} (${(str(min_value))})")

#output it into .csv file
output_path = os.path.join("fin_results.csv")
with open(output_path,"w") as file:
#write the file print statements
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_change]} (${(str(max_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_change]} (${(str(min_value))})")


