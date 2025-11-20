# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        curr=head
        d={}
        while curr:
            if curr not in d:
                d[curr]="yes"
            else:
                return True
            curr=curr.next
        return False
