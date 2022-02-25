# Create a program for a Student system.
# The program should have a menu to select options, where after each option except exit, the
# program redisplays the menu.
# The menu should look similar to:

student_list = [
    ["X100", "John Smith", "y", 1, 0, 70, 80],
    ["X200", "Daphne Towles", "y", 1, 0, 50, 55],
    ["X300", "Jane Barry", "y", 1, 0, 45, 65],
    ["X400", "Alice Jones", "n", 2, 1000, 60, 70],
    ["X500", "Ian Reeves", "n", 2, 2000, 50, 40]
]

choice = 0

while(True):
    print("")
    print("1) Llist all students")
    print("2) List Un-Registered Students")
    print("3) Calculate Student Average")
    print("4) Lowest CA1 Grade")
    print("5) Exit")

    choice = int(input("Please select an option: "))
    
    if choice < 6 or choice > 0:
        break
    
    else: 
        print("Invalid choice")

if choice == 1:
    print("")
    print("Student ID\tName\t\tCA1\tCA2")
    for student in student_list:
        print(student[0], "\t", student[1], "\t", student[4], "\t", student[5], "\t", student[6])
        
elif choice == 2:
    print("")
    print("Student ID\tName")
    for student in student_list:
        if student[2] == "n":
            print(student[0], "\t", student[1])
        
elif choice == 3:
    print("")
    print("Student ID\tName\t\tAverage")
    for student in student_list:
        average = (student[4] + student[5]) / 2
        print(student[0], "\t", student[1], "\t", average)

elif choice == 4:
    lowest = []
    print("")
    print("Student ID\tName")
    for student in student_list:
        if student[4] < student[5]:
            lowest = student
            
    print(lowest[0], "\t", lowest[1])