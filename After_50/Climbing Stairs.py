def climbStairs1(n):
    """Ways[i]==ways[i-1]+ways[i-2]"""
    """For example n=4 == all combincation of 2 and 3 """
    """time liit exceed on leetcode"""
    if n==1:
        return 1
    elif n==2:
        return 2
    return climbStairs(n-1)+climbStairs(n-2)
    #problem is recalculation is prev multiple thimes like for 4 cal 3,2 for 5 cal 4,2?


def climbStairs(n, memo={}):
    """Ways[i]==ways[i-1]+ways[i-2]"""
    """simle meemoization rpoblem"""
    """bottom up"""
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Check if already calculated
    if n in memo:
        return memo[n]

    # Calculate and store
    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)
    return memo[n]
# print(climbStairs(1))
# print(climbStairs1(1))
print(climbStairs(50))
print(climbStairs1(50))
# print(climbStairs(100))
# print(climbStairs1(100))


def climbStairs2(n):
    """Bottom up no recursion"""
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev, curr = 1, 2
    for i in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr
print(climbStairs2(50))
print(climbStairs1(50))