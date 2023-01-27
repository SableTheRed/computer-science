## class LinkedList:
##     def __init__(self):
##         self.head = None
## 
## 
## class Node:
##     def __init__(self, data):
##         self.data = data
##         self.next = None






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LList:
    def __init(self):
        self.head = None

    def __repr__(self):
        node = self.head #None
        nodes = [] #container for all its nodes
        while node is not None: #you declare a node outside to meet this
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
     
llist = LList()
first_node = Node("a")
llist.head = first_node

node2 = Node("B")
first_node.next

        

    





