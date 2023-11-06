import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('D:\\UoB Data Bootcamp\\Assignment\\Module 3 Challenge\\Starter_Code\\PyPoll\\Resources\\election_data.csv')

# Initialize variables to store data
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read in the CSV file
with open(csvpath,'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Calculate and print the results
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += f"""
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

# Export the results to a text file
with open("election_results.txt", "w") as result_file:
    result_file.write(output)