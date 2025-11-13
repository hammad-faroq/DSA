# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        """Height will not be balanced (:"""
        mid=len(nums)//2
        low=mid-1
        high=mid+1
        print(low,high)
        root=TreeNode(nums[mid])
        temp = root
        while low>=0:
            if nums[low]<temp.val:
                temp.left=TreeNode(nums[low])
                temp=temp.left
            if nums[low]>temp.val:
                temp.right=TreeNode(nums[low])
                temp=temp.right
            low-=1
        temp = root
        while high<len(nums):
            if high+2<len(nums):
                mid1=high+2
                mid=high+1
                temp.right = TreeNode(nums[mid])
                temp=temp.right
                temp.left = TreeNode(nums[high])
                temp.right = TreeNode(nums[mid1])
            elif high+1<len(nums):
                mid = high + 1
                temp.right = TreeNode(nums[mid])
                temp = temp.right
                temp.left = TreeNode(nums[high])
            else:
                temp.right = TreeNode(nums[high])

            # if nums[high]<temp.val:
            #     temp.left=TreeNode(nums[high])
            #     temp=temp.left
            # if nums[low]>temp.val:
            #     temp.right=TreeNode(nums[high])
            #     temp=temp.right
            high+=3
        return root

    def sortedArrayToBST(self,nums):
        """Balanced verison beaise at eveary call we want mid to be the root left and root right"""
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root



s=Solution()
# s.sortedArrayToBST(nums = [-10,-3,0,5,9])
rot=s.sortedArrayToBST([1,3])
while rot:
    print(rot.val)
    print(rot.left.val)
    # print(rot.right.val)
    # rot=rot.left.left