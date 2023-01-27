class Critter(object):
    """A virtual pet"""

    total = 0
    @staticmethod
    def status():
        print(f"\nThe total number of critters is {Critter.total}")


    def __init__(self, name):
        print("A new critter has been born!")
        # attributes
        self.name = name
        self.__legs = 4
        self.__hunger = 0
        self.__boredom = 0
        Critter.total += 1
 

    #string method - special method that will be called on print
    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print(f"Hi there. I'm {self.name}\n")

    def hunger(self):
        return self.__hunger

    def __update(self):
        self.__hunger += 1
        self.__boredom += 1

    


critlist = []
names = ["Joe", "John", "Lily", "Malcolm", "Boris", "doris"]
for i in names:
    critlist.append(Critter(i))

print(critlist[1].name)
print(critlist[2].name)
Critter.status()
print(f"Hunger: {critlist[1].hunger()}")

input("\n\n press enter to exit.")