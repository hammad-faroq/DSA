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
        if count==1:
            return None
        mid=count//2
        curr=head
        prev=None
        for i in range(count):
            if i == mid:
                prev.next = curr.next
                return head
            if curr.next:
                prev=curr
                curr=curr.next

    def oddEvenList(self,head):
        count = 0
        curr = head
        is_extra=False
        while curr:
            count += 1
            curr = curr.next
        if count==2 or count==1 or count==0:
            return head
        if count==3:
            curr = head
            first=curr
            sec=curr.next
            first2=curr.next.next
            first.next=first2
            sec.next=None
            first2.next=sec
            return curr

        times=count//4
        if times>=1:
            curr = head
            first = curr
            sec = curr.next
            first2 = curr.next.next
            sec2 = curr.next.next.next
            first.next = first2
            sec.next = sec2
            if count==4:
                first2.next = sec
                return curr
        if count>(count//2)*2:
            # print(count)
            # print((count//2)*2)
            is_extra=True
            # print(":Extra")
        if times==1 and is_extra:
            if not sec2.next.next:
                first2.next=sec2.next
                sec2.next=None
                first2=first2.next
                first2.next = sec
                return curr
        times = (count - 4) // 2
        temp2 = sec
        for i in range(times):
            first=sec2.next
            sec=sec2.next.next
            first2.next=first
            sec2.next=sec
            first2=first
            sec2=sec
        if is_extra:
            first.next=sec.next
            sec.next=None
            first=first.next
        first.next=temp2
        return curr

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
h3=ListNode(3)
h2.next=h3
# h4=ListNode(4)
# h3.next=h4
# h5=ListNode(5)
# h6=ListNode(6)
# h7=ListNode(7)
# h4.next=h5
# h5.next=h6
# h6.next=h7
# h8=ListNode(8)
# h7.next=h8
# h9=ListNode(9)
# h10=ListNode(10)
# h8.next=h9
# h9.next=h10
s=Solution()
# head=s.deleteMiddle(h1)
# head=s.reverseList(h1)
head=s.oddEvenList(h1)
while head:
    print(head.val)
    head=head.next

