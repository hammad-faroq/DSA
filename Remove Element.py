def removeElement(nums, val):
    i=0
    k=0
    while i< len(nums):
        if nums[i]==val:
            # print("yes")
            nums.pop(i)
            # nums.append("-")
        else:
            k+=1
            i+=1
    print(k)
    print(nums)
# removeElement(nums = [3,2,2,3], val = 3)
# removeElement([0,1,2,2,3,0,4,2],2)
def add_two_numbers_without_using_Add(a,b):
    c=a
    for i in range(b):

        print(c)
add_two_numbers_without_using_Add(7,10)