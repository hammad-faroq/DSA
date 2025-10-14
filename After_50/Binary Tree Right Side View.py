# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        if root.left and root.right is None:
            return [root.val]

        queue = [root]
        d = []

        while queue != []:
            size = len(queue)
            k=0

            for i in range(size):
                value = queue.pop()
                if k==0:
                    d.append(value.val)
                k+=1
                if value.right is not None:
                    queue.insert(0, value.right)
                if value.left is not None:
                    queue.insert(0, value.left)
        print(d)

h1=TreeNode(1)
h2=TreeNode(2)
h3=TreeNode(3)
# h1.right=h3
h1.left=h2
# h4=TreeNode(5)
# h2.left=h4
# h5=TreeNode(4)
# h4.left=h5
# h6=TreeNode(1)
# h7=TreeNode(1)
# h5.left=h6
# h5.right=h7
# h8=TreeNode(1)
# h5.right=h8
# h9=TreeNode(1)
# h6.right=h8
# h8.right=h9
s=Solution().rightSideView(h1)