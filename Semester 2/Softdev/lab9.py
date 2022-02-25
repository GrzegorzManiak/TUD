# X00189661 Grzegorz Maniak

# Create a system for a Computer Supplies shop, which manages stock.
# The program should have a menu to select options, where after each option except exit, the
# program redisplays the menu.
# The menu should look similar to:

# Copy the following 2D list into your program. Copy and paste it from the product_list.txt
# file on Moodle

product_list = [
    ["CS567", "Wireless Printer", 49.99, 20.00, 8, 10],
    ["CS100", "Document Scanner", 109.99, 60.00, 11, 5],
    ["CS777", "Ink Cartridge", 29.99, 15.00, 12, 25],
    ["CS800", "Full HD Webcam", 64.00, 30.00, 12, 10],
    ["CS990", "Optical Mouse", 5.99, 2.00, 10, 5]
]

# The above 2D list stores products’ details as follows:
# Column 1: Product ID
# Column 2: Name
# Column 3: Selling price
# Column 4: Cost price
# Column 5: Quantity of the product on hand (i.e. in the shop)
# Column 6: Re-order level (a quantity which indicates that the product should be re-ordered)

choice = 0

while True:
    print("")
    print("*" * 50)
    print("Computer Supplies System")
    print("*" * 50)
    print("")
    print("1. List all products")
    print("2. List low stock products")
    print("3. Print product details")
    print("4. Total stock value")
    print("5. Exit")
    
    choice = int(input("\nEnter your choice: "))
    
    if choice > 5 or choice < 1:
        print("\nInvalid choice!")
        continue
    
    else:
        break
    
if choice == 1:
    print("\nProduct ID\tProduct Name\tSelling Price\tCost Price\tQuantity\tRe-order Level")
    print("-" * 50)
    for index in range(len(product_list)):
        print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(product_list[index][0], product_list[index][1], product_list[index][2], product_list[index][3], product_list[index][4], product_list[index][5]))
    
elif choice == 2:
    print("\nProduct ID\tProduct Name\tQuantity\tRe-order Level")
    print("-" * 50)
    for index in range(len(product_list)):
        if product_list[index][4] < product_list[index][5]:
            print("{0}\t{1}\t{2}\t{3}".format(product_list[index][0], product_list[index][1], product_list[index][4], product_list[index][5]))

elif choice == 3:
    print("\nProduct ID\tProduct Name\tSelling Price\tCost Price\Cost Price\tProfitl")
    print("-" * 50)
    for index in range(len(product_list)):
        profit = product_list[index][2] - product_list[index][3]
        print("{0}\t{1}\t{2}\t{3}\t{4:.2f}".format(product_list[index][0], product_list[index][1], product_list[index][2], product_list[index][3], profit))
        
elif choice == 4:
    print("-" * 50)
    total_stock_value = 0
    for index in range(len(product_list)):
        total_stock_value += product_list[index][2] * product_list[index][4]
    print("\nTotal stock value: ${0:.2f}".format(total_stock_value))
    print("-" * 50)