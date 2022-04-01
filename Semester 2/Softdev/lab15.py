# X00189661 Grzegorz Maniak

class Patient:
    def __init__(self, patient_number, name, has_medical_card, is_private):
        self.patient_number = patient_number
        self.name = name
        self.has_medical_card = has_medical_card
        self.is_private = is_private
        self.length_of_stay = 0

    def set_length_of_stay(self, days):
        self.length_of_stay = days

    def get_name(self):
        return self.name
    
    def calc_bill(self):
        if self.has_medical_card == True:
            return 0.0
        
        elif self.is_private == True:
            return 300 * self.length_of_stay
        
        else:
            return 100 * self.length_of_stay
        
    def print(self):
        print("Patient Name:", self.name)
        
        if self.has_medical_card == True:
            print("Medical card y/n: Y")
        else: print("Medical card y/n: N")
            
        if self.is_private == True:
            print("Private Patient y/n: Y")
        else: print("Private Patient y/n: N")
            
        print("Length of stay:", self.length_of_stay)
        
        
p1 = Patient(78922, "Jane Austin", True, True)
p1.set_length_of_stay(10)
p1.print()
print("P1 Bill amount:", p1.calc_bill())

print()

p2 = Patient(67453, "Henry James", False, True)
p2.set_length_of_stay(5)
p2.print()
print("P2 Bill amount:", p2.calc_bill())

p2.set_length_of_stay(7)
print("P2 Bill amount after re-setting length of stay:", p2.calc_bill())

print()

name = input("Enter patient name: ")
patient_number = input("Enter patient number: ")

has_medical_card = False

while True:
    has_medical_card_input = input("Has the patient got a medical card? (Y/N): ")
    
    if has_medical_card_input.capitalize() == "Y":
        has_medical_card = True
        break
    
    elif has_medical_card_input.capitalize() == "N":
        has_medical_card = False
        break
    
    else :
        print("Invalid entry, please enter Y or N")


is_private = False

while True:
    is_private_input = input("Is the patient a private patient? (Y/N): ")
    
    if is_private_input.capitalize() == "Y":
        is_private = True
        break
    
    elif is_private_input.capitalize() == "N":
        is_private = False
        break
    
    else :
        print("Invalid entry, please enter Y or N")


p3 = Patient(patient_number, name, has_medical_card, is_private)

length_of_stay = int(input("Enter the length of stay: "))
p3.set_length_of_stay(length_of_stay)

p3.print()
print("P3 Bill amount:", p3.calc_bill())