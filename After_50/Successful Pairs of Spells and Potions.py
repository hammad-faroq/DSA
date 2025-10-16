import math
def successfulPairs(spells, potions, success):
    """Not that efficinet """
    l=[]
    potions.sort()
    for spell in spells:
        count = 0
        for j in range(len(potions)):

        # math.ceil(success / spell)
            if (spell*potions[j])>=success:
                count=len(potions)-j
                break
        l.append(count)
    print(l)
successfulPairs(spells = [5,1,3], potions = [1,2,3,4,5], success = 7)



"""spell * potion >= success.

If we rearrange:

potion >= success / spell"""


from bisect import bisect_left# this unction gonna reutnr the first occurance of that number, or if taht number no exist, then the index wheew wehn it put list reamins sorted

# class Solution:
def successfulPairs1( spells, potions, success):
    """We gonna find the min_portion needed for each speel and we gonna upeend hte count of the above when we ind the index of the min_potion_value to the lsit"""
    potions.sort()  # safe to sort
    m = len(potions)
    res = []

    for spell in spells:  # keep spell order same
            # smallest potion needed for success
        min_potion_needed = (success + spell - 1) // spell  # ceil division
        index = bisect_left(potions, min_potion_needed)### this gonna find the vlaue (index), and that value is min+potion index due to cahnge in formula
        res.append(m - index)
    return res
