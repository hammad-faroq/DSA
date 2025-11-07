def longestSubarray(nums):
    max=0
    prev=0
    count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count+=1
        else:
            if i+1<len(nums):
                if nums[i+1]==0:
                    count=0
                    prev=0
                    continue
            count-=prev
            prev=count
        if count>max:
            max=count
        if count==len(nums):
            max=count-1

    print(max)
longestSubarray(nums = [1,1,0,1])
longestSubarray(nums = [0,1,1,1,0,1,1,0,1])
longestSubarray(nums = [1,1,1])
longestSubarray([1,1,0,1,1,1,0,1,0,0])
longestSubarray([0,0,1,0,1,0,0,1])
longestSubarray([1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1])