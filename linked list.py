class Node:
    """THe linked dlist is all about making the node objects and just associating the refrences to the next objects in that objects.THe last object will have a NOne
    address and the first object is called head from where the functionalities starts.
    """
    def __init__(self,data,next_object_refrence=None):
        self.data=data
        self.next_object_refrence=next_object_refrence
    def __del__(self):
        return
class Linked_list:
    def __init__(self,head=None):
        self.head=head#when we assign a object to an attribute,It will have all the attrubutes and method of the assigned object class :)
    def add_to_the_first(self,data):
        if self.head==None:#if there is not any element in the list
            node=Node(data,next_object_refrence=self.head)
            self.head=node
        else:
            node=Node(data=data,next_object_refrence=self.head)
            self.head=node
    def add_to_last(self,data):
        if self.head==None:
            node=Node(data,next_object_refrence=self.head)
            self.head=node
        else:
            #We need a loop to go to the lsat node and then add the value to it
            curr=self.head
            while curr.next_object_refrence:
                """THis loop will only runs n-1 times but will have the refrence of the nth element before termination"""
                curr=curr.next_object_refrence
            node=Node(data)
            curr.next_object_refrence=node
    def insert_before(self,val,new_val):
        curr=self.head
        if self.head==None:
            return
        if val==curr.data:##If the new value is the first node
            node = Node(data=new_val, next_object_refrence=curr)
            self.head=node#we dont need to change or manipulate the headd to often beacuse it needs to be the first value in the linked list with the refrence to the other object
            return
        while curr.next_object_refrence:
            next_node=curr.next_object_refrence
            data=next_node.data
            if data==val:#we just have to make new node objects and just change the refrences according to the functions
                node=Node(data=new_val,next_object_refrence=next_node)
                curr.next_object_refrence=node
                break
            curr=curr.next_object_refrence
    def search(self,data1):
        cur=self.head
        while cur:
            if cur.data==data1:
                print(data1)
                return
            cur=cur.next_object_refrence
        print("No such element exist in the linked List!")
    def insert_after(self,val,new_val):
        curr=self.head
        while curr:
            if curr.data==val:
                node=Node(new_val,curr.next_object_refrence)#changing the refrence
                curr.next_object_refrence=node#Updating the refrence
                return
            curr = curr.next_object_refrence
        print("No such value exist in the linked list!")
    def show(self):
        if self.head==None:
            print("YOur linked list is empty!")
        else:
            if self.head != None and self.head.next_object_refrence == None:#THis check is if the head had a value with None refrence to the next obj
                print(self.head.data)
                return
            current_node=self.head
            while current_node.next_object_refrence:#THis will stop before the last value in the linked list
                print(f"{current_node.data}-->", end="")
                current_node=current_node.next_object_refrence
            print(current_node.data)
    def remove_at_head(self):
        if self.head==None:
            return
        next=self.head.next_object_refrence
        del self.head#THis will delete the object at the head posistion ifn the linked list
        self.head=next
    def remove_at_tail(self):
        if self.head==None:
            return
        if self.head and self.head.next_object_refrence==None:#This is the special case
            del self.head
            self.head=None
            return
        pre=self.head
        curr=self.head.next_object_refrence
        while curr.next_object_refrence:
            curr=curr.next_object_refrence
            pre=pre.next_object_refrence
        del curr
        pre.next_object_refrence=None
    def remove_before(self,data):
        if self.head==None:#if first node empty
            return
        if self.head.data==data:#If we want to remove before head not possible
            return
        temp=self.head.next_object_refrence
        if self.head!=None and temp!=None and temp.next_object_refrence==None:#Special check for two elements
            self.head.next_object_refrence=temp.next_object_refrence
            del temp
            return
        curr=self.head.next_object_refrence
        pre=self.head
        while curr:#This loop will not work if there are only two elements in the linked list
            if pre.data==data:#This wll always remove before the second element
                del self.head
                self.head=pre
                return
            elif curr.next_object_refrence.data==data:
                pre.next_object_refrence =curr.next_object_refrence
                del curr
                return
            pre=pre.next_object_refrence
            curr=curr.next_object_refrence
    def remove_after(self,data):
        if self.head==None:
            return
        if self.head.data==data and self.head.next_object_refrence==None:#Can't rmove after the head if there is only head
            return
        if self.head.data==data:#This will remove afther the head of the linked list
            temp=self.head.next_object_refrence
            next=temp.next_object_refrence
            del temp
            self.head.next_object_refrence=next
            return
        curr=self.head
        temp=self.head.next_object_refrence
        while curr.next_object_refrence:
            if curr.data==data:
                next=curr.next_object_refrence
                next2=next.next_object_refrence
                curr.next_object_refrence=next2
                del next
                return
            curr = curr.next_object_refrence
            temp = temp.next_object_refrence
    def remove(self,data):
        """This will remove any node which is in the linked list """
        curr=self.head.next_object_refrence
        temp=self.head
        if self.head==None:
            return
        if self.head.data==data:#Tjis will remove the head of the linked list
            next=self.head.next_object_refrence
            del self.head
            self.head=next
            return
        while curr:
            if curr.data==data:
                next=curr.next_object_refrence
                del curr
                temp.next_object_refrence=next
                return
            temp=temp.next_object_refrence
            curr=curr.next_object_refrence
    def remove_kth_node(self,k):
        """THis method will return true if kth node has been removed else false"""
        if self.head==None or k==0:
            print("False")
            return
        if k==1 and self.head!=None:
            next=self.head.next_object_refrence
            del self.head
            self.head=next
            print("True")
            return
        i=1
        sum=0
        curr=self.head
        while curr:
            sum+=1
            curr=curr.next_object_refrence
        if k>sum:
            print("False")
            return
        temp = self.head
        curr=self.head.next_object_refrence
        if k==2:#this will remove the second element in the linked list
            curr=self.head.next_object_refrence
            next=curr.next_object_refrence
            del curr
            self.head.next_object_refrence=next
            print("True")
            return
        pre=0
        while i<k:
            i=i+1
            if k-1==i:
                pre=curr
            curr = curr.next_object_refrence
            temp=temp.next_object_refrence
        del temp
        pre.next_object_refrence=curr
        print("True")
        return
    def combine(self,l1,l2):#We need to combine the two linked lists without making any new node
        """This method will take two list and combine them into a single list"""
        if self.head==None:#If the head of the list is empty
            head=l1.head
            if l1.head!=None:#THe head of the first list also not needs to be empty
                self.head=head
            curr=self.head
            l1.head=None
            while curr.next_object_refrence:
                curr=curr.next_object_refrence
            if l2.head!=None:
                curr.next_object_refrence=l2.head
                l2.head=None
    def remove_duplication(self):
        """This method will remove the duplications"""
        curr=self.head
        while curr:
            temp=curr.next_object_refrence
            pre=curr
            while temp:
                if curr.data==temp.data:
                    next=temp.next_object_refrence
                    temp3=temp
                    del temp3
                    pre.next_object_refrence=next
                    temp = temp.next_object_refrence
                    continue
                pre=temp
                temp=temp.next_object_refrence
            curr=curr.next_object_refrence
    def shuffle_meg(self,l1,l2):
        """THis ,ethod will sbuffle merge the linked list"""
        if self.head==None:
            if l1.head.next_object_refrence==None:#This will do merging for the length 1 linked list
                self.head = l1.head
                l1.head.next_object_refrence=l2.head
                return
            self.head=l1.head
            store=l1.head.next_object_refrence#First store
            l1.head.next_object_refrence=l2.head#Then change(update)
            store2=l2.head.next_object_refrence#First store2
            l2.head.next_object_refrence=store#Tehn update
            store=store.next_object_refrence
            temp=l2.head.next_object_refrence
            if temp.next_object_refrence==None:#This will do shuffle merging for length 2
                temp.next_object_refrence=store2
                return
            if temp.next_object_refrence.next_object_refrence==None:#For length 3
                self.mer(temp,store,store2)
                return
            while temp.next_object_refrence.next_object_refrence:#This logic will do shuffle merging for any length
                temp.next_object_refrence=store2
                store2=store2.next_object_refrence
                temp=temp.next_object_refrence
                temp.next_object_refrence=store
                store=store.next_object_refrence
                temp=temp.next_object_refrence
                temp.next_object_refrence=store2
    def mer(self,temp,store,store2):
        temp.next_object_refrence = store2
        store2 = store2.next_object_refrence
        temp = temp.next_object_refrence
        temp.next_object_refrence = store
        store = store.next_object_refrence
        temp = temp.next_object_refrence
        temp.next_object_refrence = store2
    def reverse(self):
        """This method will reverse the structure of the linked list iteratively"""
        if self.head==None:
            return
        if self.head.next_object_refrence.next_object_refrence==None:#THis will check if there are only two elements to reverse in the linked list
            curr = self.head
            next = self.head.next_object_refrence
            next.next_object_refrence = curr  # Updating(Changing the refrence)
            self.head = next
            curr.next_object_refrence = None
            return
        curr=self.head
        next=self.head.next_object_refrence
        next2 = next.next_object_refrence
        next.next_object_refrence=curr#Updating(Changing the refrence)
        self.head=next
        curr.next_object_refrence=None
        if next2.next_object_refrence==None:#THis will check if there arre two elements in the linked list
            next2.next_object_refrence=self.head
            self.head=next2
            return
        while next2.next_object_refrence:#This loop will work for more tahn 3 elements in the linked list.
            next3=next2.next_object_refrence
            next2.next_object_refrence=self.head
            self.head=next2
            next2=next3
        next3.next_object_refrence=self.head
        self.head=next3
    def recursively(self,curr,pre=None):
        """This method will reverse the structure of the linked list adn i Have written multiple if's just
        to cover all the boundry cases fo the recursion"""
        if pre==None and curr.next_object_refrence.next_object_refrence==None:#This will work if there are only two nodes given from the main because other will through and error otherwise
            next=curr.next_object_refrence
            next.next_object_refrence=self.head
            self.head=next
            curr.next_object_refrence=None
            return
        if curr.next_object_refrence==None:#THis will work when there is only one node left at the end after te recursive call
            curr.next_object_refrence=pre
            self.head=curr
            return
        if curr.next_object_refrence.next_object_refrence==None:#THis will work for recursively if there are two nodes left in the linkedd list
            next=curr.next_object_refrence
            curr.next_object_refrence=self.head
            self.head=curr
            next.next_object_refrence=self.head
            self.head=next
            return
        if curr.next_object_refrence.next_object_refrence!=None:#This will work for any number of list
            next=curr.next_object_refrence
            next2=next.next_object_refrence
            next.next_object_refrence=curr
            self.head=next
            curr.next_object_refrence=pre
            self.recursively(curr=next2,pre=next)
def main():
    l=Linked_list()
    l.add_to_the_first(4)
    l.add_to_the_first(3)
    l.add_to_the_first(2)
    l.add_to_the_first(1)
    l.add_to_the_first(5)
    # l.add_to_the_first(6)
    # l.add_to_the_first(7)
    l.show()
    l.recursively(curr=l.head)
    # recursively(curr=l.head)
    # l.recursively()
    # l.add_to_last(5)
    # l.add_to_last(6)
    # l.add_to_last(7)
    # l.add_to_last(7)
    # l.add_to_last(1)
    l.show()
    # l.reverse()
    # l.show()
    # # l.reverse()
    # l.remove_duplication()
    # l.show()
    # l1=Linked_list()
    # l1.add_to_last(31)
    # l1.show()
    # l.show()
    # l3=Linked_list()
    # l3.shuffle_meg(l1,l)
    # l3.show()
main()
"""THis is comple ADT of the Singly limked list
CREDITS:HAmmad FArooq
DATE:24_Feb_2024"""
