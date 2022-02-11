# X00189661 Grzegorz Maniak

# ABC Ltd. employees 4 salespeople, each of which have a weekly sales target to meet, (assume for
# version 1 there is just a single weekly target figure which all salesmen try to reach), the weekly
# target figure should be input by the user.
#
# All the salespeople attempt to meet this target, by entering daily sales figures, that is, for each
# salesperson five daily figures are entered during a week, i.e. you have to create a 2D list with 4 rows
# and 5 columns in each row.
#
# The program calculates the weekly sales figure from the daily figures entered for each salesperson
# and output that weekly figure for each salesperson. In addition, the program outputs any
# salesperson’s number who exceeded the weekly target and the amount by which they exceeded that
# target.

# At the end of the run the program outputs the total sales for the week and the number of
# salespersons who exceeded the target figure.

def version1():
    
    EMPLOYEES = 4
    WORK_DAYS = 5
    WEEKS = 1

    totalSales = []
    weeklyTargets = []


    for week in range(WEEKS):
        totalSales.append([])
        
        weeklyTarget = float(input("Enter the weekly target for week [{0}]: ".format(week + 1)))
        
        weeklyTargets.append(weeklyTarget)
        

    for employeeIndex in range(EMPLOYEES):
        
        print("------------[Employee {0}]------------".format(employeeIndex + 1))
        
        for week in range(WEEKS):
            print("")
            print("Week [{0}]".format(week + 1))
            employeeSales = []
        
            for workIndex in range(WORK_DAYS):
                salesInput = float(input("Enter sales for employee [{0}] day [{1}] week [{2}]: ".format(employeeIndex + 1, workIndex + 1, week + 1)))
                employeeSales.append(salesInput)

            totalSales[week].append(employeeSales)


    for week in range(WEEKS):
        print("")
        print("------------[Week {0}]------------".format(week + 1))
        
        totalWeeklySales = 0.0
        exceededTarget = []

        for employeeIndex in range(EMPLOYEES):
            employeeSales = sum(totalSales[week][employeeIndex])

            print("")
            totalWeeklySales += employeeSales
            exceededTarget.append(employeeIndex)

            print("Employee [{0}] sales: {1}$".format(employeeIndex + 1, employeeSales))
            
            if employeeSales >= weeklyTargets[week]:
                print("Employee [{0}] exceeded weekly target by {1}$".format(employeeIndex + 1, employeeSales - weeklyTargets[week]))
            
            else:
                print("Employee [{0}] did not exceed weekly target by {1}$".format(employeeIndex + 1, weeklyTargets[week] - employeeSales))
            
        print("")
        print("The total sales for week [{0}] is {1}$".format(week + 1, totalWeeklySales))
        print("{0} salespersons exceeded the weekly target".format(len(exceededTarget)))

def version2():
    
    EMPLOYEES = 4
    WORK_DAYS = 5
    WEEKS = 2

    totalSales = []
    
    for week in range(WEEKS):
        totalSales.append([])

    for employeeIndex in range(EMPLOYEES):
        
        print("------------[Employee {0}]------------".format(employeeIndex + 1))
        
        for week in range(WEEKS):
            print("")
            print("Week [{0}]".format(week + 1))
            weeklyTarget = float(input("Enter the weekly target for week [{0}]: ".format(week + 1)))

            employeeSales = []
        
            for workIndex in range(WORK_DAYS):
                salesInput = float(input("Enter sales for employee [{0}] day [{1}] week [{2}]: ".format(employeeIndex + 1, workIndex + 1, week + 1)))
                employeeSales.append(salesInput)

            totalSales[week].append([employeeSales, weeklyTarget])


    for week in range(WEEKS):
        print("")
        print("------------[Week {0}]------------".format(week + 1))
        
        totalWeeklySales = 0.0
        exceededTarget = []
        
        for employeeIndex in range(EMPLOYEES):
            employeeSales = sum(totalSales[week][employeeIndex][0])
            emploteeTarget = totalSales[week][employeeIndex][1]
            
            print("")
            totalWeeklySales += employeeSales
            
            print("Employee [{0}] sales: {1}$".format(employeeIndex + 1, employeeSales))
            
            if employeeSales >= emploteeTarget:
                print("Employee [{0}] exceeded weekly target by {1}$".format(employeeIndex + 1, employeeSales - emploteeTarget))
                exceededTarget.append(employeeIndex)
            
            else:
                print("Employee [{0}] did not exceed weekly target by {1}$".format(employeeIndex + 1, emploteeTarget - employeeSales))
            
        print("")
        print("The total sales for week [{0}] is {1}$".format(week + 1, totalWeeklySales))
        print("{0} salespersons exceeded the weekly target".format(len(exceededTarget)))
        
version2()