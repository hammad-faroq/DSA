class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __del__(self):
        return
class QueueLinkedList:
    """THis Class will Implement the Queue FUnctionality using linkned list methodology"""
    def __init__(self,max_size):
        self.head=None
        self.tail=None
        self.max_size=max_size
        self.count=0
    def enqueue(self,data):
        self.count += 1
        if self.count>self.max_size:
            print("YOur Queue is of mazsix")
            return
        if self.head==None:
            new_node=Node(data)
            self.head=new_node
            self.tail=new_node
        else:
            new_node=Node(data)
            temp=self.head
            while temp.next:
                temp=temp.next
            self.tail=temp
            temp2=self.head
            new_node.next=temp2
            self.head=new_node
            temp3=self.head
            # print(self.head.data)
            # print(self.tail.data)
            # self.tail.next=temp3
            self.tail.next=None
            self.tail.next=self.head
    def dequeue(self):
        if self.head==None:
            print("Your Queue is EMpty!")
            return
        elif self.head.next==None:
            temp=self.head
            print(temp.data)
            del temp
            self.head=None
            self.tail=None
            self.count -= 1
            return
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp2=temp.next
            temp.next=None
            self.count -= 1
            print(temp2.data)
            del temp2
    def show(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def is_empty(self):
        if self.head==None:
            return True
        return False
    def remove(self,element):
        """This method will remove any node from the Queue having duplicates"""
        pre=None
        temp=self.head
        while temp:
            if element == self.head.data:
                temp = self.head
                self.head = temp.next
                pre = None
                temp = self.head
            elif temp.data==element:
                temp2=temp.next
                pre.next=temp2
                temp=temp.next
                continue
            pre=temp
            temp=temp.next

    def rotate(self,upto):
        """THis method will rotate the Queue upto the given index"""
        if self.count==upto or upto>self.count:
            return
        temp=self.head
        for i in range(self.count-upto-1):
            temp=temp.next
        temp2=temp.next#4
        temp.next=None
        temp3=self.head#1
        self.head=temp2
        while temp2.next:
            temp2=temp2.next
        temp2.next=temp3
    def size(self):
        print(self.count)
    def front(self):
        if not self.is_empty():
            print(self.tail.data)
    def back(self):
        if not self.is_empty():
            print(self.head.data)

q=QueueLinkedList(5)
q.enqueue("Haseeb")
q.enqueue("HAroon")
q.enqueue("Haris")
q.enqueue("Hammad")
q.enqueue("HAHA")
q.show()
# print()
# q.front()
# print(q.tail.data.next)
# print(q.head.data)
# q.back()
# # q.enqueue(7)
# q.enqueue(2)
# q.enqueue(6)
# q.enqueue(5)
# q.enqueue(4)
# q.enqueue(3)
# q.enqueue(1)
# # q.enqueue(2)
# # q.enqueue(2)
# q.enqueue(2)
# q.enqueue(2)
# q.enqueue(1)
# q.enqueue(1)
# q.enqueue(1)
# q.show()
# print()
# q.remove(2)
# q.show()
# print()
# q.remove(1)
# q.show()
# # print()
# # q.rotate(1)
# # q.show()
# # q.front()
# # q.back()
