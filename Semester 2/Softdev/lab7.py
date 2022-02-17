# X00189661 Grzegorz Maniak

def ver1():
    TOTAL_CANDIDATES = 4
    SPACEING = 15

    candidates = []

    for i in range(TOTAL_CANDIDATES):
        print('--- Candidate {} ---'.format(i + 1))
        candidates.append([])
        
        candidates[i].append(input("Enter the last name of the candidate: "))
        
        candidates[i].append(int(input("Enter the number of votes received by the candidate: ")))
        
        candidates[i].append(input("Enter the constituency of the candidate: "))
        
        print('')


    total_votes = 0

    for index in range(TOTAL_CANDIDATES):
        total_votes += candidates[index][1]
        
    print('')
    print('Name         Votes         Constituency         %')
    print('-------------------------------------------------')

    for index in range(TOTAL_CANDIDATES):
        name = candidates[index][0]
        votes = candidates[index][1]
        constituency = candidates[index][2]
        percent = round(candidates[index][1] / total_votes * 100, 2)
        
        candidates[index].append(float(percent))
        
        name += ' ' * (SPACEING - len(name))
        votes = str(votes) + ' ' * (SPACEING - len(str(votes)))
        constituency = constituency + ' ' * (SPACEING - len(constituency))
        
        print('{0} {1} {2} {3}%'.format(name, votes, constituency, percent))
        
    print('')

    winner = [0.0, '']
    for index in range(TOTAL_CANDIDATES):
        if candidates[index][3] > winner[0]:
            winner = [
                candidates[index][3],
                candidates[index][2]
            ]
            
    print('Winner: {0}, with a total percentage of {1}%'.format(winner[1], winner[0]))
    
    
    looser = [100.0, '']
    for index in range(TOTAL_CANDIDATES):
        if candidates[index][3] < winner[0]:
            looser = [
                candidates[index][3],
                candidates[index][2]
            ]
    
    print('Looser: {0}, with a total percentage of {1}%'.format(looser[1], looser[0]))
           
def ver2():
    TOTAL_CANDIDATES = 4
    SPACEING = 15

    candidates = []
    
    for i in range(TOTAL_CANDIDATES):
        print('--- Candidate {} ---'.format(i + 1))
        candidates.append([])
        
        candidates[i].append(input("Enter the last name of the candidate: "))
        
        candidates[i].append(int(input("Enter the number of votes received by the candidate: ")))
        
        candidates[i].append(input("Enter the constituency of the candidate: "))
        
        print('')


    total_votes = 0
    for index in range(TOTAL_CANDIDATES):
        total_votes += candidates[index][1]
        
        
    print('')
    print('Name         Votes         Constituency         %')
    print('-------------------------------------------------')

    for index in range(TOTAL_CANDIDATES):
        name = candidates[index][0]
        votes = candidates[index][1]
        constituency = candidates[index][2]
        percent = round(candidates[index][1] / total_votes * 100, 2)
        
        candidates[index].append(percent)
        
        name += ' ' * (SPACEING - len(name))
        votes = str(votes) + ' ' * (SPACEING - len(str(votes)))
        constituency = constituency + ' ' * (SPACEING - len(constituency))
        
        print('{0} {1} {2} {3}%'.format(name, votes, constituency, percent))
        
    print('')

    unique_results = []
    
    for index in range(TOTAL_CANDIDATES):
        if candidates[index][3] not in unique_results:
            unique_results.append(candidates[index][3])
    
    unique_results.sort()
    
    winner = unique_results[0]
    looser = unique_results[len(unique_results) - 1]
    
    total_winners = []
    for index in range(TOTAL_CANDIDATES):
        if candidates[index][3] == winner:
            total_winners.append(candidates[index][2])
            
    for index in range(len(total_winners)):
        if len(total_winners) == 1:
            print('Winner: {0} with a percentage of {1}%'.format(total_winners[index], winner))
        else:
            print('Draw Winner: {0} with a percentage of {1}%'.format(total_winners[index], winner))
             
             
    print('')
    
    
    total_losers = []
    for index in range(TOTAL_CANDIDATES):
        if candidates[index][3] == looser:
            total_losers.append(candidates[index][2])
            
    for index in range(len(total_losers)):
        if len(total_losers) == 1:
            print('Looser: {0} with a percentage of {1}%'.format(total_losers[index], looser))
        else:
            print('Draw Looser: {0} with a percentage of {1}%'.format(total_losers[index], looser))

    