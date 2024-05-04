class BNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BST:
    def __init__(self,value):
        self.root=BNode(value)
    def insert(self,value):
        curr=self.root
        while True:
            if value<curr.value:
                if curr.left is None:
                    curr.left=BNode(value)
                    break
                curr=curr.left
            if value>=curr.value:
                if curr.right is None:
                    curr.right=BNode(value)
                    break
                curr=curr.right
    def insert_iterative(self,value,curr=None):
        if curr== None:
            curr=self.root
        if value<curr.value:
            if curr.left is None:
                curr.left = BNode(value)
                return
            else:
                self.insert_iterative(value=value, curr=curr.left)
        elif value>= curr.value:
            if curr.right is None:
                curr.right=BNode(value)
                return
            else:
                self.insert_iterative(value=value,curr=curr.right)


    def search(self,value):
        curr=self.root
        while True:
            if value==curr.value:
                print(value)
                break
            if value<curr.value:
                if curr.left is None:
                    print("Does not exist!")
                    break
                curr=curr.left
            elif value>=curr.value:
                if curr.right is None:
                    print("Does not exist!")
                    break
                curr=curr.right
    def search_iterative(self,value,curr=None):
        if curr ==None:
            curr=self.root
        if curr.value==value:
            print(value)
            return
        if value<curr.value:
            if curr.left==None:
                print("does not Exist!")
                return
            else:
                self.search_iterative(value=value,curr=curr.left)
        if value>=curr.value:
            if curr.right==None:
                print("Does not Exist!")
                return
            else:
                self.search_iterative(value=value,curr=curr.right)
    def show_right(self):
        curr = self.root
        while curr.right:
            print(curr.value, end="----->")
            curr=curr.right
        print(curr.value)
    def show_left(self):
        curr=self.root
        while curr.left:
            print(curr.value, end="----->")
            curr=curr.left
        print(curr.value)
b=BST(7)
b.insert(4)
b.insert(1)
b.insert_iterative(0)
b.insert_iterative(12)
b.insert_iterative(14)
b.insert_iterative(18)
b.insert_iterative(21)
b.insert_iterative(-2)
b.insert_iterative(171)
b.insert_iterative(-4)
b.insert_iterative(-11)
b.show_right()
b.show_left()
# b.insert_iterative(12)
b.search_iterative(-2)




