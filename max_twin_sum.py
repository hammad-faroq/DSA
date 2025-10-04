# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:
        """Problem is that time limit exceed other wise logic is correct (:"""
        if not head:
            return 0
        sum=0
        i=0
        n=0
        max1=0
        curr = head
        s=[]
        while curr:
            n+=1
            curr=curr.next
        curr=head
        # temp=curr
        while curr:
            if s !=[]:
                sum,ind=s.pop()
                if i==ind:
                    sum+=curr.val
                else:
                    s.append((sum, ind))
            if 0 <= i <= (n / 2) - 1:
                # sum=curr.val
                # twin_ind=(n-1-i)
                s.append((curr.val,n-1-i))
                # temp=curr
                # for j in range(i,twin_ind):
                #     curr=curr.next
                # sum += curr.val
                # print(sum)
                # curr=temp
            if max1<sum:
                max1=sum
            sum=0
            i+=1
            curr=curr.next
        return max1




h1=ListNode(5)
h2=ListNode(4)
h1.next=h2
h3=ListNode(2)
h2.next=h3
h4=ListNode(1)
h3.next=h4
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
print(s.pairSum(h1))
# while head:
#     print(head.val)
#     head=head.next

