class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        stack=[(head,head.val)]
        curr=head.next
        while curr.next:
            # ref,value=stack[-1]
            # if curr.val==value:
            if curr.val in [value for ref, value in stack]:
                if len(stack)==1:
                    head=curr
                    stack.pop()
                else:
                    ref1, value1 = stack[-1]
                    ref1.next=curr.next
                    curr = curr.next
                    continue
            stack.append((curr,curr.val))
            curr=curr.next
        if curr.val in [value for ref, value in stack]:
            ref1, value1 = stack[-1]
            ref1.next=None
        return head







h1=ListNode(1)
# h2=ListNode(1)
# h1.next=h2
# h3=ListNode(2)
# h2.next=h3
# h4=ListNode(1)
# h3.next=h4
# h5=ListNode(2)
# h6=ListNode(3)
# h7=ListNode(3)
# h4.next=h5
# h5.next=h6
# h6.next=h7
# h8=ListNode(1)
# h7.next=h8
# h9=ListNode(2)
# h10=ListNode(1)
# h8.next=h9
# h9.next=h10
s=Solution().deleteDuplicates(None)
while s:
    print(s.val)
    s=s.next