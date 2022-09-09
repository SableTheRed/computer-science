# Binary Search
# 19/11/2020

#defining variables
L = [1,2,6,7,15,16,17,19,20,68,360]
LB = 0
UB = len(L)
Found = 'false'

#defining searched
searched = int(input("What number are you searching for?"))

#search
while Found == 'false' and LB != UB + 1:
    MP = int((LB + UB) /2)
    if L[MP] == searched:
        Found = 'true'
    elif L[MP] < searched:
        LB = MP + 1
    else:
        UB = MP - 1
    print(MP,LB,UB)
if Found == 'true':
    print("Item found at position", MP + 1)
else:
    print("Item not in list")
    

