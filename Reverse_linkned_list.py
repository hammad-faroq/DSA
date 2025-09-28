# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head):
        """In linked list head=NOne shows an empty linked list"""
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        # print(count)
        if count==1:
            return None
        mid=count//2
        # print(mid)
        curr=head
        prev=None
        for i in range(count):
            if i == mid:
                # print(prev.val)
                # print(curr.val)
                prev.next = curr.next
                return head
            if curr.next:
                prev=curr
                curr=curr.next
                # print(prev.val)
                # print(curr.val)

    def reverseList(self, head):
        curr = head
        prev = None
        next1 = curr.next
        if head.next is None:
            return head
        if not next1.next:
            next1.next=curr
            curr.next=prev
            return next1
        while next1.next:
            temp=next1
            next1=next1.next
            temp.next=curr
            curr.next=prev
            prev=curr
            curr=temp
        next1.next=temp
        return next1





h1=ListNode(1)
h2=ListNode(2)
h1.next=h2
# h3=ListNode(3)
# h2.next=h3
# h4=ListNode(4)
# h3.next=h4
# h5=ListNode(5)
# h6=ListNode(6)
# h7=ListNode(7)
# h4.next=h5
# h5.next=h6
# h6.next=h7
s=Solution()
# head=s.deleteMiddle(h1)
head=s.reverseList(h1)
while head:
    print(head.val)
    head=head.next

