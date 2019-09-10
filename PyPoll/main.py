import os
import csv

csvpath = os.path.join('election_data.csv')

total_votes = 0 
candidates = []
candidate_votes =[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
            #if candidate not in candidates list then add to list and add 1 to vote count
            candidates.append(candidate_in)
            candidate_votes.append(1)

prct = []
max_votes = candidate_votes[0]
max_idx = 0

for x in range(len(candidates)):
    #lets get that percentage now! **Go back to stack overflow and look it up again**
    vote_prct = round(candidate_votes[x]/total_votes * 100, 2)
    prct.append(vote_prct)

    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_idx = x

winner = candidates[max_idx]

#lets print this to the terminal and see if it works ***USE THE PRINT FUNCTION CLINT***
print('ELECTION RESULTS')
print('---------------------------------')
print(f'TOTAL VOTES: {total_votes}')
print('---------------------------------')
for x in range(len(candidates)):
    print(f'{candidates[x]} : {prct[x]}% ({candidate_votes[x]})')
print('---------------------------------')
print(f'WINNER OF THE ELECTION: {winner.upper()}')

#that worked print it to the .csv now, look at the pandas and last weeks lesson for this! 
printcsv = os.path.join("fin_vote_tally.csv")
with open(printcsv, 'w', newline='') as file:
    file.write('ELECTION RESULTS')
    file.write('\n')
    file.write('--------------------------')
    file.write('\n')
    file.write(f'TOTAL VOTES: {total_votes}')
    file.write('\n')
    file.write('--------------------------')
    file.write('\n')
    for x in range(len(candidates)):
        file.write(f' {candidates[x]} : {prct[x]}% ({candidate_votes[x]}) ' )
    file.write('\n')
    file.write('----------------------------')
    file.write('\n')
    file.write(f'WINNER OF THE ELECTION: {winner.upper()}')



