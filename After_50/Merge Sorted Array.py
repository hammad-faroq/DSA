def merge( nums1, m, nums2, n: int):
    i=0
    j=0

    while i < len(nums1):
        # if nums1[i]==0:
        #     break
        if j>=len(nums2):
            break
        if nums1[i]< nums2[j]:
            i+=1
        elif nums1[i]==nums2[j]:
            nums1.insert(i,nums2[j])
            j+=1
            i+=2
        elif nums1[i]>nums2[j]:
            nums1.insert(i,nums2[j])
            j+=1
            i+=1
    nums1[:] = nums1[:m + j]
    if j < len(nums2):
        # print("ina")
        # nums1[:]=nums1[:m+j]#not creates new copy
        #nums=nums[:] create a new copy
        for i in range(j,len(nums2)):
            nums1.append(nums2[i])
            j+=1
    # c=0
    # for i in range(-1,-len(nums1),-1):
    #     # print(i)
    #     # print(nums1[i])
    #     if nums1[i]==0:
    #         # print("uaau")
    #         c+=1
    #     else:
    #         break
    # print(c)
    # c=len(nums1)-c
    print(nums1)




    # for i in range(len(nums1)):
    #     print(nums1[i])
merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
# print(nums1)
# merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)
merge([-1,-1,0,0,0,0],4,[-1,0],2)