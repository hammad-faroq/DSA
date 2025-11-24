class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                count += 1  # remove this interval
            else:
                prev_end = end
        return count

    def eraseOverlapIntervals1(self, intervals):
        """This is brute force with somewaht worng logic"""
        n=0
        for i in range(len(intervals)-1):
            a=intervals[i][0]
            b = intervals[i][1]
            for j in range(i+1,len(intervals)):
                c = intervals[j][0]
                d = intervals[j][1]
                if (a<c and c<b) and (b>d and d>a) or (a<=c and c<b) and (b>=d and d>a):
                    n+=1
        # if n >0 :
        return n
        # else:
        #     return n
s=Solution()
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))