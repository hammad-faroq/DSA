def maxOperations(nums, k):
    nums=sorted(nums)
    i=0
    j=len(nums)-1
    no_operations = 0
    while i < j:
        sum=nums[i]+nums[j]
        if sum==k:
            no_operations+=1
            i+=1
            j-=1
        elif sum < k:
            i+=1
        else:
            j-=1
    return no_operations

# maxOperations([3,2,1],1)
maxOperations( nums = [1,2,3,4], k = 5)