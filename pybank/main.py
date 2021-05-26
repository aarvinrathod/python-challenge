# importing modules
import os
import csv

# # Finding and storing file path
csvpath = os.path.join(os.getcwd())

# reading csv file
with open(csvpath,'r') as csvfile:

    #initialize the writer
    csvreader = csv.reader(csvfile, delimiter=',')

    #print total months
    for row in csvreader:
        total_months = len(list(csvreader))
        print(f'Total Months: {total_months}')

    total_profit_and_loss = 0

    for row in csvreader:
        total_profit_and_loss += int(row['Profit/Losses'])
        print(f'Total: {total_profit_and_loss}')