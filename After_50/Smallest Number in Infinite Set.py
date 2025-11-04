import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.added_back_nums = []
        self.next_unpopped = 1

    def popSmallest(self) -> int:
        if self.added_back_nums:
            return heapq.heappop(self.added_back_nums)
        else:
            result = self.next_unpopped
            self.next_unpopped += 1

            return result

    def addBack(self, num: int) -> None:
        if num < self.next_unpopped:# because the number is already in the infifnite set,ie counter
            #so we must store it in case it is lesser than the self.pop
            if num not in self.added_back_nums:
                heapq.heappush(self.added_back_nums, num)