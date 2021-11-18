#######################
##  GRZEGORZ MANIAK  ##
##  X00189661        ##
##  CA2 18/11/2021   ##
#######################

#members name
#in = user id, first character is g
#eg G215873X max lenght

#in = year of birth
CURRENT_YEAR = 2021
MEMBER_FEE = 2000.0

DISCOUNT_70 = 0.50
discountsGiven50 = 0

DISCOUNT_50_70 = 0.25
discountsGiven25 = 0

DISCOUNT_50 = 0.00
discountsGiven0 = 0


#NAME
userName = input('Member Name:  ')

#ID
userInput = input('Member ID:  ').lower()

count = 0
error = ''
passed = True

for chars in userInput:
    if count == 0 and userInput[count] != 'g':
        error += 'Invalid ID, First character must be "G" \n'
        passed = False
        
    if count > 0 and count < 7 and userInput[count].isdigit() == False:
        error += f'Character {count + 1} => "{userInput[count]}" Is not a digit \n'
        passed = False
        
    if count > 7:
        error += 'Id is too long'
        passed = False
            
    count += 1
    
if count < 8:
    error += 'Id is too short'
    passed = False

if passed == False:
    print(error)
    exit()

print(f'!!!Processing Discount:!!!')

#AGE
birthYear = input('Year born: ')
if birthYear.isdigit() == False:
    print('Invalid Birth Year')
    exit()

birthYear = int(birthYear)
age = CURRENT_YEAR - birthYear

#DISCOUNTS

discount = 0.0
if age >= 70:
    discount = DISCOUNT_70
    discountsGiven50 += 1
    
elif age >= 50 and age < 70:
    discount = DISCOUNT_50_70
    discountsGiven25 += 1
    
elif age < 50:
    discount = DISCOUNT_50
    discountsGiven0 += 1
    
totalDiscount = MEMBER_FEE * discount

totalFees = MEMBER_FEE - totalDiscount

print(f'Member: {userName}')
print(f'Number: {userInput}')
print(f'Age:    {age}')
print(f'Fees Due: ${MEMBER_FEE}') #sorry, I dont have a euro symbol! Hopefully a '$' will do
print(f'Percentage Fees Discounted: {discount}%')
print(f'Amount Fees Discounted    : ${totalDiscount}')
print(f'Amount Fees to be paid    : ${totalFees}')

print('Category information')
print(f'Number of 50% discounts: {discountsGiven50}')
print(f'Number of 25% discounts: {discountsGiven25}')
print(f'Number of 0% discounts: {discountsGiven0}')