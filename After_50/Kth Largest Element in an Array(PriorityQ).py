import heapq
def findKthLargest(nums, k):
    pq=[]
    for value in nums:
        heapq.heappush(pq, -value)
    for m in range(k):
        k_max=heapq.heappop(pq)
    return - k_max


