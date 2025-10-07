def findPeakElement(nums):
    left=0
    right=len(nums)-1
    mid=(left+right)//2
    while left<right:
        if nums[mid]>nums[mid+1]:
            right=mid
        else:
            left=mid+1
        mid=(left+right)//2
    print(left)
# findPeakElement([1,2,1,3,5,6,4])
findPeakElement([3,1,2])

"""Case 1️⃣ — Downhill slope

nums[mid] > nums[mid + 1]

That means we are on a downward slope 🏔️
So, the peak must be on the left side (could even be mid itself).
→ We shrink our search space to [left, mid].

Case 2️⃣ — Uphill slope

nums[mid] < nums[mid + 1]

That means we are climbing upward,
so the peak must be on the right side.
→ We move our search range to [mid + 1, right]."""