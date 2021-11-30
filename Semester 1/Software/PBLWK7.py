residence_name = input("Enter the name of your residence: ")

total_sleep = 0
good_sleep = 0

for i in range(5):
    sleep = int(input("Enter the number of hours you slept last night: "))
    
    if sleep >= 0:
        good_sleep += 1 
        total_sleep += sleep
        
    else:
        print("Your sleep will not be counted in the avg.")
      
avg_Sleep = total_sleep / good_sleep  
print('The avg ammount of sleep is: ', avg_Sleep)