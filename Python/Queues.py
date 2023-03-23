class linqueue():
    def __init__(self,max):
        self.queue = []
        self.head = 0
        self.tail = -1
        self.max = max

    def __repr__(self):
        print("\nPrinting queue:")
        return ", " .join(self.queue)

    def enqueue(self,new):
        if self.tail == (self.max - 1):
            print("\nSorry, queue is full.\n")
        else:
            #new = input("What do you want to append?\n")
            print(f"\nappending {new} to queue.\n")
            self.queue.append(new)
            self.tail += 1

    def dequeue(self):
        if self.tail < self.head:
            print("\nSorry, queue is empty.\n")
        else:
            print("\nRemoving front item.")
            self.queue.pop(0)
            self.tail += -1

print("Instantiate your queue")
print("E.g. queue = linqueue(5):\n\n")

lete = linqueue(5)

print(lete)
lete.enqueue("Orange")
print(lete)

lete.enqueue("apple")
print(lete)


lete.dequeue()
print(lete)



## Supermarket??

##lete = "abcdefghi"
##
##for i in lete:
##    print(f'"{i}",')



