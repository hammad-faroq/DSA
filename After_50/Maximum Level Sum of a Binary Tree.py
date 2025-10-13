# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum1(self, root) -> int:
        """my code was good but it does not wotk for the unbalanced tree beasue i handle then it other side has both child none
         but i dont handle taht if none level has no more level but other sdie has values(nodes) leading to less addition to levelcount
          while level is changes (like calcylating for 2 but level got  to taht point due to un babanced trree )"""
        queue = [root]
        level = 0
        d = {}
        sum = root.val
        # print(sum)
        i = 0
        while queue != []:
            value = queue.pop()
            i += 1
            if value is not None and value is not root:
                sum += value.val
            if i == (2 ** level):
                d[level] = sum
                sum = 0
                i = 0
                level += 1
            if value is not None:
                if value.left is not None:
                    obj = value.left
                    queue.insert(0, obj)
                else:
                    queue.insert(0, None)
                if value.right is not None:
                    obj = value.right
                    queue.insert(0, obj)
                else:
                    queue.insert(0, None)
        # print(d)
        max = float("-inf")
        key = 0
        for i in d:
            if d[i] > max:
                max = d[i]
                key = i + 1
        return key
    def maxLevelSum(self, root):
        if not root:
            return 0

        queue = [root]
        level = 0
        d = {}

        while queue != []:
            size = len(queue)
            sum = 0

            for i in range(size):
                value = queue.pop()
                if value is not None:
                    sum += value.val
                    if value.left is not None:
                        queue.insert(0, value.left)
                    if value.right is not None:
                        queue.insert(0, value.right)

            d[level] = sum
            level += 1

        max_sum = float("-inf")
        key = 0
        for i in d:
            if d[i] > max_sum:
                max_sum = d[i]
                key = i + 1

        print(key)


h1=TreeNode(1)
h2=TreeNode(7)
h3=TreeNode(0)
h1.right=h3
h1.left=h2
h4=TreeNode(12)
h2.left=h4
# h5=TreeNode(0)
# h2.right=h5
# h6=TreeNode(1)
# h7=TreeNode(1)
# h5.left=h6
# h5.right=h7
# h8=TreeNode(1)
# h5.right=h8
# h9=TreeNode(1)
# h6.right=h8
# h8.right=h9
s=Solution().maxLevelSum(h1)