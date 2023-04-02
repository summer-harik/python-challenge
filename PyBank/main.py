#Import the os and csv modules
import os
import csv

#assign path for csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#list to hold p/l values
p_l_list = []

#list to hold months
months = []

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip header row
    next(csvreader,None)

#set months, p/l total, and p/l change values to 0    
    months_count = 0
    
    total = 0

    p_l = 0

#loop thru rows in the csv file
    for row in csvreader:

#count the total months        
        months_count+=1 

#get and store the month
        months.append(row[0])

#calculate the total p/l
        total+=int(row[1])  

#calculate change in p/l, add the value to the p/l list, and get next value of p/l
        p_l_change = int(row[1]) - p_l
        p_l_list.append(p_l_change)
        p_l = int(row[1])

#calculate the average of p/l change
        avg_change = sum(p_l_list)/len(p_l_list)

#calculate greatest increase in p/l, store the value in an index, and get month
        greatest_in = max(p_l_list)
        greatest_in_index = p_l_list.index(greatest_in)
        greatest_in_date = months[greatest_in_index]

#calculate greatest decrease in p/l, store the value in an index, and get month
        greatest_dec = min(p_l_list)
        greatest_dec_index = p_l_list.index(greatest_dec)
        greatest_dec_date = months[greatest_dec_index]

#print values
    print(f"Total Months: {months_count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {greatest_in_date} ${greatest_in}")
    print(f"Greatest Decrease in Profits: {greatest_dec_date} ${greatest_dec}")

#export to txt file
output_file = os.path.join('/Users/summerharik', 'Desktop','PyBank_Analysis.txt')

f = open(output_file, "w")

#write txt file lines *format found on stackoverflow*
f.write(f"Total Months: {months_count}\n")
f.write(f"Total: ${total}\n")
f.write(f"Average Change: ${avg_change}\n")
f.write(f"Greatest Increase in Profits: {greatest_in_date} ${greatest_in}\n")
f.write(f"Greatest Decrease in Profits: {greatest_dec_date} ${greatest_dec}\n")
f.close()


      

