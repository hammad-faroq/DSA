def longestOnes(nums, k):
    """we ave to find the max nomber of consective 1s if we flip k no of zeros in it as well"""
    max=0
    no=0
    slide=0
    i=0
    while i < len(nums):
        if k!=0:
            if nums[i]==1:
                # print("first iteration")
                no+=1
        if nums[i]==0 and k>=1:
            # print("first iteration sub k")
            no+=1
            k-=1
        elif k==0:#har iteration par ma apna slides ka max consective 1 no, no variable ma rak rha
            print(i, slide)
            if nums[i]==0 and nums[slide]==1:#case1
                slide+=1
                no-=1
                i-=1
            elif nums[i]==0 and nums[slide]==0:
                slide+=1
            elif nums[i]==1 and nums[slide]==0:
                no+=1
            elif nums[i]==1 and nums[slide]==1:
                no+=1
            elif slide==i:
                i+=1
                print("conti")
                continue
        if no> max:
            max=no
        i += 1
    return max
print(longestOnes([1,0,1,0],0))
# print(longestOnes(nums = [0,1,0,1,0,1,1,1]
# ,k = 2))