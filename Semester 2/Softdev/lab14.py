# Question 1

class Student:
    def __init__(self, ID, name, subject, ca1, ca2):
        self.ID = ID
        self.name = name
        self.subject = subject
        self.ca1 = ca1
        self.ca2 = ca2
        self.grade = ""
        
    def print_student(self):
        print("Student ID: ", self.ID)
        print("Name: ", self.name)
        print("Subject: ", self.subject)
        print("CA1 result: ", self.ca1)
        print("CA2 result: ", self.ca2)
        print("Grade: ", self.grade)
        
    def set_grade(self):
        if (self.ca1 + self.ca2) / 2 >= 80:
            self.grade = "A"
            
        elif (self.ca1 + self.ca2) / 2 >= 60:
            self.grade = "B"
            
        elif (self.ca1 + self.ca2) / 2 >= 40:
            self.grade = "C"
            
        else:
            self.grade = "F"
            
        self.print_student()
            
    def get_grade(self):
        return self.grade
    

# Question 2

class PrintCard:
    def __init__(self, account_number, password, credits):
        self.account_number = account_number
        self.password = password
        self.credits = credits
        
    def print(self):
        print("Account number: ", self.account_number)
        print("Password: ", self.password)
        print("Credits: ", self.credits)
        
    def add_bonus(self):
        self.credits += 400
        
    def get_credits(self):
        return self.credits
        


student = Student(
    "X123456", 
    "John Smith", 
    "Software Development", 
    77, 
    80
)

student.print_student()
student.set_grade()
student.print_student()

print("*" * 20)

card = PrintCard(
    236589,
    "Txy54",
    100
)

card.print()

print("*" * 20)

def calcBonus(StudentInstance, PrintCardInstance):
    StudentInstance.set_grade()
    
    grade = StudentInstance.get_grade()
    
    if grade in ["A", "B"]:
        PrintCardInstance.add_bonus()
        
    PrintCardInstance.print()
        
calcBonus(
    student,
    card
)