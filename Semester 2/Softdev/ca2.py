# X00189661 Grzegorz Maniak

# -----------[Functions start]----------- #
    
from random import Random


def print_flights(flights_list):
    print('*' * 40)
    print('{0:^40}'.format('Booking details'))
    print('*' * 40)
    
    print('{0:20} {1:20}'.format('Name', 'Destination'))
        
    for employee in flights_list:
        print('{0:20} {1:20}'.format(employee[1], employee[2]))
    
    print()

def determine_total_cost(flights_list):
    totalCost = 0
    
    for employee in flights_list:
        totalCost += employee[3]
        
    # Keyboard dosent have the euro symbol, hopfully $$$$$$$ works
    print('Total cost of employees\' flights ${0:0.2f}'.format(totalCost))
    
    print()

def valid_destination(valid_destinations: list, destination): 
    for validDestination in valid_destinations:
        if validDestination == destination:
            return True
        
    return False

def add_flight(valid_destinations, prices, flights_list):
    staffName = input('Staff\'s name : ')
    
    destination = input('Destination : ')
    
    if valid_destination(valid_destinations, destination) == False:
        while True:
            destination = input('   Re-enter Destination : ')
            
            if valid_destination(valid_destinations, destination) == True:
                break
    
    # Find the index of their destination 
    destinationIndex = valid_destinations.index(destination)
    
    flights_list.append([
        flights_list[destinationIndex],
        staffName,
        destination,
        prices[destinationIndex]
    ])
    
    print('Flight added\n')
    
def generate_password():
    password = ''
    
    rule1 = Random().randint(1, 50)
    password += str(rule1)
    
    for i in range(4):
        password += str('FN101'[Random().randint(0, 3)])
        
    if len(password) < 6:
        password += str(Random().randint(0, 9))
    
    print('New password : {0}'.format(password))
    
    print()
    
def display_menu():
    throwError = False
    errorMessage = ''
    
    while True:
        print('*' * 40)
        print('{0:^40}'.format('Travel Booking System'))
        print('*' * 40)
        
        if throwError == True:
            throwError = False
            print('Error: {0} \n'.format(errorMessage))
        
        print('1) Display staff flights')
        print('2) Display total cost')
        print('3) Add a flight')
        print('4) Generate Password')
        print('5) Exit')
        
        print('*' * 40)
        
        choice = input('Please enter option: ')
        
        print()
        
        if choice == '1':
            print_flights(flights_list)
            
        elif choice == '2':
            determine_total_cost(flights_list)
            
        elif choice == '3':
            add_flight(valid_destinations, prices, flights_list)
        
        elif choice == '4':
            generate_password()
            
        elif choice == '5':
            print('Exiting...')    
            exit()
            
        else:
            throwError = True
            errorMessage = '"{0}" is not a valid option, please try again.'.format(choice)
            
# -----------[Functions end]----------- #


# Column 1: Flight number
# Column 2: Name of the employee who travelled
# Column 3: Destination 
# Column 4: Price of ticket
flights_list = [
    ["FN109", "John Smith", "London",  55.99],
    ["FN202", "Mary Jones", "Madrid",  110.99],
    ["FN359", "Ann Murray", "Boston",  350.00],
    ["FN654", "Peter Moore", "Berlin",  150.00]
]

# Company offices
valid_destinations = ["London", "Madrid", "Boston", "Berlin", "Bonn"]

# Coresponding flight number
flight_numbers = ["FN109", "FN202", "FN359", "FN654", "FN878"]

# Coresponding flight price
prices = [55.99, 110.99, 350.00, 150.00, 125.00]

# -----------[Main]----------- #

display_menu()