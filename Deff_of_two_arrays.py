def findDifference(nums1, nums2):
    set1=set()
    set2=set()
    ans1=[]
    ans2=[]
    for i in nums1:
        set1.add(i)
    for i in nums2:
        set2.add(i)
    common=set1&set2
    for i in nums1:
        if i not in common and i not in ans1:
            ans1.append(i)
    for j in nums2:
        if j not in common and j not in ans2:
            ans2.append(j)
    return [ans1,ans2]

    # print(set1)
print(findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))