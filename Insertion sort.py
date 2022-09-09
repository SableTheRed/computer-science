### INSERTION SORT PSEUDOCODE ###

### CREATE A RANDOM LIST TO SORT ###
import random

# declare an empty list for the unsorted list #
unsortedList = []

# add 10 random numbers between 1 and 100 to the list #
for number in range(1,10):
    unsortedList.append(random.randint(1,100))

# print the unsorted list #
print(unsortedList)

### declaring the unsorted list #
##unsortedList = [6,3,5,4,7,1,9,16,12,21,13,8]
##print(unsortedList)

# declaring an empty list for the sorted list #
sortedList = []

# adding the first card from unsorted to sorted list #
sortedList.append(unsortedList[0])

# removing card from unsorted list #
del(unsortedList[0])



## MAIN LOOP BEGINS HERE ##

position = 0
# keep going while there are cards in the unsorted list #
while unsortedList != []:
    sortedList.append(unsortedList[0])
    del(unsortedList[0])
# start at the end of the sorted list
    position = len(sortedList) - 1
# start swapping the cards
    while sortedList[position] < sortedList[position - 1]:
        temp = sortedList[position]
        sortedList[position] = sortedList[position - 1]
        sortedList[position - 1] = temp
        position = position - 1
        if position == 0:
            break
# check that it's worked
print(sortedList)
