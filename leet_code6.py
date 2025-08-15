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
import math
from traceback import print_tb


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def helper(list1, list2):
    if list1.next is not None:
        if list2.next is None:
            # print("helper")
            return "list_one"

    if list2.next is not None:
        # print("/")
        if list1.next is None:
            return "list_two"
    return ""


def mergeTwoLists(list1, list2):
    whole_left = "no_one"
    l_o=True
    l_n=True
    if list1==[] and list2==[]:
        return []
    if list1==[]:
        whole_left= "list_two"
        l_o=False
    if list2==[]:
        print("00mmm")
        whole_left="list_one"
        l_n=False



    if l_o:
        print("list one is not empty")
        head = ListNode(list1[0])
        previous = head
        for i in range(1, len(list1)):
            current = ListNode(list1[i])
            previous.next = current
            previous = current
    if l_n:
        print("list 2 is aslo noew empty")
        head2 = ListNode(list2[0])
        previous2 = head2
        for i in range(1, len(list2)):
            current2 = ListNode(list2[i])
            previous2.next = current2
            previous2 = current2

    if l_o is False:
        list1=None
        list2 = head2
    elif l_n is False:
        list2=None
        list1 = head
    else:
        print("both set")
        list1=head
        list2=head2
    # while list2:
    #     print(list2.val)
    #     list2=list2.next
    # print("end")
    # while list1:
    #     print(list1.val)
    #     list1=list1.next
    l = []
    while list1 and list2:
        # print("flist ", list1.val)
        # print("Slist ", list2.val)

        if list1.val > list2.val:
            l.append(list2.val)
            whole_left = helper(list1=list1, list2=list2)
            list2 = list2.next
        elif list1.val < list2.val:
            # print("i ran")
            l.append(list1.val)
            whole_left = helper(list1=list1, list2=list2)
            list1 = list1.next
        elif list1.val == list2.val:
            l.append(list1.val)
            l.append(list2.val)
            whole_left = helper(list1=list1, list2=list2)
            list1 = list1.next
            list2 = list2.next
        if whole_left != "":
            break
    # print(whole_left)
    if whole_left == "":
        if list1 is not None:
            l.append(list1.val)
        if list2 is not None:
            l.append(list2.val)

    if whole_left == "list_one":  # one list 2 had left
        # print("leist 1 left ")
        if list2 is not None:
            is_left = True
            while list1:
                print("infiniein")
                print(list1.val, list2.val)
                print(is_left)
                if list1.val > list2.val and is_left:
                    # print("leftt is done!!!!!!!!!!!!!!!!!!!!")
                    l.append(list2.val)
                    is_left = False
                l.append(list1.val)
                list1 = list1.next
            if is_left:
                l.append(list2.val)
        else:
            # print("uuuu")
            while list1:
                l.append(list1.val)
                list1 = list1.next
    if whole_left == "list_two":
        # print("List2 left")
        if list1 is not None:
            is_left = True
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
                list2 = list2.next
    print(l)
    leng=len(l)
    median=0
    leng=leng%2
    if leng==0:
        median=l[len(l)//2]+l[len(l)//2-1]
        median=float(median/2)
    else:
        median=math.floor(len(l)//2)
        median=float(l[median])
    print(median)

l4=[1,3]
l=[]
li = mergeTwoLists(l4, l)
# while li:
#     print(li.val, "---->", end="")
#     li = li.next
# print(-7<-4)
