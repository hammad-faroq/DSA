def pivotIndex(nums):
    sum_left=[]
    sum_right=[None for i in range(len(nums))]
    sum=0
    for i in range(len(nums)):
        if i == 0:
            sum_left.append(0)
        else:
            sum+=nums[i-1]
            sum_left.append(sum)
    index=-1
    sum=0
    for i in range(len(nums)-1,-1,-1):
        if i == len(nums)-1:
            sum_right[index]=0
        else:
            sum+=nums[i+1]
            sum_right[index]=sum
        index-=1
    print(sum_right)
    print(sum_left)
    if sum_left[0] == sum_right[0]:
        return 0
    if len(sum_left)>=2:
        if sum_left[1]==sum_right[1]:
            return 1

    for i in range(1,len(sum_right)-1):
        # print(i)
        # print(sum_left[i+1],sum_right[i-1])
        if sum_left[i+1]==sum_right[i-1]:
            # print(i)
            # break
            return i
    if len(sum_left)>=2:
        # print("yes")
        # if sum_left[0]==sum_right[0]:
        #     return 0
        # if sum_left[1]==sum_right[1]:
        #     return 1
        if sum_left[-1]==sum_right[-1] :
            return len(nums)-1
        if sum_left[-2]==sum_right[-2]:
            return len(nums) - 2
    return -1
# pivotIndex([1,7,3,6,5,6])
# print(pivotIndex([0,0]))
# print(pivotIndex([-1,-1,1,0,0,-1]))
print(pivotIndex([0]))