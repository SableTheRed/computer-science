
# computer shop project

#by Isobel Ryder,completed 03/09/2022

#import libraries
import sys, random, csv, time
from datetime import date, datetime

#create class for components in build
class component:
    def __init__(self, name, price, stock,daysales):
        self.n = name
        self.p = price
        self.s = stock
        self.sales = daysales

#declare each component with price and number in stock
p3 = component("P3 processor",100,10,0)
p5 = component("P5 processor",120,20,0)
p7 = component("P7 processor",200,20,0)

gb16 = component("16GB RAM",75,20,0)
gb32 = component("32GB RAM",150,20,0)

tb1 = component("1TB storage",50,20,0)
tb2 = component("2TB storage",100,20,0)

inches19 = component('19" screen',65,20,0)
inches23 = component('23" screen',120,20,0)

minitower = component("Mini Tower case",40,20,0)
miditower = component("Midi Tower case",70,20,0)

ports2 = component("2 USB Ports",10,20,0)
ports4 = component("4 USB Ports",20,20,0)


#main program
print("\nCOMPUTER SHOP PRICE ESTIMATION PROGRAM\n")

#lists for each component group
processors = [p3,p5,p7]
ram = [gb16,gb32]
storage = [tb1,tb2]
screen = [inches19,inches23]
case = [minitower,miditower]
usbports = [ports2,ports4]

global buildParts
buildParts = [processors,ram,storage,screen,case,usbports]

#procedure to place an order
def placeOrder(buildParts):
    count = 0
    chosen = []
    runningprice = float(0)
    print("The total cost of your build will be the price of the parts plus 20% labour cost for assembly")
    for item in buildParts:
        rightchoice = False
        for i in item:
            time.sleep(0.5)
            #display cost of each part in every category
            if i.s > 0:
                outpt = i.n + " will cost £" + str(i.p)
            else:
                outpt = i.n + " is out of stock."
            print(outpt)
        time.sleep(1)
        #have user select a part to use in their pc
        while rightchoice == False:
            temp = 0
            #have user select a part, or opt not to include it
            print("\nPlease select which item you would like for your pc build.")
            time.sleep(0.5)
            if count == 0:
                choice = input('Type "1" for the first displayed option, "2" for the second, or "3" for the third displayed option.\nOtherwise type "NULL" to build without: ')
            else:
                choice = input('Type "1" for the first displayed option, or "2" for the second displayed option.\nOtherwise type "NULL" to build without: ')
            try:
                if choice.upper() == "NULL":
                    choicepart = "not to include this in your order"
                else:
                    choicepart = item[int(choice)-1].n
                    temp = item[int(choice)-1].p
            except ValueError:
                choice = "NULL"
                choicepart = "not to include this in your order"
            #confirm user's choice
            try:
                if item[int(choice)-1].s > 0:
                    time.sleep(0.2)
                    print("You have chosen",choicepart,"\nIs that correct?")
                    rc = input('Please type "yes" to confirm.\n')
                else:
                    print("Sorry, this item is out of stock.")
                    rc = "OutOfStock"
            except ValueError:
                time.sleep(0.2)
                print("You have chosen",choicepart,"\nIs that correct?")
                rc = input('Please type "yes" to confirm.\n')
            #confirm order
            if rc.lower() == "yes":
                rightchoice = True
                print("This item has been added to your order.\n")
                #adjust order, order price, and stock levels accordingly
                runningprice = runningprice + temp
                if choice.upper()!="NULL":
                    chosen.append(item[int(choice)-1])
                    item[int(choice)-1].s = item[int(choice)-1].s - 1
                    item[int(choice)-1].sales = item[int(choice)-1].sales + 1
                    

                
        time.sleep(1)
        print("Items in your build so far:")
        for item in chosen:
            time.sleep(0.75)
            print(item.n)
        time.sleep(1)
        print("This will currently cost you:",runningprice*1.2)
        count = count + 1
        time.sleep(1)
        input("Press [Enter] to continue:")
        print()
    return chosen, runningprice*1.2 
    time.sleep(0.25)



              
x=1
orders = []
newno = 0
newarr = []
while x==1:
    Order = []
    print("Welcome to the computer build price calculator.")
    
    ff = input("Please press [Enter] to start your order, or type 'Finish' to end day:\n")
    if ff.upper() == "FINISH":
        x=0
    else:
        Name = input("What is the customer's name? ")
        Order = placeOrder(buildParts)
        #Order = [[p3,gb32],500.0] #this line was for testing later features without having to complete the entire order process.
        print("Order complete")
        
        time.sleep(1)
        print("You have ordered:")
        for item in Order[0]:
            time.sleep(0.5)
            print(item.n)
        time.sleep(1)
        print("Price: £"+Order[1])
        print()
        time.sleep(1)
        newarr.append([Name, "Order "+str(date.today().day)+ str(date.today().month)+"000"+str(newno), Order[0], Order[1], datetime.now()])

        print(newarr[-1][1], "placed for",Name,"confirmed on", newarr[-1][4])
        
        input()
        
        for count in range(0,30):
            time.sleep(0.02)
            print("\n")
        newno = newno + 1

print("End of day summary:\n")
tvalue = 0
for item in newarr:
    tvalue = tvalue + item[3]
time.sleep(.5)
print("There were",newno,"orders placed today at a total value of £"+tvalue)
print()
time.sleep(2)
print("Sales by component:")
for item in buildParts:
    for i in item:
        print(i.sales,"x",i.n)
time.sleep(2)
print()

print("Price by orders:")
for item in newarr:
    print(item[1],"was placed for £"+item[3])
time.sleep(6)
print("Closing program.")
input()


        
