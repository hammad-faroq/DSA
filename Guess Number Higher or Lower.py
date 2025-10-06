class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        mid=(low+high)//2
        waht=guess(mid)
        while waht !=0:
            if waht == -1:#chota ha
                high=mid-1
                mid=(low+high)//2
            elif waht == 1:
                low = mid+1
                mid=(low+high)//2
            waht=guess(mid)
        return mid