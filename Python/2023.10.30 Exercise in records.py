"""
30 Minutes:

Create a record type for a customer with the following attributes:
    ID number
    First name
    Surname
    Age
    Gender
    Product
    Price

Now, develop the program so that the user (salesman) can choose
to either enter a new sale record or view sales (menu system)

If they choose to add a record the program must ask the salesman
for each attribute


"""

from collections import namedtuple

# setup:
customers = namedtuple("customer", "ID forename surname age gender product price")
sales = []

# new sale:
def new():
    global sales
    ID = len(sales)
    fore = input("Forename: ")
    sur = input("Surname: ")
    age = input("Age: ")
    gender = input("Gender: ")
    product = input("Product: ")
    price = input("Price: ")
    new = customers(ID, fore, sur, age, gender, product, price)
    sales.append(new)
    menu()

# view sales:
def allSales():
    global sales
    for record in sales:
        print(record)
    menu()

# menu:
def menu():
    choice = int(input("""
    1. New Sale
    2. View Sales
    3. Quit
    """))
    if choice == 1:
        new()
    elif choice == 2:
        allSales()
    else:
        return

# main:
print("Sales Program \n\n")
menu()

