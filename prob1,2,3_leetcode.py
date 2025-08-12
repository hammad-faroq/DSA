#prob#2
def addBinary(a, b):

    l1=len(a)
    l2=len(b)
    new=""
    if l1>l2:
        diff=l1-l2
        for i in range(diff):
            new+="0"
        b=new+b
    elif l2>l1:
        diff = l2 - l1
        for i in range(diff):
            new += "0"
        a = new + a

    #     choose=l1
    #     not_choose=l2
    #     dict={"not":"b"}
    # if l2>l1:
    #     choose=l2
    #     not_choose=l1
    #     dict={"not":"a"}
    # if l2==l1:
    #     not_choose=choose=l1
    # reverse=False
    # for i in range(not_choose,choose):
    #     reverse=True
    #     if dict["not"]=="a":
    #         a+="0"
    #     else:
    #         b+="0"
    # if reverse:
    #     if dict["not"]=="a":
    #         a = a[::-1]
    #     else:
    #         b = b[::-1]
    print(a,b)
    result=""
    cary=""
    l1=len(a)
    for i in range(l1-1,-1,-1):
        if a[i]=="1" and b[i]=="0" and cary=="1" or a[i]=="0" and b[i]=="1" and cary=="1":
            cary="1"
            result+="0"
        elif a[i]=="1" and b[i]=="0" and cary=="" or a[i]=="0" and b[i]=="1" and cary=="":
            cary=""
            result+="1"
        elif a[i]=="0" and b[i]=="0" and cary=="":
            result+="0"
        elif a[i]=="0" and b[i]=="0" and cary=="1":
            result+="1"
            cary=""
        elif a[i] == "1" and b[i] == "1" and cary=="":
            cary="1"
            result+="0"
        elif a[i] == "1" and b[i] == "1" and cary=="1":
            cary="1"
            result+="1"
    if cary=="1":
        result+="1"
    result=result[::-1]
    print(result)
# addBinary("1010","1011")
addBinary("100","110010")

#prob1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # L1=[]
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             L1.append(i)
        #             L1.append(j)
        #             return L1
        # now implementing using hash map
        dict = {}
        for i in range(len(nums)):
            dict[i] = nums[i]
        for key in dict:
            comp = target - dict[key]
            if comp in dict.values():
                other = list(dict.values()).index(comp)
                if other == key:
                    continue
                data = []
                data.append(key)
                data.append(other)
                return data

#prob 3
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                "CD": 400, "CM": 900}
        num = 0
        skip = False
        for i in range(len(s) - 1):
            if skip:
                skip = False
                continue
            if s[i] + s[i + 1] in dict:
                st = s[i] + s[i + 1]
                num += dict[st]
                skip = True
            elif s[i] in dict:
                num += dict[s[i]]
                skip = False
        if not skip:
            num += dict[s[-1]]
        return num






