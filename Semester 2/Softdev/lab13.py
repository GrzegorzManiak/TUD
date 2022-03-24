# X00189661 Grzegorz Maniak

import time

staff_list = [
    [ 100, "Jones", "Jack", "01-10-2000", 5, 60000, 0 ],
    [ 200, "Smith", "Mary", "01-07-2000", 6, 70000, 0 ],
    [ 300, "Bennett", "Patrick", "01-11-2001", 6, 70000, 0 ],
    [ 400, "Lewis", "Ann", "01-12-2011", 4, 40000, 0 ]
]

def valid_grade(grade):
    if grade > 0 and grade <= 8:
        return True
    else:
        return False
    
def add_employee():
    while True:
        staff_id = int(input("Enter the staff ID:"))

        first_name = input("Enter the first name:")

        surname = input("Enter the surname:")

        date_of_commencement = input("Enter the date of commencement of employment:")

        grade = int(input("Enter the grade: "))
        
        if valid_grade(grade) == False:
            while True:
                grade = int(input("Invalid value, please enter a valid value for the grade: "))
                
                if valid_grade(grade):
                    break
            
        salary = int(input("Enter the salary:"))
        
        bonus = int(input("Enter the bonus: "))
        
        staff_list.append([staff_id, first_name, surname, date_of_commencement, grade, salary, bonus])
        break

def search_emp(staff_list, staff_id):
    for employee in staff_list:
        if employee[0] == staff_id:
            print("Staff ID:", employee[0])
            print("First Name:", employee[1])
            print("Surname:", employee[2])
            print("Date of Commencement:", employee[3])
            print("Grade:", employee[4])
            print("Salary:", employee[5])
            print("Bonus:", employee[6])
            
            print("-" * 20)
            break
    else:
        print("Employee not found")

def emp_display(staff_list):
    for employee in staff_list:
        print("Staff ID:", employee[0])
        print("First Name:", employee[1])
        print("Surname:", employee[2])
        print("Date of Commencement:", employee[3])
        print("Grade:", employee[4])
        print("Salary:", employee[5])
        print("Bonus:", employee[6])
        print("-" * 20)
        
    print("Number of employees:", len(staff_list))
    
def calc_bonus(staff_list):
    for employee in staff_list:
        start_year = int(employee[3].split("-")[2])
        current_year = int(time.strftime("%Y"))
        bonus = employee[5] * (current_year - start_year) / 100
        employee[6] = bonus

def menu():
    while True: 
        print("*" * 20)
        print("*{:^18}*".format("HR Department"))
        print("*" * 20)
        print("1- Add Employee")
        print("2- Search Employee")
        print("3- List Employees")
        print("4- Set Bonus")
        print("5- Exit")
        print("*" * 20)
        print("Please enter menu option:")
        
        choice = input()
        
        if choice == "1":
            print("Add Employee")
            add_employee()
            
        elif choice == "2":
            print("Search Employee")
            search_emp(staff_list, int(input("Enter the staff ID:")))
            
        elif choice == "3":
            print("List Employees")
            emp_display(staff_list)
            
        elif choice == "4":
            print("Set Bonus")
            calc_bonus(staff_list)
            
        elif choice == "5":
            print("Exit")
            break
            
        else:
            print("Invalid option")

menu()