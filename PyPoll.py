#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
with open (file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)
#close the file
#import csv and os modules
import csv
import os
#add filename that references the path
file_to_load = os.path.join("Resources", "election_results.csv")

#open the election results and read the file
with open (file_to_load) as election_data:

#print the filename object
    print(election_data)

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt.")

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open (file_to_save, "w") as outfile:
# Write some data to the file.
    outfile.write("Hello World")

# Close the file
outfile.close()

file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
        # Make a header
        # Write three counties to the file.
        txt_file.write("Counties in the Election\n-------------------------\nAraphoe\nDenver\nJefferson")

# Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Initialize a total vote counter
total_votes = 0

# Declare a new candidate list
candidate_options = []
# 1. Declare the empy dictionary
candidate_votes = {}

# open the election results and read the file
with open(file_to_load) as election_data:
        # To do: read and analyze the data here 
        # Read the file object with the reader function
        file_reader = csv.reader(election_data)

        # Print the header row
        headers = next(file_reader)
        print(headers)
        # Print each row in the CSV file.
        for row in file_reader:
                #Add to the total vote count
                total_votes += 1

                # Print the candidate name from each row
                candidate_name = row[2]

                # If the candidate does not match any existing candidate...
                if candidate_name not in candidate_options:
                    # Add the candidate name from each row
                    candidate_options.append(candidate_name)

                    #2. Begin tracking that candidates vote count.
                    candidate_votes[candidate_name] = 0

                #Add a vote to that candidates count.
                candidate_votes[candidate_name] += 1
        # Determine the percentage of votes for each candidate by looping through the count.
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote county of a candidate.
            votes = candidate_votes[candidate_name]
            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # To do: print out each candidates name, vote count, and percentage of votes to the terminal

            # Print the candidate name and percentage of votes.
            print(f"{candidate_name}: {vote_percentage:.1f} ({votes:,})\n")
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent = # vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        winning_candidate_summary = (
                f"--------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage: .1f}%\n"
                f"---------------------\n"
        )
        print(winning_candidate_summary)
        # To do: print out the winning candidate, vote count and percentage to the terminal
        #Print the candidate vote dictionary
        print(candidate_votes)