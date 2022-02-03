from operator import indexOf
import random

def ex1():
    user_list = []
    
    for index in range(4):
        user_input = int(input("[{0}] Enter a number: ".format(index+1)))
        user_list.append(user_input)
        
    print("")
        
    print("[a] Even index")
    for index in range(len(user_list)):
        if index % 2 == 0:
            print("[{0}] {1}".format(index, user_list[index]))
        
    print("")
    
    print("[b] Even values")
    for index in range(0, len(user_list)):
        if user_list[index] % 2 == 0:
            print("[{0}] {1}".format(index, user_list[index]))
        
    print("")
    
    print("[c] Insert a number at pos 1")
    user_input = int(input("Enter a number: "))
    user_list.insert(1, user_input)
    
    print("")
    
    print("[d] Check that the number was inserted correctly")
    index = indexOf(user_list, user_input)
    print(index, user_list[index])
    
    print("") 
    
    print("[e] Remove a number") 
    remove_number = int(input("Enter a number to remove: "))
    
    if(remove_number in user_list):
        user_list.remove(remove_number)
        print("Number removed")
        
    else:
        print("Number not found")
        
    print("")
    
    print("[f] Check if number is still in the list")
    if(remove_number in user_list):
        print("Number in list", user_list)
        
    else:
        print("Number not in list", user_list)
    
    print("")
    
    print("[g] Print all values in reverse order")
    print(user_list[::-1])
    
def ex2():
    user_list = []
    
    for index in range(4):
        user_input = int(input("[{0}] Enter a number: ".format(index+1)))
        user_list.append(user_input)
        
    print("")
        
    print("Search for a number?")
    print("--------------------")
    
    user_input = input("[y]es or [n]o: ")
    
    if(user_input.capitalize() == "Y"):
        search_bool = True
        
    else:
        search_bool = False
    
    while search_bool == True:
        search_input = int(input("Enter a number to search for: "))
        
        if search_input in user_list:
            index = user_list.index(search_input)
            print("Number found at index: " + str(index))
            
        else:
            print("Number not found")
            
        user_input = input("Do you wish to search for another number? (y/n): ")
        
        if(user_input.capitalize() != "Y"):
            search_bool = False

def ex3():
    random_list = []
    
    for index in range(5):
        random_list.append(random.randint(0, 100))
        
    print("")
    
    print("[a] Random numbers")
    for index, value in enumerate(random_list):
        print("[{0}] {1}".format(index+1, value))
        
    print("")
    
    print("[b] Lowest number")
    lowest = min(random_list)
    print(lowest)
        
    print("")
    
    print("[c] Highest number")
    highest = max(random_list)
    print(highest)
        
    print("")
    
    print("[d] Difference between lowest and highest")
    print(highest - lowest)
    

        