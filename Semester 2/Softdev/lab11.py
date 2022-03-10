# EX1

import random

def populate_list(list, num_values, lower_bound, upper_bound):
    for i in range(num_values):
        list.append(random.randint(lower_bound, upper_bound))
        
def display_list(list):
    for i in range(len(list)):
        print("Element {0}, In list {1}".format(i + 1, list[i]))
        
def num_of_negatives(list):
    # Create a counter
    counter = 0
    
    # Loop through the list
    for i in range(len(list)):
        # If the number is negative
        if list[i] < 0:
            # Increment the counter
            counter += 1
            
    # Return the counter
    return counter

def even_count(list):
    # Instantiate the counter
    even = 0
    
    # Loop trough the list
    for i in range(len(list)):
        
        # If the value is 0, do nothing
        if list[i] == 0:
            break
        
        # If the number is even, incrament even
        elif list[i] % 2 == 0:
            even += 1
    
    # Retrun the counter
    return even
        
def mainEX1():
    # Create an empty list
    list = []
    
    # Populate the list with 10 values
    populate_list(list, 10, -5, 5)
    
    # Display the list
    display_list(list)
    
    print("")
    
    # Call the num_of_negatives function
    print("Number of negatives: {0}".format(num_of_negatives(list)))
    
    # Call the even_count function
    print("Number of evens: {0}".format(even_count(list)))
    
# mainEX1()

# EX2
def print_lists(list, results):
    for index in range(len(list)):
        print("Student {0} has a result of {1}".format(list[index], results[index]))

def find_index(names_list, name):
    # Instantiate the index at -1
    index = -1
    
    # Loop trough the list
    for name_index in range(len(names_list)):
        # Do the names match?
        if names_list[name_index] == name:
            # If so, set the index
            index = name_index
    
    # Return the index
    return index
        
def get_above_average(names_list, results_list, average):
    # Create an empty list
    above_average = []
    
    # Loop through the list
    for i in range(len(results_list)):
        # If the result is above the average
        if results_list[i] > average:
            # Add the name to the list
            above_average.append(names_list[i])
    
    # Return the list
    return above_average
    
def mean(list):
    total = 0
    
    for index in range(len(list)):
        total += list[index]
        
    return total / len(list)

def mainEX2():
    # Create empty lists
    student_names = []
    student_results = []
    
    # Get the number of students
    num_students = int(input("How many students: "))
    
    # Loop through the number of students
    for i in range(num_students):
        while True:
            # Get the student name
            student_name = input("Student name: ")
            
            # Get the student result
            student_result = float(input("Student result: "))
            
            if student_result > 100:
                print("Invalid results value")
                continue
            
            # Add the student name to the list
            student_names.append(student_name)
            
            # Add the student result to the list
            student_results.append(student_result)
            
            # Break out of the loop
            break
    
    # Call the print_lists function
    print_lists(student_names, student_results)
    
    # ask the user if they want to find a user
    name = input("Students name to find (case sensitive): ")
    
    # Invoke the find_index function
    name_index = find_index(student_names, name)
    
    # If no one is found, tell the user that 
    if name_index == -1:
        print("No student was found with the name of {0}".format(name))
        
    else: print("Student {0} was found at index {1}".format(name, name_index))
    
    # Get the avg grade 
    mean_value = mean(student_results)
    
    # Check who got above avg
    above_avg = get_above_average(student_names, student_results, mean_value)
    
    if len(above_avg) < 1:
        print("No one got above avg")
        
    else:
        for index in range(len(above_avg)):
            print("Student {0} scored above avg".format(above_avg[index]))
        
mainEX2()