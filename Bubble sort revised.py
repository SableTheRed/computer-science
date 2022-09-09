import random
import time



x = int(input("How many numbers would you like to sort?"))
mylist = []
for i in range(0,x):
    mylist.append(random.randint(1,100))


start_time = time.time()

position = 0
swapmade = True
print(mylist)
while swapmade == True:
    swapmade = False
    position = 0
    for position in range(0,len(mylist) -  1):
        if mylist[position] > mylist[position + 1]:
            #swap items
            temp = mylist[position]
            mylist[position] = mylist[position + 1]
            mylist[position + 1] = temp
            swapmade = True
        print(mylist,"\n")

        
print("this is how long the sort took to complete: ")
print("--- %s seconds ---" % (time.time() - start_time))
