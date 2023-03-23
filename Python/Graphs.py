

# Store the Graph
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"


graph = [[A,D,12],[A,C,60],
         [B,A,10],
         [C,B,20],[C,D,32],
         [E,A,7]]

## CREATE stack
## 
## MARK startingNode as VISITED AND PUSH currentNode onto stack
## 
## WHILE stack NOT EMPTY
## 
## currentNode = topOfStack
## 
## WHILE currentNode has (unvisited) neighbour
## 
## MARK neighbourNode as VISITED AND PUSH onto stack
## 
## currentNode = topOfStack
## 
## POP topOfStack

class Stack():
    def __init__(self,max):
        self.stack = []
        self.pointer = -1
        self.max = max

    def __repr__(self):
        print("\nPrinting stack:")
        return "-> " .join(self.stack)

    def push(self,new):
        if self.pointer == (self.max - 1):
            print("\nSorry, stack is full.\n")
        else:
            #new = input("What do you want to append?\n")
            print(f"\nappending {new} to stack.\n")
            self.stack.append(new)
            self.pointer += 1

    def pop(self):
        if self.pointer < 0:
            print("\nSorry, stack is empty.\n")
        else:
            print("\nRemoving last item.")
            self.stack.pop(-1)
            self.pointer += -1

visited = []
Graph = Stack(100)
for i in graph:
    Graph.push(i)

print(Graph)
