# importing modules
import os
import csv

# # Finding and storing file path
csvpath = os.path.join(os.getcwd(),'pybank','resources','budget_data.csv')

# reading csv file
with open(csvpath,'r') as csvfile:

    #initialize the writer
    csvreader = csv.reader(csvfile, delimiter=',')
    total_profit_and_loss = 0
    
    #print total months
    for row in csvreader:
        total_months = len(list(csvreader))
        print(f'Total Months: {total_months}')


with open(csvpath,'r') as csvfile:
    #initialize the writer
    csvreader = csv.DictReader(csvfile, delimiter=',')
    total_profit_and_loss = 0

    for row in csvreader:
        total_profit_and_loss += int(row['Profit/Losses'])

print(f'Total: {total_profit_and_loss}')

with open(csvpath,'r') as csvfile:
    #initialize the writer
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    list_PandL = []
    list_change_in_PandL = []
    change_in_PandL = 0
    sum_change_in_PandL = 0
    average_change = 0
    for row in csvreader:
        list_PandL.append(int(row[1]))

# print(len(list_PandL))
end = len(list_PandL)

for x in range(1,end):
    change_in_PandL = list_PandL[x] - list_PandL[x - 1]
    list_change_in_PandL.append(int(change_in_PandL))

# print(change_in_PandL)
# print(list_change_in_PandL)

sum_change_in_PandL = sum(list_change_in_PandL)

# print(sum_change_in_PandL)

average_change = sum_change_in_PandL / len(list_change_in_PandL)

print(f'Average change: {average_change}')