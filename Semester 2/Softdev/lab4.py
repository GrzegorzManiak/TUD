
#X00189661

number_of_sales_men = int(input("Please input the number of sales men (positive whole number): "))

sales_names = []
kitchens_sold = []
total_sales = []
sold_for = []
total_commisions = []

for sales_index in range(number_of_sales_men):
    
    print("-------------------")
    
    sales_name = input("[{0}] Whats their name? ".format(sales_index + 1))
    sales_names.append(sales_name)
    
    total_sold = int(input("[{0}] Total kitchens sold? (positive whole number): ".format(sales_index + 1)))
    kitchens_sold.append(total_sold)
    
    temp_sold_for = []
    
    print("")
    
    for sold_index in range(total_sold):
        price_sold = int(input("--[{0}] Price of kitchen [{1}] sold? (positive whole number): ".format(sales_index + 1, sold_index + 1)))
        temp_sold_for.append(price_sold)
        
    sold_for.append(temp_sold_for)
    
    print("")
    
    total_sales_rep = sum(temp_sold_for)
    total_sales.append(total_sales_rep)
        
print("--------------------------")
print("--------------------------")
            
for sales_index in range(len(sales_names)):
    print("--------------------------")
    
    sales_name = sales_names[sales_index]
    print("Sales men name: {0}".format(sales_name))
        
    numbers_of_kitchens = kitchens_sold[sales_index]
    print("Kitchens sold: {0}".format(numbers_of_kitchens))
    
    for kitchens_index in range(numbers_of_kitchens):
        print(" -Price of kitchen [{0}] sold: {1}".format(kitchens_index + 1, sold_for[sales_index][kitchens_index]))
        
    print("")    
    
    total_sales_rep = total_sales[sales_index]
    print("Total sales for {0} is {1}".format(sales_name, total_sales_rep))

    if total_sales_rep > 50000:
        commission = total_sales_rep * 0.15
        
        print("Commission for {0} is {1} Euro".format(sales_name, commission))
        total_commisions.append(commission)
        
    else:
        print("No commission for {0}".format(sales_name))
        total_commisions.append(0)
    
print("--------------------------")
print("Name                 Sales")
            
for sales_index in range(len(sales_names)):
    sales_name = sales_names[sales_index]
    total_sold_for = total_sales[sales_index]

    print("{0}              {1}".format(sales_name, total_sales_rep))

print("--------------------------")

print("Total commisions: {0}".format(round(sum(total_commisions), 2)))

highest_earner_index = total_sales.index(max(total_sales))
print("Higest sales: {0} with a total of sales of {1}".format(sales_names[highest_earner_index], max(sold_for[highest_earner_index])))