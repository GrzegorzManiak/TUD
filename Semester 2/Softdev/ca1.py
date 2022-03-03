# X00189661 Grzegorz Maniak

recruit_list = [
    ["RS100", "Mary Moore",  "F", "Dublin", "Python"],
    ["RS200", "John Moore",  "P", "Dublin", "Python"],
    ["RS300", "Sean Enright",  "P", "Cork", "Java"],
    ["RS400", "Kate Nugent",  "F", "Galway", "Java"],
    ["RS500", "Eliza Smith",  "F", "Sligo", "Python"]
]

# Option 1: Display full- time students
def opt1():
    print("*" * 50)
    print("{0:^50}".format("Full time student details"))
    print("*" * 50)
    print("Name\tCity")
    print("*" * 50)
    for student in recruit_list:
        if student[2] == "F":
            print("{0}\t{1}".format(student[1], student[3]))
            
    print("\n" * 2)

# Option 2. Add a Student  
def opt2():
    print("*" * 50)
    print("Add student")
    print("")
    
    while True:
        print("" * 2)
        
        # Get student id
        id_input = input("Student ID: ")
        
        # If the student id is too long
        if len(id_input) > 5:
            print("Invalid student id! Your id must be 5 characters")
            continue
        
        # Get the fist 2 characters of the input
        if id_input[:2] != "RS":
            print("Invalid student ID, must start with RS!")
            continue
        
        # Get the last 3 characters of the input
        # Make sure its a number
        if id_input[-3:].isdigit() == False:
            print("Invalid student ID digit's")
            continue
        
        for student in recruit_list:
            if id_input.lower() == student[0].lower():
                print("Student ID already exists! It must be unique!")
                continue
        
        name_input = input("Student Name: ")
        
        course_input = input("Course: ")
        
        # Check if the course code is F or P
        if course_input.lower() == "f" or course_input.lower() == "p":
            course_input = course_input.upper()
        
        # else, tell the user his input is invalid
        else:
            print("Invalid course type!")
            continue
        
        city_input = input("City: ")
        language_input = input("Programming Language: ")
        
        recruit_list.append([
            id_input, 
            name_input, 
            course_input, 
            city_input, 
            language_input
        ])
        
        break
             
    print("\n" * 2)

# Option 3: City Search 
def opt3():
    print("*" * 50)
    
    # When the user enters the city, make it lower case.
    city_input = str(input("Enter city: ")).lower()
    
    print("*" * 50)
    # center the text
    print("{0:^50}".format(city_input + " Matches"))
    print("*" * 50)
    
    print("Name\tSkills")
    
    # Go trough the rectuit list and see 
    # if we come up with any matches
    for student in recruit_list:
        if student[3].lower() == city_input:
            print("{0}\t{1}".format(student[1], student[4]))

# Option 4. Update Skills
def opt4():
    print("*" * 50)
    print("Update Skills")
    print("")
    
    # For each student in the list
    # Append the string to the start of the skills
    for student in recruit_list:
        student[4] = "Problem Solving, " + student[4]
        
    print("ID\tName\tCourse\tCity\tSkills")
    for student in recruit_list:
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(student[0], student[1], student[2], student[3], student[4]))
            
while True:
    print("\n" * 2)
    print("*" * 50)
    print("{0:^50}".format("Recruitment System"))
    print("*" * 50)
    print("")
    print("1. List all full time students")
    print("2. Add a student")
    print("3. Search by city")
    print("4. Update Skills")
    print("5. Exit")
    print("*" * 50)
    
    choice = int(input("\nEnter your choice: "))
    
    if choice > 5 or choice < 1:
        print("\nInvalid choice!")
        continue
    
    else:
        if(choice == 1): opt1()
        elif(choice == 2): opt2()
        elif(choice == 3): opt3()
        elif(choice == 4): opt4()
        elif(choice == 5): break

