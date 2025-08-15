
# def addTwoNumbers(l1,l2):
#     num1=num2=""
#     for i in range(len(l1)-1,-1,-1):
#         num1+=str(l1[i])
#     for i in range(len(l2)-1, -1, -1):
#         num2+=str(l2[i])
#     res=int(num1)+int(num2)
#     res2=str(res)
#     list1=[]
#     for i in range(len(res2)-1,-1,-1):
#         list1.append(int(res2[i]))
#     print(list1)
# addTwoNumbers([2,4,3],[5,6,4])

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def helper(list1,list2):
    if list1.next is not None:
        print("/")
        if list2.next is None:
            print("helper")
            return "list_one"

    if list2.next is not None:
        print("/")
        if list1.next is None:
            return "list_two"
    return ""

def mergeTwoLists(list1, list2):
    # head = ListNode(list1[0])
    # previous = head
    # for i in range(1, len(list1)):
    #     current = ListNode(list2[i])
    #     previous.next = current
    #     previous = current
    #
    # head2 = ListNode(list2[0])
    # previous = head2
    # for i in range(1, len(list2)):
    #     current = ListNode(list2[i])
    #     previous.next = current
    #     previous = current



    whole_left = "no_one"
    if list1==None and list2 is None:
        return []
    if list1 is None:
        whole_left= "list_two"
    if list2 is None:
        print("00")
        whole_left="list_one"


    l=[]
    while list1 and list2:
        print("flist ",list1.val)
        print("Slist ",list2.val)


        if list1.val>list2.val:
            l.append(list2.val)
            whole_left = helper(list1=list1, list2=list2)
            list2 = list2.next
        elif list1.val<list2.val:
            print("i ran")
            l.append(list1.val)
            whole_left = helper(list1=list1, list2=list2)
            list1 = list1.next
        elif list1.val==list2.val:
            l.append(list1.val)
            l.append(list2.val)
            whole_left = helper(list1=list1, list2=list2)
            list1=list1.next
            list2=list2.next
        if whole_left!="":
            break
    print(whole_left)
    if whole_left=="":
        if list1 is not None:
            l.append(list1.val)
        if list2 is not None:
            l.append(list2.val)

    if whole_left=="list_one":#one list 2 had left
        print("leist 1 left ")
        if list2 is not None:
            is_left=True
            while list1:
                print("infiniein")
                print(list1.val, list2.val)
                # print(is_left)
                if list1.val>list2.val and is_left:
                    print("leftt is done!!!!!!!!!!!!!!!!!!!!")
                    l.append(list2.val)
                    is_left=False
                l.append(list1.val)
                list1=list1.next
            if is_left:
                l.append(list2.val)
        else:
            while list1:
                l.append(list1.val)
                list1=list1.next
    if whole_left=="list_two":
        print("List2 left")
        if list1 is not None:
            is_left=True
            while list2:
                if list2.val > list1.val and is_left:
                    # print("leftt")
                    l.append(list1.val)
                    is_left = False
                l.append(list2.val)
                list2 = list2.next
            if is_left:
                l.append(list1.val)
        else:
            while list2:
                l.append(list2.val)
                list2=list2.next
    head=ListNode(l[0])
    previous=head
    for i in range(1,len(l)):
        current=ListNode(l[i])
        previous.next=current
        previous=current
    return head

l=ListNode(1)
l1=ListNode(2)
l3=ListNode(3)
l31=ListNode(4)
# l32=ListNode(1)
# l33=ListNode(6)
# l34=ListNode(6)
l.next=l1
l1.next=l3
l3.next=l31
# l31.next=l32
# l32.next=l33
# l33.next=l34
#
l4=ListNode(4)
l5=ListNode(5)
l6=ListNode(6)
l7=ListNode(55)
l4.next=l5
l5.next=l6
l6.next=l7
li=mergeTwoLists(l4,l)
while li:
    print(li.val,"---->",end="")
    li=li.next
# print(-7<-4)
