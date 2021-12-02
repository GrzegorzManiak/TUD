#EX1 VERSION 1
import math
print("""
    1. Cube
    2. Cylinder
    3. Sphere
    4. Exit
    """)
choice = int(input("Please select a shape: "))
if choice == 1:
    length = float(input("Enter the length: "))
    v = length**3
    print("The volume of the cube is " + str(v))
elif choice == 2:
    r = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    v = math.pi * r**2 * height
    print("The volume of the cylinder is " + str(v))
elif choice == 3:
    r = float(input("Enter the radius: "))
    v = (4 / 3) * math.pi * r**3
    print("The volume of the sphere is " + str(v))
elif choice == 4:
    print("Goodbye!")
else:
    print("Invalid choice")

#EX1 VERSION 2
import math
print("""
    1. Cube
    2. Cylinder
    3. Sphere
    4. Exit
    """)
choice = int(input("Please select a shape: "))
if choice == 1:
    length = float(input("Enter the length: "))
    v = length**3
    print("The volume of the cube is " + str(v))
elif choice == 2:
    while True:
        r = float(input("Enter the radius: "))
        if r > 0:
            break
        
    height = float(input("Enter the height: "))
    v = math.pi * r**2 * height
    print("The volume of the cylinder is " + str(v))
elif choice == 3:
    while True:
        r = float(input("Enter the radius: "))
        if r > 0:
            break
        
    v = (4 / 3) * math.pi * r**3
    print("The volume of the sphere is " + str(v))
elif choice == 4:
    print("Goodbye!")
else:
    print("Invalid choice")
    
#EX2
sentence = input("Enter a sentence: ")
urlsentence = ""
for i in sentence:
    if i == " ":
        urlsentence += "%20"
    else:
        urlsentence += i
print("The sentence is: " + sentence)
print("The URL sentence is: " + urlsentence)

#EX3
sentence = input("Enter a sentence: ")
character = input("Enter a character: ")
while len(character) != 1:
    character = input("Enter a character: ")
count = 0
sentence = sentence.lower()
character = character.lower()
for i in sentence:
    if i == character:
        count += 1
print("The character appears " + str(count) + " times in the sentence")
