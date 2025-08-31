# class Solution:
def kidsWithCandies(candies, extraCandies):
    max=0
    out=[]
    for i in range(len(candies)):
        out.append(False)
        if candies[i]> max:
            max=candies[i]
    # print(out)
    for i in range(len(candies)):
        if candies[i]+extraCandies >= max:
            out[i]=True
    print(out)
kidsWithCandies(candies = [4], extraCandies = 0)
