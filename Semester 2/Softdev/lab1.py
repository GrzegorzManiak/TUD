#EX 1
def ex1():
    distances = []
    for i in range(5):
        distances.append(int(input("Enter distance for day in Km " + str(i+1) + ": ")))

    total = 0
    for i in distances:
        total += i
    average = total/5

    print("Total distance travelled: " + str(total) + "km")
    print("Average distance travelled: " + str(average) + "km")
    print("Longest distance travelled: " + str(max(distances)) + "km")
    print("Shortest distance travelled: " + str(min(distances)) + "km")
    
    
#EX 2
def ex2():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Enter number " + str(i+1) + ": ")))

    for i in range(len(numbers)):
        numbers[i] += 1

    print(numbers)
    
    
#EX 3
def ex3():
    sales = []
    
    people_input = int(input("Enter number of salespeople: "))
    
    for i in range(people_input):
        sales_input = int(input("Enter sales for employee (" + str(i+1) + ") in euros: "))
        
        sales.append(sales_input)
    
    print("Sales person          Sales")
    print("---------------------------")
    
    for people in sales:
        print("Sales person " + str(sales.index(people)+1) + ": " + str(people) + " euros")
    
    print("----------Summary----------")
    print("Total sales      : " + str(sum(sales)))
    print("Average sales    : " + str(sum(sales)/len(sales)))
    print("Maximum sales    : " + str(max(sales)))
    print("Minimum sales    : " + str(min(sales)))
    