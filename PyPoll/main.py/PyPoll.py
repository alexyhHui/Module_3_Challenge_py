import os
import csv

# Define the path to the CSV file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Initialize variables to store data
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read and analyze the CSV file
with open(csvpath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

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
