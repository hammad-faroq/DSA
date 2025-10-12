class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if p ==root:
            return p
        if q ==root:
            return q
        d = {}
        stack = [root]
        while stack != []:
            value = stack.pop()
            if value.left is not None or value.right is not None:
                if value.left is not None:
                    obj = value.left
                    d[obj] = value
                    stack.append(obj)
                if value.right is not None:
                    obj = value.right
                    d[obj] = value
                    stack.append(obj)
        temp = d.get(p, None)
        while temp is not None:
            temp2=d.get(q,None)
            while temp2 is not None:
                if temp==temp2:
                    return temp
                elif temp2==p:
                    return p
                elif temp == q:
                    return q
                else:
                    temp2 = d.get(temp2, None)
            temp = d.get(temp, None)
h1=TreeNode(3)
h2=TreeNode(5)
h3=TreeNode(1)
h1.right=h3
h1.left=h2
h4=TreeNode(6)
h2.left=h4
h5=TreeNode(2)
h2.right=h5
h6=TreeNode(7)
h7=TreeNode(4)
h5.left=h6
h5.right=h7
h8=TreeNode(0)
h9=TreeNode(8)
h3.left=h8
h3.right=h9
s=Solution().lowestCommonAncestor(h1,h2,h7)
print(s.val)