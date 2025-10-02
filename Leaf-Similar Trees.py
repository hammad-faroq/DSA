# def maxDepth(root):
#     # i=0
#     # count=0
#     # if len(root)>=3:
#     #     stack=[]
#     #     left=2*i+1
#     #     right=2*i+2
#     #     if left and right <len(root):
#     #         if root[left] is not None and root[right] is not None:
#     #             stack.append(root[left])
#     #             stack.append(root[right])
#     #             count+=1
#     #     while stack
#     # i=0
#     count=1
#     # max=0
#     stack=[root[0]]
#     while stack!=[]:
#         value=stack.pop()
#         i=root.index(value)
#         # print(i)
#         left = 2 * i + 1
#         right=2*i+2
#         # print(left)
#         # print(right)
#         if left and right < len(root):
#             if root[left] is not None or root[right] is not None:
#                 if root[left] is not None:
#                     stack.append(root[left])
#                 if root[right] is not None:
#                     stack.append(root[right])
#                 count+=1
#     print(count)
#
#             # if root[left] is  None and root[right] is None:
#
#
# maxDepth(root = [3,9,20,None,None,15,7])
# maxDepth(root = [1,None,2])
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self,root1, root2):
        s=self.helper(root1)
        s2=self.helper(root2)
        if s==s2:
            print(True)
    def helper(self,root):
        stack = [root]
        s=[]
        while stack != []:
            value= stack.pop()
            if value.left is not None or value.right is not None:
                if value.left is not None:
                    obj=value.left
                    stack.append(obj)
                if value.right is not None:
                    obj=value.right
                    stack.append(obj)
            if value.left is  None and value.right is None:
                s.append(value.val)
        return s
    def maxDepth(self, root) -> int:
        """Jsut creatting a tuple to sotre the level of each mode and retrieving taht using _,_ solves the isuue rahter tahtn creating messy logic
         and dept+1 not deapt=dept+1, simple login thinking make life and probel easier using the data strcuture"""
        count = 1
        max1=0
        if root is None:
            return 0
        stack = [(root,1)]
        while stack != []:
            value,depth= stack.pop()
            max1=max(max1,depth)
            if value.left is not None or value.right is not None:
                if value.left is not None:
                    obj=value.left
                    stack.append((obj,depth+1))
                if value.right is not None:
                    obj=value.right
                    stack.append((obj,depth+1))
                count += 1

        # print(count)
        return max1
# h10=TreeNode(None)
h1=TreeNode(3)
h2=TreeNode(1)
h3=TreeNode(5)
h1.right=h2
h1.left=h3
h4=TreeNode(9)
h5=TreeNode(8)
h2.left=h4
h2.right=h5
h6=TreeNode(6)
h7=TreeNode(2)
h3.left=h6
h3.right=h7
h8=TreeNode(7)
h9=TreeNode(4)
h7.left=h8
h7.right=h9


h11=TreeNode(3)
h22=TreeNode(1)
h33=TreeNode(5)
h11.right=h22
h11.left=h33
h44=TreeNode(6)
h55=TreeNode(7)
h33.left=h44
h33.right=h55
h66=TreeNode(4)
h77=TreeNode(2)
h22.left=h66
h22.right=h77
h88=TreeNode(9)
h99=TreeNode(8)
h77.left=h88
h77.right=h99
s=Solution().leafSimilar(h1,h11)
