## Q1 ## 
import time

userInput = input('Q1: DoB in format dd/mm/YYYY > ').split('/')
currentYear = time.gmtime().tm_year
age = currentYear - int(userInput[2])

print('Q1: ', age)

print('---------------------')
## Q2 ## 

# I know all your imports should go to the top of your page
import math

userInput = float(input('Q2: Circle radius > '))

if userInput < 0:
    print('Number cant be negative')
    exit()
    
radius = math.pi * (userInput ** 2)

print('Q2: ', radius)

print('---------------------')
## Q3 ##

userInput = input('Q3: Full name (John Doe) > ')

splitName = userInput.split()
firstName = splitName[0].upper()
lastName = splitName[1].upper()

print(f'Q3: {userInput} {firstName[0]}, {lastName[0]}')

print('---------------------')
## Q4 ## 

import random

loopFor = random.randint(1, 5)

totalProduct = 1
totalSum = 0

i = 0
while i < loopFor:
    randInt = random.randint(1, loopFor)
    
    totalProduct *= randInt
    totalSum += randInt
    
    i += 1
    
print(f'Q4: The random number is {loopFor}')
print(f'Q4: sum of the numbers from 1 to {loopFor} is {totalSum}')
print(f'Q4: product of the numbers from 1 to {loopFor} is {totalProduct}')

print('---------------------')
## Q5 ##

i = 0
while i < 20:
    if i % 2 == 0:
        print(f'Q5: {i} is odd')
        
    else:
        print(f'Q5: {i} is even')
    i += 1