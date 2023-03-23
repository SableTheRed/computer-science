## An exercise to understand stacks

#smaller pieces take priority
#desired stack is closest to empty (smallest valid piece on top)


class Hanoi_solver:

    def __init__(self,pieces):
        self.pieces = pieces
        self.towers = []
        for i in range(3):
            self.towers.append(Stack)
        pass


class Stack():

    def __init__(self):
        self.discs = []
        self.top = -1
        print("Instantiated")

    def __repr__(self):
        
        return " | " .join(str(self.discs).replace(" ","").replace(",",""))

    def startingwith(self,x):
        for i in range(1,x+1):
            self.discs.append(i)
        self.top += x

    def push(self,size):
        try:
            if size > self.discs[self.top]:
                return False
            else:
                self.discs.append(size)
                self.top += 1
                return True
        except IndexError:
            self.discs.append(size)
            self.top += 1
            return True

    def pop(self, new):
        Valid = False
        if self.top < 0:
            print("Nah it's empty bro")
        else:
            Valid = new.push(self.discs[self.top])
        if Valid == True:
            self.discs.pop(self.top)
            self.top += -1
        







Tower_1 = Stack()
Tower_1.startingwith(5)

Tower_2 = Stack()

for i in range(5):
    Tower_1.pop(Tower_2)
    print(f"\nFirst tower: {Tower_1}\nSecond Tower: {Tower_2}\n\n")


