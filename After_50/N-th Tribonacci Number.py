def tribonacci(n,memo={}):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    if n in memo:
        return memo[n]

    memo[n]=tribonacci(n-1,memo)+tribonacci(n-2,memo)+tribonacci(n-3,memo)#store and then return
    return memo[n]
print(tribonacci(4))
print(tribonacci(25))
