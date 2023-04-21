# import dependencies
import csv
import os

#Csv Location
budget_info = "./Resources/budget_data.csv"
budget_analysis = "./analysis/financial_analysis.txt"
# Open csv file
with open(budget_info) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Skip Header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Finding total months
    total_months = 0
    total_profit = 0
    profit_list = []
    profit_change = []
    previous_profit_loss = 0
    current_profit_loss = 0
    max_change = 0
    avg_change = 0
    # Read each row of data after the header
    for row in csvreader:
        

        #The total number of months included in the dataset
        total_months = total_months + 1
        current_profit_loss = int(row[1])
        profit_list.append(current_profit_loss)
        total_profit = total_profit + current_profit_loss
            #Another way to do it
        if (current_profit_loss - previous_profit_loss) > max_change:
            max_change = current_profit_loss - previous_profit_loss
        profit_change.append(current_profit_loss - previous_profit_loss)
        previous_profit_loss = current_profit_loss
    max_profit_change = max(profit_change)
    min_profit_change = min(profit_change)
    avg_change = sum(profit_change) / len(profit_change)
    #avg_profit = sum(profit_list) / len(profit_list)

#Print Result
# print(total_months)
financial_analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total_profit}\n"
    f"Average Change: {avg_profit}\n"
    f"Greatest Increase in Profits: {max_profit_change}\n"
    #f"Test algorithim: {max_change}\n"
    f"Greatest Decrease in Profits: {min_profit_change}\n"
)

print(financial_analysis)

# Saved in analysis
with open(budget_analysis, "w") as f_analysis:
    f_analysis.write(financial_analysis)

