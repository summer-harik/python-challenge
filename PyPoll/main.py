#Import the os and csv modules
import os
import csv

#assign path for csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#dict to hold candidate values
candidates = {}

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip header row
    next(csvreader,None)

#set vote count value to 0
    vote_count = 0

#loop thru rows in the csv file
    for row in csvreader:

#count the total votes        
        vote_count+=1 

#get and store the candidate values
        candidate_name = row[2]

 #if the candidate name is already listed in the dict, add 1 to their total       
        if candidate_name in candidates:
            candidates[candidate_name]+=1
        else:
            candidates[candidate_name] = 1

 #calculate the vote percentage for each candidate
    candidates["Charles %"]= round((candidates['Charles Casper Stockham']/vote_count)*100,2)      
    candidates["Diana %"]= round((candidates['Diana DeGette']/vote_count)*100,2)    
    candidates["Raymon %"]= round((candidates['Raymon Anthony Doane']/vote_count)*100,2)    

#determine the winner by finding the max value of the dict *max of dict found on stackoverflow*
winner_name = max(candidates, key=candidates.get)

#print values
print(f"Total Votes: {vote_count}")
print(f"{candidates}")
print("Winner: " + winner_name)

output_file = os.path.join('/Users/summerharik', 'Desktop','PyPoll_Analysis.txt')

f = open(output_file, "w")

#write txt file lines *format found on stackoverflow*
f.write(f"Total Votes: {vote_count}\n")
f.write(f"{candidates}\n")
f.write(f"Winner: {winner_name}\n")
f.close()





      

