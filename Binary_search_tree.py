# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val: int):
        curr=root
        while curr:
            if val>curr.val:
                curr=curr.right
            elif val<curr.val:
                curr=curr.left
            elif val==curr.val:
                return curr
        return None
h1=TreeNode(4)
h2=TreeNode(2)
h3=TreeNode(7)
h4=TreeNode(1)
h5=TreeNode(3)
h1.left=h2
h1.right=h3
h2.left=h4
h2.right=h5
s=Solution()
n=s.searchBST(h1,2)
while n:
    print(n.val)
    print(n.left.val)
    print(n.right.val)
    n=n.right
    # n=n.right

