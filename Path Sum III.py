class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        """we used a simple approch with DFS, with storing each {child: parent} and using the get tos get the curr nodes preant and his preatn so a bit logic was not correct but approch was good"""
        d = {}
        stack = [root]
        i = 0
        c = 0
        while stack != []:
            sum1 = 0
            value = stack.pop()
            if i >= 1:
                temp = value
                while temp is not None:
                    sum1 += temp.val
                    if sum1 == targetSum:
                        c += 1
                    temp = d.get(temp, None)
            if value.left is not None or value.right is not None:
                if value.left is not None:
                    obj = value.left
                    d[obj] = value
                    stack.append(obj)
                if value.right is not None:
                    obj = value.right
                    d[obj] = value
                    stack.append(obj)
            i += 1
        return c


h1=TreeNode(10)
h2=TreeNode(5)
h3=TreeNode(-3)
h1.right=h3
h1.left=h2
h4=TreeNode(3)
h2.left=h4
h5=TreeNode(2)
h2.right=h5
h6=TreeNode(3)
h7=TreeNode(-2)
h4.left=h6
h4.right=h7
h8=TreeNode(1)
h5.right=h8
h9=TreeNode(11)
h3.right=h9
# h7.left=h8
# h7.right=h9
s=Solution().pathSum(h1,8)
print(s)
