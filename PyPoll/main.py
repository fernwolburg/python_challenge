import os
import csv

# open csv file path
electioncsv = '/Users/fernandawolburg/Downloads/election_data.csv'

# open csv file
with open(electioncsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #vdeclare your ariables here
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Tooley_votes = 0
    
    #start loop that will go through the csv and add to votes everytime the 
    #name is matched
    for row in csvreader:
    
        #add the row to total_votes count
        total_votes = total_votes + 1
        
        #if the name in row[2] = Khan, then add to Khan_votes
        if row[2] == "Khan":
            Khan_votes = Khan_votes + 1
           
        #elf the name in row[2] = Correy, then add to Correy_votes
        elif row[2] == "Correy":
            Correy_votes = Correy_votes + 1
        
            
        #elif if the name in row[2] = Li, then add to Li_votes
        elif row[2] == "Li":
            Li_votes = Li_votes + 1
          
            
        #elif if the name in row[2] = O'Tooley, then add to Tooley_Votes
        elif row[2] == "O'Tooley":
            Tooley_votes = Tooley_votes + 1
            

    # List to store candidate votes
    candidates = [(Correy_votes, 'Correy'), 
                  (Li_votes, 'Li'),
                  (Tooley_votes, "O'Tooley"),
                  (Khan_votes, 'Khan')]
          
    #to figure out which person had the highest votes
    #order the 'candidates' list from highest to lowest value
    candidates.sort(reverse = True)
    #create a variable that will hold the first value of the 'candidates' list
    winner = candidates[0]

    #turn votes into percentages
    pkhan_votes = (Khan_votes/total_votes) * 100
    pcorrey_votes = (Correy_votes/total_votes) * 100
    pli_votes = (Li_votes/total_votes) * 100
    ptooley_votes = (Tooley_votes/total_votes) * 100
  
#print out the message    
print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {pkhan_votes}% ({Khan_votes} votes)")
print(f"Correy: {pcorrey_votes}% ({Correy_votes} votes)")
print(f"Li: {pli_votes}% ({Li_votes} votes)")
print(f"O'Tooley: {ptooley_votes}% ({Tooley_votes} votes)")
print("-------------------------")
print(f"Winner: {winner[1]}")
print("-------------------------")
