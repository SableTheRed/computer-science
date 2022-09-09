#list
inventory = ["sword", "shield", "armour", "healing potion", "happy meal"]
print(inventory,'\n')

#selecting individual items
print(inventory[3],'\n')

#negative index
print(inventory[-1],'\n')

#concantation
itemdrop = ["spear", "bow", "arrow", "arrow", "arrow", "arrow", "arrow"]
bothlists = inventory + itemdrop
print(inventory)
print(itemdrop)
print(bothlists,'\n')

#multiplication
itemdrop = ["spear", "arrow"]
print(itemdrop * 3)
print(itemdrop[1] * 3,'\n')

#slicing
itemdrop = ["spear",  "bow", "metal ingot", "arrow", "arrow", "arrow", "arrow"]

print(itemdrop)
print(itemdrop[2:5])
print(itemdrop[:4])
print(itemdrop[5:],'\n')

#editing data
print(inventory)
inventory[4] = "cooked meat"
print(inventory,'\n')

#lists of lists
Spawn0 = ["raw fish", "hide"]
Spawn1 = ["raw meat", "raw prime meat"]
Spawn2 = ["wood", "thatch"]
Spawn3 = ["waterskin", "bola"]
Spawn4 = ["happy meal", "KFC"]
Spawnlist = [Spawn0,Spawn1,Spawn2,Spawn3,Spawn4]

print(Spawnlist)
print(Spawnlist[4])
print(Spawnlist[4][0],'\n')

#append
print("you are carrying:")
for item in inventory:
    print(item)
choice = input("\nWould you like a cabbage???     [Y/N]\n")
if choice == "Y":
    inventory.append("cabbage")
    print("\nYou have acquired a cabbage!\n")
else:
    print("\nnothing happens...\n")
print("you are carrying:")
for item in inventory:
    print(item)
print()

#insert
print("You encounter a bag")
print("you pick up the bag...")
print("It contains a sandwich!")
inventory.insert(3,"sandwich")

print()

print("you are carrying:")
for item in inventory:
    print(item)
print()

#sort    
print()

inventory.sort()

print()

print("you are carrying:")
for item in inventory:
    print(item)

#count
count = input("what item would you like to count? [all lower case please]")
print("you are carrying",inventory.count(count),count)

#extend
print("you are carrying:")
for item in inventory:
    print(item)
print()

print("you are also carrying:")
for item in Spawn4:
    print(item)
print()

inventory.extend(Spawn4)

print("you are now carrying:")
for item in inventory:
    print(item)
print()

#pop
thing = inventory.pop()
print("you are carrying:")
for item in inventory:
    print(item)
print()
print(thing)

