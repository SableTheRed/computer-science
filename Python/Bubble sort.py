#bubble sort
mylist = [1,2,5,9,21,3,6]
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
print("""

Sort is...




COMPLETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
