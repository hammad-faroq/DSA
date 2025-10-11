class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root):
        zig_zag = 0
        max1 = 0
        if root is None:
            return zig_zag
        stack = [(root, 0, "None")]
        while stack != []:
            value, zig_zag, parent_dir = stack.pop()
            if value.left is not None or value.right is not None:
                if value.left is not None:
                    obj = value.left
                    if parent_dir == "right" or parent_dir == "None":
                        stack.append((obj, zig_zag + 1, "left"))
                    else:
                        stack.append((obj, 1, "left"))
                if value.right is not None:
                    obj = value.right
                    if parent_dir == "left" or parent_dir == "None":
                        stack.append((obj, zig_zag + 1, "right"))
                    else:
                        stack.append((obj, 1, "right"))
            if zig_zag > max1:
                max1 = zig_zag
        print(max1)
        return max1