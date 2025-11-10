def minCostClimbingStairs(cost):
    dp=[None for  i in range(len(cost)+1)]
    dp[0]=0
    dp[1]=0
    for i in range(2,len(cost)+1):
        dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[len(cost)]

print(minCostClimbingStairs([10,15,20]))

