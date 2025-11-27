class Solution:
    def maxProfit(self, prices):
        """we are finding min price in each iteration"""
        stack=prices[0]
        max1 = 0
        for i in range(len(prices)):
            s = prices[i]-stack
            if s>max1:
                max1=s
            if prices[i]<stack:
                stack=prices[i]
        return max1







    def maxProfit1(self, prices):
        """This ocde is 100% correct but ha time limit exceed issue"""
        # min=0
        max1=0
        for i in range(len(prices)):
            s=prices[i]
            for j in range(i,len(prices)):
                diff=prices[j]-s
                if diff>max1:
                    max1=diff
        return max1
s=Solution()
print(s.maxProfit(prices = [7,1,5,3,6,4]))

