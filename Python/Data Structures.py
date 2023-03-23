from collections import namedtuple

customer = namedtuple("customer", "ID forename surname age gender product price")


Entries = []
runningID = 0
def createRecord():
    global runningID
    print("Cerating new record:")
    forename = input("Forename: ")
    surname = input("Surname: ")
    age = input("Age: ")
    gender = input("Gender(M/F): ")
    product = input("Product: ")
    price = input("Price: ")

    Entries.append(customer(runningID, forename, surname, age, gender, product, price))

    runningID += 1

def searchRecord():
    searchby = ""
    searchby = input("What will you search by?\n ID/forename/surname/age/gender/product/price: ")
    possibles = ["ID", "forename", "surname", "age", "gender", "product", "price"]
    



    pass

def viewAll():
    global Entries
    for i in Entries:
        print(i)
    print("No more records found.")




def menu():
    print ("""
    Please select an option:
    1 - Create a record
    2 - Search for a record
    3 - View all records
    4 - Exit
    """)
    choice = input()
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        input("OK. Now leaving program.\n")
        quit()