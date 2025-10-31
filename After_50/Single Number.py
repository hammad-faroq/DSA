def singleNumber( nums):
    if nums == []:
        return 0
    d={}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]]=1
        else:
            count=d[nums[i]]
            count+=1
            d[nums[i]]=count
    for key in d:
        if 1 ==d[key]:
            return key
print(singleNumber(nums = []))