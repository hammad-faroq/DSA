import heapq
def totalCost(costs, k, candidates):
    """List ma sa remove nai kiya, two points to track and add the number in the heap"""
    left_ptr = 0
    right_ptr = len(costs) - 1
    left_heap=[]
    right_heap=[]
    total_cost = 0
    while len(left_heap) < candidates and left_ptr <= right_ptr:
        heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
        left_ptr += 1
        if left_ptr <= right_ptr:
            heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
            right_ptr -= 1
    for _ in range(k):
        if not left_heap or (right_heap and right_heap[0] < left_heap[0]):
            cost_chosen, index_chosen = heapq.heappop(right_heap)
            if left_ptr <= right_ptr:
                heapq.heappush(right_heap, (costs[right_ptr], right_ptr))
                right_ptr -= 1
        else:
            cost_chosen, index_chosen = heapq.heappop(left_heap)
            if left_ptr <= right_ptr:
                heapq.heappush(left_heap, (costs[left_ptr], left_ptr))
                left_ptr += 1
        total_cost += cost_chosen