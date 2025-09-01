
def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(0,len(nums)):
        i=0
        j=0
        while j< len(nums):
            if nums[i]==0:
                # print(nums[i])
                # print(nums)
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            j+=1
        print(nums)
moveZeroes(nums = [0,0,1])
moveZeroes([0,1,0,3,12])