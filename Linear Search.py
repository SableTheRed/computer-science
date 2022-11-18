Mylist = ["cat","dog","mouse","cheese","fish"]

def linearSearch(aList, sought):
    index = -1
    found = False
    for i in range(0, len(aList)):
        index += 1
        print("iterated")
        if aList[index] == sought:
            found = True
            return index
    if found == False:
        return -999

index = linearSearch(Mylist, "fish")
if index == -999:
    print("Item not found")
else:
    print(f"Item found at index {index}")
