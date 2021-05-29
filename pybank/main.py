print(f'Financial Analysis')
print(f'___________________________')

# importing modules
import os
import csv
from typing_extensions import Final

# # Finding and storing file path
csvpath = os.path.join(os.getcwd(),'pybank','resources','budget_data.csv')

# reading csv file
with open(csvpath,'r') as csvfile:
    # creating variables
    total_months = 0
    total_profit_and_loss = 0
    list_dates = []
    list_PandL = []
    list_change_in_PandL = []
    change_in_PandL = 0
    sum_change_in_PandL = 0
    average_change = 0
    greatest_decrease = 0 
    greatest_increase = 0
    greatest_increase_date = ''

    #initialize the writer
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) #remove header
    
    for row in csvreader:
        list_PandL.append(int(row[1])) # making a list of profit and loss as integers
        list_dates.append(row[0])      # making list of dates as string
        total_profit_and_loss = sum(list_PandL) # formula to calculate total profit
        total_months = len(list_PandL)  # formula to calculate total months
        end = len(list_PandL) # variable to count the end of list
            
    for x in range(1,end):  # no change recorded in the first row hence start at 1
        change_in_PandL = list_PandL[x] - list_PandL[x - 1] #calculating change from the bottom up
        list_change_in_PandL.append(int(change_in_PandL)) #making a new list for change in P&L

        sum_change_in_PandL = sum(list_change_in_PandL) # formula for sum of change in P&L
        average_change = sum_change_in_PandL / len(list_change_in_PandL) # formula for average change
    
        greatest_increase = max(list_change_in_PandL) # formula for greatest increase
        greatest_decrease = min(list_change_in_PandL) # formula for greatest decrease
        greatest_increase_index = list_change_in_PandL.index(greatest_increase) # finding index for greatest increase
        greatest_decrease_index = list_change_in_PandL.index(greatest_decrease) # finding index for greatest decrease
        greatest_increase_date = list_dates[greatest_increase_index + 1]    # code to find date - adding 1 to move down
        greatest_decrease_date = list_dates[greatest_decrease_index + 1]    # code to find date - adding 1 to move down

average_change = round(average_change , 2)  # rouding average change

# print statements
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_and_loss}')
print(f'Average change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}')

financial_analysis = os.path.join(os.getcwd(),'pybank','analysis','financial_analysis.txt')

with open (financial_analysis, 'w') as file:
    
    file.write(f'Financial Analysis')
    file.write(f'\n')
    file.write(f'___________________________')
    file.write(f'\n')
    file.write(f'Total Months: {total_months}')
    file.write(f'\n')
    file.write(f'Total: ${total_profit_and_loss}')
    file.write(f'\n')
    file.write(f'Average change: ${average_change}')
    file.write(f'\n')
    file.write(f'Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}')
    file.write(f'\n')
    file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}')