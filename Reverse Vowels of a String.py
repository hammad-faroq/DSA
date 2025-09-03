def swap_chars(s, i, j):
    # Convert to list because strings are immutable
    s_list = list(s)

    # Swap characters
    s_list[i], s_list[j] = s_list[j], s_list[i]#LIST SWAPPING IS SAME AS variable swapoing

    # Convert back to string
    return "".join(s_list)#TO convert list to string
def reverseVowels(s):
    # n=len(s)//2
    d=["A","a","E","e","I","i","O","o","U","u"]
    j=-1
    i=0
    if len(s)==1 or s=="":
        return s
    kitni_dafa=0
    while i< len(s):
        k=j*(-1)-1
        # if len(s)==2 and k<=i or k==len(s):
        #     return s
        # print(len(s))
        print(k,i)
        if len(s)==2 and s[i] in d and s[j] in d:
            s = swap_chars(s, i, j)
            return s
        if k+i==len(s)-1 or k+i ==len(s):
            # print("yes")
            return s
        if s[i] in d:
            if s[j] not in d:
                j-=1
            elif s[j] in d:
                # print("yes")
                s=swap_chars(s, i, j)
                # print(s)
                # print(len(s))
                j-=1
                i+=1
                # print(i, j)
        elif s[i] not in d:
            i+=1
        # print(i, j, k)
# print(reverseVowels(s = "aI"))
# print(reverseVowels("race a car"))
# print(reverseVowels("IceCreAm"))
# print(reverseVowels("a.."))
# print(reverseVowels("Noel sees Leon."))


def reverseVowels1( s: str):
    d = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    j = len(s) - 1
    i = 0

    if len(s) <= 1:
        return s

    while i < j:  # ✅ stop when i >= j
        if s[i] in d and s[j] in d:
            s = swap_chars(s, i, j)
            i += 1
            j -= 1
        elif s[i] not in d:
            i += 1
        else:
            j -= 1
    return s
print(reverseVowels1(s = "aI"))
print(reverseVowels1("race a car"))
print(reverseVowels1("IceCreAm"))
print(reverseVowels1("a.."))
print(reverseVowels1("Noel sees Leon."))


class Solution:
    def reverseVowels(self, s: str) -> str:
        d = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}  # use set for O(1) lookup
        s_list = list(s)  # ✅ convert once
        j = len(s_list) - 1
        i = 0

        while i < j:
            if s_list[i] in d and s_list[j] in d:
                s_list[i], s_list[j] = s_list[j], s_list[i]  # ✅ swap directly
                i += 1
                j -= 1
            elif s_list[i] not in d:
                i += 1
            else:
                j -= 1

        return "".join(s_list)

