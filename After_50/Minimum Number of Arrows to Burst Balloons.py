class Solution:
    def findMinArrowShots(self, points) -> int:
        """Shoot the first one end and skip the ones waht are in the between, but first sort by endoing ime , this gives the mniiium no of arrows"""
        points.sort(key=lambda x: x[1])
        count = 1
        prev_end = points[0][1]

        for i in range(1, len(points)):
            start, end = points[i]
            if start <= prev_end:
                continue
            else:
                count+=1
                prev_end = end
        return coun
s=Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[4,5]]))