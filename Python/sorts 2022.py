
aList = [1,5,8,2,6,9,4,8,1,5,7,9,4,6,2,0]

def bubble(aList):
    swapped = True
    while swapped == True:
        swapped = False
        for pointer in range(0,len(aList)-1):
            if aList[pointer] > aList[pointer+1]:
                temp = aList[pointer]
                aList[pointer] = aList[pointer+1]
                aList[pointer+1] = temp
                swapped = True
                print("Swap made.")
        print("Iteration made.")
    return aList

def insertion(aList):
    for i in range(1,len(aList)-1):
        pos = i
        while aList[pos] > aList[pos - 1]:
            aList[pos], aList[pos-1] = aList[pos-1], aList[pos]
            print("Switched")
        print("moving on")
    return aList



print(aList)
print(bubble(aList))
print(insertion(aList))