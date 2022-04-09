import random 

# 
# Question 1
# 

class Animal:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        
    def display_details(self):
        print("Animal:")
        print("\tId: ", self.id)
        print("\tType: ", self.type)
        
class Greyhound(Animal):
    def __init__(self, name, sex, father, mother):
        self.id = random.randint(1000, 9999)
        self.type = "Greyhound"
        
        self.animal = Animal(self.id, self.type)
        
        self.name = name
        self.sex = sex
        self.father = father
        self.mother = mother
        
        self.pups = 0
        self.litters = 0
        
    def update_breeding_record(self, pups):
        self.pups += pups
        self.litters += 1
        
    def display_details(self):
        super().display_details()
        
        print("\tName: ", self.name)
        print("\tSex: ", self.sex)
        print("\tFather: ", self.father)
        print("\tMother: ", self.mother)
        print("\tLitter: ", self.litters)
        print("\tPups: ", self.pups)

GreyhoundInstance = Greyhound(
    "Mrs Flash",
    "female",
    "Tom Foley",
    "The Late Late Show",
)

GreyhoundInstance.update_breeding_record(4)
GreyhoundInstance.update_breeding_record(5)

GreyhoundInstance.display_details()

# 
# Question 2
# 

print()

class Employee:
    def __init__(self, name, number, hours, rate):
        self.name = name
        self.number = number
        self.hours = hours
        self.rate = rate
        
        if self.hours < 0:
            self.hours = 0
        if self.rate < 0:
            self.rate = 0
        
    def calculate_salary(self):
        return self.hours * self.rate
    
    def print(self):
        print("Name: ", self.name)
        print("Employee Number: ", self.number)
        print("Wages Per Hour: ", self.rate)
        print("Hours Worked this week: ", self.hours)
        print("-" * 20)
        print("Salary: ", self.calculate_salary())

        
class Trainee(Employee):
    def __init__(self, name, number, hours, rate, training_hours):
        super().__init__(name, number, hours, rate)
        self.training_hours = training_hours
        
    def calculate_salary(self):
        return super().calculate_salary() + self.training_hours * 5
    
    def print(self):
        super().print()
        print("Includes training hours: ", self.training_hours)

TraineeInstance = Trainee(
    "John Smith",
    1234,
    40,
    20,
    2,
)

TraineeInstance.print()