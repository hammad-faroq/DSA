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


h1=ListNode(1)
# h2=ListNode(2)
# h1.next=h2
# h3=ListNode(3)
# h2.next=h3
# h4=ListNode(4)
# h3.next=h4
# h5=ListNode(1)
# h6=ListNode(2)
# h7=ListNode(6)
# h4.next=h5
# h5.next=h6
# h6.next=h7
s=Solution()
head=s.deleteMiddle(h1)
while head:
    print(head.val)
    head=head.next

