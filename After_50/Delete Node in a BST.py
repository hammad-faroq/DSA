class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        d={}
        stack = [root]
        is_break=False
        if root is None:
            return None
        if root.val==key:
            curr=root
            if curr.left is None and curr.right is None:
                return None
            elif curr.left and curr.right:
                par=curr.right
                left1=curr.right.left
                if left1 is None:
                    curr.right.left=curr.left
                    return par
                while left1.left:
                    left1=left1.left
                left1.left=curr.left
                return par
            elif curr.right and curr.left is None:#case3
                return  curr.right
            elif curr.right is None and curr.left:
                return curr.left

        while stack != []:
            value = stack.pop()
            if value.left is not None or value.right is not None:
                if value.left is not None:
                    obj = value.left
                    stack.append(obj)
                    d[obj]=value
                    if value.left.val==key:
                        is_break=True
                        curr = value.left
                        break
                if value.right is not None:
                    obj = value.right
                    stack.append(obj)
                    d[obj] = value
                    if value.right.val==key:
                        is_break = True
                        curr=value.right
                        break
        if is_break:
            if curr.left is None and curr.right is None:#case1
                par=d[curr]
                if curr.val<par.val:
                    par.left=None
                else:
                    par.right=None
                return root
            elif curr.left and curr.right:#case2
                par = d[curr]
                if curr.val > par.val:
                    par.right=curr.right
                    left1=curr.right.left
                    if left1 is None:
                        curr.right.left=curr.left
                        return root
                    while left1.left:
                        left1=left1.left
                    left1.left=curr.left
                else:
                    par.left=curr.right
                    left1 = curr.right.left
                    if left1 is None:#if the new node taking plase has no left child
                        curr.right.left = curr.left
                        return root
                    while left1.left:
                        left1 = left1.left
                    left1.left = curr.left
                return root
            elif curr.right and curr.left is None:#case3
                par = d[curr]
                if curr.val > par.val:
                    par.right=curr.right
                else:
                    par.left=curr.right
                return  root
            elif curr.right is None and curr.left:#case4
                par = d[curr]
                if curr.val > par.val:
                    par.right=curr.left
                else:
                    par.left=curr.left
                return  root
        else:
            return root

# h10=TreeNode(None)
h1=TreeNode(15)
h2=TreeNode(7)
h3=TreeNode(30)
h1.right=h3
h1.left=h2
h4=TreeNode(1)
h5=TreeNode(10)
h2.left=h4
h2.right=h5
h6=TreeNode(18)
h7=TreeNode(40)
h3.left=h6
h3.right=h7
h8=TreeNode(16)
h9=TreeNode(24)
h6.left=h8
h6.right=h9
s=Solution().deleteNode(h1,h3.val)
print(s)

# h11=TreeNode(3)
# h22=TreeNode(1)
# h33=TreeNode(5)
# h11.right=h22
# h11.left=h33
# h44=TreeNode(6)
# h55=TreeNode(7)
# h33.left=h44
# h33.right=h55
# h66=TreeNode(4)
# h77=TreeNode(2)
# h22.left=h66
# h22.right=h77
# h88=TreeNode(9)
# h99=TreeNode(8)
# h77.left=h88
# h77.right=h99

