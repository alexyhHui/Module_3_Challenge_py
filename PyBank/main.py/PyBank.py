import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('..','Resources','budget_data.csv')

# Initialize variables to store data
total_months = 0
net_total = 0
previous_profit = 0
Profit_changes = []
dates = []

# Read in the CSV file
with open(csvpath,'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        
        # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total amount of profit/losses
        net_total += profit
        
        # Calculate the change in profit/losses from the previous month
        if total_months > 1:
            change = profit - previous_profit
            Profit_changes.append(change)
            dates.append(date)
        
        previous_profit = profit

    # Calculate the average change
    average_change = sum(Profit_changes) / len(Profit_changes)

    # Find the greatest increase and decrease in profits
    max_increase = max(Profit_changes)
    max_decrease = min(Profit_changes)

    # Find the corresponding dates for the greatest increase and decrease
    increase_date = dates[Profit_changes.index(max_increase)]
    decrease_date = dates[Profit_changes.index(max_decrease)]

# Print the financial analysis results
print("Financial Analysis")
print("-" * 28)
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${max_decrease})")

# Save the results to a text file
with open("financial_analysis.txt", 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-" * 28 + "\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_date} (${max_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${max_decrease})\n")
