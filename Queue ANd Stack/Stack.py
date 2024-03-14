
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class StackLinkedList:
    """This is the stack mechanism which works on LIFO and uses piles of plates example"""
    def __init__(self):
        self.head=None
        self.count=0
    def push(self,data):
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
        else:
            next=self.head
            new_node=Node(data,next)
            self.head=new_node
        self.count+=1
    def pop(self):
        if self.head==None:
            print("Stack is empty")
            return
        else:
            temp=self.head
            # print(temp.data)
            self.head=temp.next
        self.count-=1
        return temp.data
    def is_empty(self):
        if self.head==None:
            # print("Your Stack is empty")
            return True
        return False
    def peek(self):
        if self.head==None:
            print("your Sack is empty!")
            return
        else:
            return self.head.data
    def search(self,data):
        temp=self.head
        position=1
        while temp:
            if temp.data==data:
                print(f"YOur Data is at Position {position} in the StacK!")
                return
        print(f"No such Data {data} Exist in the Stack")

    def show(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def size(self):
        print(self.count)

# s=StackLinkedList()
# s.push(1)
# s.push(2)
# s.push(3)
# s.size()
# s.search(3)
# s.pop()
# s.peek()
# s.pop()
# s.pop()
# s.show()
def reverse_data(str1):
    s=StackLinkedList()
    d = ""
    l=0
    j=0
    for i in range(len(str1)):
        if str1[i]==" ":
            for i1 in range(i-(j+1)):
                j+=1
                l-=1
                d+=f"{s.pop()}"
            d += " "
            continue
        l+=1
        s.push(str1[i])
    for i in range(l):
        d += f"{s.pop()}"
    print(f"Before Reversing: {str1}")
    print("After Reversing",end=": ")
    print(d)
reverse_data("Algorithm hAMMAd FArooq")

def main(str):
    ""'THis method will detect a string if haing correct paranthesis order or not!'
    s=StackLinkedList()
    l=len(str)
    d=["{","[","("]
    d1=["}",')',']']
    for i in range(l):
        if str[i] in d:
            s.push(str[i])
        com=s.peek()
        if com=="(":
            com=")"
        elif com=="{":
            com="}"
        elif com=="[":
            com="]"
        if com==str[i]:
            s.pop()
        elif str[i] in d1:#THis is the boundery check
            print("Not COrrect Order!")
            return
    if s.is_empty():
        print("COrrect Order!")
    else:
        print("Not COrrect Order!")
#main("{(123)+(123)+[1223](1)2]}")
# main("")

