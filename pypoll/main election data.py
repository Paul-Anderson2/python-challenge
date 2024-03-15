# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:03:57 2024

@author: pauld
"""

import csv

# Read resources from the csv file that was provided

csv_path = "C:/Users/pauld/OneDrive/Desktop/VU Analytics Boot Camp/Mod 3 HW/election_data.csv"

#Define new variables and initialize them
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

#main loop that iterates through rows of the csv file
#calcs total_votes , each candidates' votes and determines the winner

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        # Check for the winner
        if candidates[candidate] > winner_votes:
            winner = candidate
            winner_votes = candidates[candidate]

# Calculate the percentage of votes for each candidate
percentage_format = "{:.3%}"
candidate_results = []
for candidate, votes in candidates.items():
    percentage = votes / total_votes
    formatted_percentage = percentage_format.format(percentage)
    candidate_results.append(f"{candidate}: {formatted_percentage} ({votes})")

# Print and export results
output = f"""
Election Results
--------------------------------
Total Votes: {total_votes}
--------------------------------
{chr(10).join(candidate_results)}
---------------------------------
Winner: {winner}
---------------------------------
"""

#exporting the txt file
print(output)

with open("election_results.txt", "w") as output_file:
    output_file.write(output)