import os # importing module
import csv # importing module

csvpath = os.path.join(os.getcwd(),'pypoll','resources','election_data.csv') # storing file path

# reading csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # removing header
    # creating variables
    total_votes_cast = 0 
    voter_id_list = []
    candidate_list = []
    unique_name_list = []
    for row in csvreader:
        voter_id_list.append(int(row[0])) # creating a list of voterID
        total_votes_cast = len(voter_id_list) # findind total number of voters
        candidate_list.append(row[2]) # making list of all cast votes

for x in candidate_list:
    if x not in unique_name_list:
        unique_name_list.append(x) # finding names of unique candidates

results = {}
for y in candidate_list:
    if y in unique_name_list:
        if y in results:
            results[y] = results[y] + 1
        else:
            results[y] = 1

list_of_number_of_votes = list(results.values()) #finding number of votes each candidate received

list_of_percent_votes = []

list_of_percent_votes = [(z/total_votes_cast)*100 for z in list_of_number_of_votes] # percent of votes received

list_of_percent_votes_rounded = [round(n,2) for n in list_of_percent_votes] #rounding percentages

x = len(unique_name_list)
winning_votes = max(list_of_number_of_votes)
winning_index = list_of_number_of_votes.index(winning_votes) # finding index of winning candidate

# print statements

print('Election Results')
print('_________________________')
print(f'Total Votes: {total_votes_cast}')
print('_________________________')

# printing all results
for r in range(0,x):
    print(f'{unique_name_list[r]}: {list_of_percent_votes_rounded[r]}% ({list_of_number_of_votes[r]})')
    
print('_________________________')
print(f'Winner: {unique_name_list[winning_index]}')
print('_________________________')

election_analysis = os.path.join(os.getcwd(),'pypoll','analysis','election_analysis.txt')

with open (election_analysis, 'w') as file:
    
    file.write(f'Election Analysis')
    file.write(f'\n')
    file.write(f'___________________________')
    file.write(f'\n')
    file.write(f'Total Votes: {total_votes_cast}')
    file.write(f'\n')
    file.write(f'___________________________')
    file.write(f'\n')
    for r in range(0,x):
        file.write(f'{unique_name_list[r]}: {list_of_percent_votes_rounded[r]}% ({list_of_number_of_votes[r]})')
    file.write(f'\n')
    file.write(f'___________________________')
    file.write(f'\n')
    file.write(f'Winner: {unique_name_list[winning_index]}')
    file.write(f'\n')
    file.write(f'___________________________')
