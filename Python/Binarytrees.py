class Bintree():
    def __init__(self, mylist):
        self.parentnode = Node(mylist[0])
        nodeth = self.parentnode


        for count in range(len(mylist)):
            child = Node(mylist[count])
            added = False

            while not added:

                while child.value < nodeth.value:
                    if nodeth.leftchild == None:
                        nodeth.leftchild = child
                        added = True
                    else:
                        nodeth = nodeth.leftchild

                if not added:
                    if nodeth.rightchild == None:
                        nodeth.rightchild = child
                        added = True
                    else:
                        nodeth = nodeth.rightchild

    def inOrder(self):
        node = self.parentnode
        oldlist = []
        x=True
        while x:
            query = node.leftchild
            while query != None:
                querynode = node.leftchild
                if querynode.read:
                    query = None
                else:
                    oldlist.append(node)
                    node = querynode
            query = node.rightchild
            if query != None:
                querynode = node.rightchild
                if querynode.read:
                    query = None
                else:
                    oldlist.append(node)
                    node = querynode
            print(node)
            node.read = True
            node = oldlist[-1]
            return "/n"


                
            





    def __repr__(self):
        return "A binary tree. To view nodes, please name a method of traversal."




class Node():
    def __init__(self, value):
        self.value = value
        self.read = False
        self.leftchild = None
        self.rightchild = None

    def __repr__(self):
        return str(self.value)

fruitlist = ["Apple", "Orange", "Banana", "Pear", "Kiwi", "Mango", "Peach"]

tree = Bintree(fruitlist)
tree.inOrder()