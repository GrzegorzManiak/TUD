# X00189661 Grzegorz Maniak

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b    

def power(a, b):        
    if b <= 0:
        while True:
            print("Invalid value, please enter a valid value for the power:")
            b = int(input())
            if b >= 0:
                break
    
    return a ** b
        
def list_of_squares(a, b):
    list_of_squares = []
    
    for i in range(a, b + 1):
        list_of_squares.append(i ** 2)
        
    return list_of_squares

def upper_lower_case(string):
    upper_case = 0
    lower_case = 0
    
    for i in range(len(string)):
        if string[i].isupper():
            upper_case += 1
            
        else:
            lower_case += 1
            
    print("No. of Upper case characters : " + str(upper_case))
    print("No. of Lower case Characters : " + str(lower_case))

def display_element(string, number):    
    if number <= 0 or number > len(string):
        while True:
            print("Invalid value, please enter a valid value for the element:")
            number = int(input())
            if number > 0 and number <= len(string):
                break
    else:
        print(string[number - 1])

def getNumbersInput():
    result = []
    
    while True:
        print("Enter a number:")
        number = int(input())
        
        print("Enter another number:")
        number2 = int(input())
        
        result = [number, number2]
        
        break

    return result

def menu():
    while True: 
        print("****************************")
        print("* Calculator + *")
        print("1- Add")
        print("2- Subtraction")
        print("3- Multiplication")
        print("4- Division")
        print("5- Raise to the power")
        print("6- List of squares")
        print("7- Upper and Lower Case")
        print("8- Display specific element")
        print("9- Exit")
        print("****************************")
        print("Please enter menu option:")
        
        choice = input()
        
        if choice == "1":
            print(add(*getNumbersInput()))
            
        elif choice == "2":
            print(subtract(*getNumbersInput()))
            
        elif choice == "3":
            print(multiply(*getNumbersInput()))
            
        elif choice == "4":
            print(divide(*getNumbersInput()))
            
        elif choice == "5":
            print(power(*getNumbersInput()))
            
        elif choice == "6":
            print(list_of_squares(*getNumbersInput()))
            
        elif choice == "7":
            print(upper_lower_case(input("Enter a string: ")))
            
        elif choice == "8":
            display_element(input("Enter a string: "), int(input("Enter a number: ")))
            
        elif choice == "9":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please enter a valid choice:")
        
menu()