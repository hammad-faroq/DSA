"""Product of array except self"""

def productExceptSelf(nums):
    """this solution is not O(n)"""
    i=0
    j=0
    out=[None for i in range(len(nums))]
    sum=1
    while i< len(nums):
        if i==j:
            j+=1
            continue
            # sum+=nums[j]
        elif j==len(nums):
            print(sum)
            out[i]=sum
            i+=1
            sum=1
            j=0
        sum*=nums[j]
        j+=1
    print(out)
# productExceptSelf([1,2,3,4])
# productExceptSelf([-1,1,0,-3,3])
# productExceptSelf([0,1,2])
# productExceptSelf([2,3,4,5,6])
# productExceptSelf([5])
def productExceptSelf1(nums):
    """this gonna hev time complexity of O(n)"""
    out = [1 for i in range(len(nums))]
    prefix=1
    suffix=1
    for i in range(len(nums)):
        out[i]=prefix
        prefix*=nums[i]
    # prefix = 1
    # for i in range(len(nums)):
    #     out[i] = prefix
    #     prefix *= nums[i]
    # suffix = 1
    # print(out)
    for i in range(len(nums) - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    # print(out)
    print(out)
productExceptSelf1([1,2,3,4])