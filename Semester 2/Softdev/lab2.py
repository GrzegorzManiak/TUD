
def ex1():
    votes = []
    names = []
        
    for index in range(5):
        names_input = input("Enter name for candidate " + str(index+1) + ": ")
        
        votes_input = int(input("Enter votes for candidate (" + str(index+1) + "): "))
        
        votes.append(votes_input)
        names.append(names_input)
    
    print("Candidate    Votes recived    Percentage")
    print("----------------------------------------")
    
    total = sum(votes)
    
    for people in enumerate(votes):
                
        percentage = round((people[1]/total) * 100, 2)
        
        print("Candidate " + str(names[people[0]]) + "  " + str(votes[people[0]]) + "   " + str(percentage))
    
   
    print("")
    
    print("Total votes      : " + str(sum(votes)))
    print("Average votes    : " + str(sum(votes)/len(votes)))
    
    print("")
    
    print("Most votes       : " + str(names[votes.index(max(votes))]))
    print("Least votes      : " + str(names[votes.index(min(votes))]))
    
    
def ex2():
    hours_worked = []
    
    for index in range(5):
        hours_input = int(input("Enter hours worked for day " + str(index+1) + ": "))
        
        while hours_input < 0 or hours_input > 9:
            print("Invalid input. Try again: ")
            hours_input = int(input("Enter hours worked for day " + str(index+1) + ": "))
        
        hours_worked.append(hours_input)
    
    print("Hours worked each day")
    print("---------------------")
    
    for people in enumerate(hours_worked):
        print(str(people[0]+1) + ": " + str(people[1]))
    
    print("")
    
    print("Total hours worked: " + str(sum(hours_worked)))
    print("Average hours worked: " + str(sum(hours_worked)/len(hours_worked)))
    
    print("")
    
    print("Days worked over 6 hours: " + str(hours_worked.count(6)))
    

names_ = ["John", "Paul", "George", "Ringo", "Pete", "john"]    
list_ = [ 345345, 353, 456456, 345345, 345, 345 ]

for item in enumerate(list_):
    print(item)
    print(names_[item[0]])