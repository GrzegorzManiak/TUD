# X00189661 Grzegorz Maniak

import lab10 as lab

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
            print(lab.add(*lab.getNumbersInput()))
            
        elif choice == "2":
            print(lab.subtract(*lab.getNumbersInput()))
            
        elif choice == "3":
            print(lab.multiply(*lab.getNumbersInput()))
            
        elif choice == "4":
            print(lab.divide(*lab.getNumbersInput()))
            
        elif choice == "5":
            print(lab.power(*lab.getNumbersInput()))
            
        elif choice == "6":
            print(lab.list_of_squares(*lab.getNumbersInput()))
            
        elif choice == "7":
            print(lab.upper_lower_case(input("Enter a string: ")))
            
        elif choice == "8":
            lab.display_element(input("Enter a string: "), int(input("Enter a number: ")))
            
        elif choice == "9":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please enter a valid choice:")
        
menu()