import math
def helper(piles,speed):
    j=0
    total_hours = 0
    while j < len(piles):
        what = piles[j]

        hours_needed = math.ceil(what / speed)
        total_hours += hours_needed
        j += 1
    return total_hours
def minEatingSpeed(piles, h):
    """"Computing the max is jsut esctra beasue we can
    do max(piles) beasue max cannot be more thatn this no matter how miuch samller the hour is"""
    speed = 5
    l = [1]
    k=-1
    find_max=True
    while find_max:
        l.append(speed)
        total_hours=helper(piles,speed)
        if total_hours <= h:
            find_max=False
        else:
            find_max=True
            speed+=5
        k += 1
    low = l[k]
    high = l[-1]
    while low<high:
        mid=(low+high)//2
        total_hours = helper(piles, mid)
        if total_hours <= h:
            high=mid
        else:
            low=mid+1

    print("Speed:", mid)


minEatingSpeed(piles = [30,11,23,4,20], h = 6)
# minEatingSpeed([1],1)
