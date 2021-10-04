# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..','Resources','election_data.csv' )

#Declare Lists and Dictionaries
total_rows = 0
vote_count ={}
total_votes = 0
voters = []
candidates = []


with open(r"C:\Git\ClassWork_HomeWork\python-challenge\PyPoll\Resources\election_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
        
    # Read first and third row of data after the header for analysis
    for row in csvreader:
        voters.append(row[0])
        total_votes = len(voters)
        candidates = row[2]
    #Calcualte number of votes for each candidate within the loop   
        total_rows += 1
        if candidates in vote_count:
            vote_count[candidates] += 1
        else:
            vote_count[candidates] = 1 
            
            
    #Look up inside vote_count dictionary and calculate percentage won for each candidate
    final_percentage = []
    for k, v in vote_count.items():
        percentage_won  = {}
        percentage_won = v * 100.0 / total_votes
        percentage_won = k, round(percentage_won, 3)
        #Append percentage won for each candidate inside dictionary
        final_percentage.append(percentage_won)
        #Determine election winner from vote_count dictionary
        winner = max(vote_count, key=vote_count.get)
    #Print winner, percentage won for each candidate, number of votes won for each candidate, and total number of votes        
    print("Winner is: "  + str(winner))
    print("Final Percentages are %: " + str(final_percentage))    
    print("Total votes won per candidate: " + str(vote_count))          
    print("Total Number of Votes: " + str(total_votes))
# I am sorry for somewhat convoluted way to write into text file, it was only way I figured out:) 
#If possible, I would like feedback, on how could I improve my coding efficiency, I know that all of these nested for loops aren't ideal
    with open(r"C:\Git\ClassWork_HomeWork\python-challenge\PyPoll\Analized_PyPoll", 'w') as file:
            file.write(f"\nElection Results")
            file.write(f"\n_________________________________")
            file.write(f"\nTotal Votes: " + str(total_votes))
            file.write(f"\n_________________________________")
            file.write(f"\nPercentage Won: {final_percentage[0]}")
            file.write(f",Votes Won: " + str(vote_count["Khan"]))
            file.write(f"\nPercentage Won: {final_percentage[1]}")
            file.write(f",Votes Won: " + str(vote_count["Correy"]))
            file.write(f"\nPercentage Won: {final_percentage[2]}")
            file.write(f",Votes Won: " + str(vote_count["Li"]))
            file.write(f"\nPercentage Won: {final_percentage[3]}")
            file.write(f",Votes Won: " + str(vote_count["O'Tooley"]))
            file.write(f"\nWinner is: " + str(winner))

