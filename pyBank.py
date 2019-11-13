#!/usr/bin/env python
# coding: utf-8

# In[13]:



# coding: utf-8

# In[68]:




# Dependencies

import csv

# Files to load and output (Remember to change these)
file_to_load = "Resources/budget_data.csv"
file_to_output = "Output/pyBankAnalysis.txt"

total_months = 0
total_amount = 0
previous = 0
monthly_change = []
maxIncrease = 0
maxDecrease = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:
        # Track the total
        total_months = total_months + 1
        total_amount = total_amount + int(row['Profit/Losses'])

        if total_months > 1 :
            change=int(row['Profit/Losses'])-previous
            monthly_change.append(change)
        
            if change > maxIncrease :
                maxIncrease = change
                maxIncreaseMonth = row['Date']
                
            if change < maxDecrease :
                maxDecrease = change
                maxDecreaseMonth = row['Date']                
            
        previous=int(row['Profit/Losses'])
        
average = round(sum(monthly_change)/(len(monthly_change)+0.0),2)

output=('Total number of months = ' + str(total_months)+'\n'+
'Total net amount pf profit/loses = ' + str(total_amount)+'\n' +
'Average change in profit/losses between months = ' + str(average) + '\n'
'The greatest increase in profits (date and amount) = ' + maxIncreaseMonth + ' $'+str(maxIncrease) + '\n' +       
'The greatest decrease in losses (date and amount) = ' + maxDecreaseMonth + ' $'+str(maxDecrease) + '\n' )

print(output)

with open(file_to_output,'w') as outputfile:
        outputfile.write(output)
        




