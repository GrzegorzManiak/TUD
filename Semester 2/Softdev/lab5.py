# X00189661 Grzegorz Maniak

# Write a program that reads, for each of 3 students, 4 test results from the user, i.e. a 2D list with 3 rows and
# each row has 4 columns: marks are in the range 0 through 100, and print the following statistics to two decimal
# places: Validate the marks, so that a number outside the 0..100 range is not accepted, loop until a valid mark is
# entered.

students = []

for student in range(3):
    print("--------------------------")
    
    test_results = []
    
    for test in range(4):
        valid = False
        
        print("------------")

        while valid == False:

            test_result = float(input("[Student: {0}] Test result [{1}]: ".format(student + 1, test + 1)))
        
            if test_result < 0 or test_result > 100:
                print("Invalid test result [{0}]".format(test_result))
            
            else:
                test_results.append(test_result)
                valid = True 
                
        print("------------")
        
    students.append([test_results])
    
# Calculate the overall average of all the results and print it. Note you cannot use mean() on a 2D list, only on a 1D
# list. You may calculate this manually by adding the sum of each row and dividing the total by the number of
# items in the 2D list

for student in range(len(students)):
    student = students[student]
    
    total = 0
    lenght = len(student[0])
    
    for value in range(lenght):
        total += student[0][value]
        
    average = total / lenght
    
    student.append(average)

# For each of the 3 students print:
# Their average and the difference between the overall average mark and their average mark (this can be either
# positive or negative).
# Print an appropriate message congratulating them if their average is equal to or above the overall
# average or telling them their average is below the overall average.
# Count the number of students whose average is equal to or greater than the overall average. Print the number
# of students whose average score equals or exceeds the overall average.
overall_avg = 0
total = 0

for student in range(len(students)):
    total += len(students[student][0])
    overall_avg += students[student][1]
    
overall_avg = overall_avg / total
total_over_avg = 0

for student in range(len(students)):
    print("------")
    print("The average of student {0} is {1}".format(student + 1, students[student][1]))
    
    avg_dif = students[student][1] - overall_avg
    print("The difference between the overall average mark and their average mark is {0}".format(round(avg_dif, 2)))
    
    if students[student][1] >= overall_avg:
        print("Congratulations! Your average is equal to or above the overall average.")
        total_over_avg += 1
    
    else:
        print("Your average is below the overall average.")
        
print("--------------------------")

if total_over_avg > 0:
    print("There are {0} students whose average is equal to or above the overall average.".format(total_over_avg))
    
else:
    print("There are no students whose average is equal to or above the overall average.")
    
# Create a 1D list to store the 3 students’ total marks (i.e. the sum of the 4 tests’ marks for each student, i.e. the
# sum of each row).

total_marks = []

for student in range(len(students)):
    total_marks.append(students[student][1])
    
# Print the lowest total mark from the above 1D list and the student who scored that mark, i.e. the 1st or 2nd or
# 3rd student etc.
# Sort the 1D totals list (use sort() or sorted())and print out the sorted list

total_marks = sorted(total_marks)

for student in range(len(total_marks)):
    print("------")
    remark = "th"
    
    if student == 0:
        remark = "st"
        
    elif student == 1:
        remark = "nd"
        
    elif student == 2:
        remark = "rd"
    
    print("The {0}{1} place student has the a total mark of {2}".format(student + 1, remark, total_marks[student]))