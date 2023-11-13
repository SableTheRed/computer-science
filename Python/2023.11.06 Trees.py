

class TreeChild():
    def __init__(self, data):
        self.data = data
        self.leftchild = "NULL"
        self.rightchild = "NULL"

    def traverse(self):
        if self.leftchild != "NULL":
            self.leftchild.traverse()
        if self.rightchild != "NULL":
            self.rightchild.traverse()
        print(self.data)

    def newchild(self, value):
        if value < self.data:
            if self.leftchild == "NULL":
                self.leftchild = TreeChild(value)
            else:
                self.leftchild.newchild(value)
        else:
            if self.rightchild == "NULL":
                self.rightchild = TreeChild(value)
            else:
                self.rightchild.newchild(value)
                




Root = TreeChild(10)
Root.newchild(5)
Root.newchild(15)
Root.newchild(2)
Root.newchild(7)

Root.traverse()


