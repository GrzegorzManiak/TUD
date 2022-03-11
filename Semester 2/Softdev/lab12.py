# X00189661 Grzegorz Maniak

def add(titles, copies, title, copies_num):
    titles.append(title)
    copies.append(copies_num)
    
def add_dvd(titles, copies):
    while True:
        title = input("Enter title of DVD: ")
        copies_num = int(input("Enter number of copies: "))
        
        if copies_num < 0:
            print("Invalid number of copies")
            continue
        
        add(titles, copies, title, copies_num)
        break

def display_stock(titles, copies):
    for i in range(len(titles)):
        print("{0} {1}".format(titles[i], copies[i]))    

def search(titles, title):
    for i in range(len(titles)):
        if titles[i] == title:
            return True 
    
    return False

def rent(titles, copies, title):
    if search(titles, title):
        for i in range(len(titles)):
            if titles[i] == title:
                if copies[i] > 0:
                    copies[i] -= 1
                    print("DVD rented")
                else:
                    print("DVD not available")
    else:
        print("DVD not found")
    
def return_dvd(titles, copies, title):
    if search(titles, title):
        for i in range(len(titles)):
            if titles[i] == title:
                copies[i] += 1
                print("DVD returned")
    else:
        print("DVD not found")

def list_no_stock(titles, copies):
    no_stock = []
    
    for i in range(len(titles)):
        if copies[i] == 0:
            no_stock.append(titles[i])
            
    return no_stock
            
def display_low_stock(titles, copies, threshold):
    low_stock = []
    
    for i in range(len(titles)):
        if copies[i] < threshold:
            low_stock.append(titles[i])
            
    return low_stock

def menu():
    dvd_titles = []
    dvd_copies = []
    
    while True:
        print("*" * 25)
        print("DVD Store".center(25))
        print("*" * 25)
        print("* 1) Add a DVD {0}*".format(" " * 9))
        print("* 2) Stock Lsit {0}*".format(" " * 8))
        print("* 3) Rent DVD {0}*".format(" " * 10))
        print("* 4) Return DVD {0}*".format(" " * 8))
        print("* 5) Search {0}*".format(" " * 12))
        print("* 6) No Stock List {0}*".format(" " * 5))
        print("* 7) Low Stock List {0}*".format(" " * 4))
        print("* 8) Exit {0}*".format(" " * 14))
        print("*" * 25)
        
        user_choice = input("Please enter option: ")
        
        if user_choice == "1":
            add_dvd(dvd_titles, dvd_copies)
            
        elif user_choice == "2":
            display_stock(dvd_titles, dvd_copies)
            
        elif user_choice == "3":
            title = input("Enter title of DVD: ")
            rent(dvd_titles, dvd_copies, title)
            
        elif user_choice == "4":
            title = input("Enter title of DVD: ")
            return_dvd(dvd_titles, dvd_copies, title)
            
        elif user_choice == "5":
            title = input("Enter title of DVD: ")
            if search(dvd_titles, title):
                print("DVD found")
            else:
                print("DVD not found")
                
        elif user_choice == "6":
            no_stock = list_no_stock(dvd_titles, dvd_copies)
            
            if len(no_stock) > 0:
                print("No stock DVD titles: ")
            
                for title in no_stock:
                    print(title)
                    
            else:
                print("Each DVD is in stock")
        
        elif user_choice == "7":
            low_stock = display_low_stock(dvd_titles, dvd_copies, 4)
            
            if len(low_stock) > 0:
                print("low stock DVD titles: ")
            
                for title in low_stock:
                    print("{0} {1} Copies".format(title, dvd_copies[dvd_titles.index(title)]))

            else:
                print("No low stock DVD titles")
                
        else:
            print("Invalid option")
    
menu()