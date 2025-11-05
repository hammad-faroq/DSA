import heapq
def maxScore(nums1, nums2, k):
    l=[]
    max=0
    score=0

    for i in range(len(nums1)):
        l.append((nums2[i],nums1[i]))
    l.sort(key=lambda x: x[0], reverse=True)
    current_sum = 0
    min_heap = []  # This heap stores only n1 values to track the largest K

    for n2, n1 in l:  # l is now sorted (n2, n1)
        heapq.heappush(min_heap, n1)
        current_sum += n1
        if len(min_heap) > k:#n1 ma sa minimum niqal dna ha
            smallest_n1 = heapq.heappop(min_heap)
            current_sum -= smallest_n1
        if len(min_heap) == k:#if we sortd be ascending then at the k=, n2 will beminimum all all the prevoius
            score = current_sum * n2
        if max<score:
            max=score
    return max

print(maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))














def maxScore1(nums1, nums2, k):
    nums2.sort()
    max=0
    for i in range(len(nums2)):
        """Notwhen we sort, the cahnged the order taht was needed (:"""
        sum=0
        min=0
        res=0
        min=nums2[i]
        for j in range(k):
            if i+2<len(nums2):
                sum=nums1[i]+nums1[i+1]+nums1[i+2]
        res=sum*min
        print(min,sum)
        if max<res:
            max=res
    return max

    # print(nums2)
# print(maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
