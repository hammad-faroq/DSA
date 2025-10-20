def searchInsert(nums, target):
    low=0
    high=len(nums)
    mid=(low+high)//2
    while low<high:
        print(mid)
        if nums[mid]>target:
            high=mid
            # print("yes")
        elif nums[mid]<target:
            low=mid+1
            # print("i ran")
        elif nums[mid]==target:
            return mid
        mid = (low + high) // 2
    return mid
# print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert(nums = [1,3,5,6], target = 0))