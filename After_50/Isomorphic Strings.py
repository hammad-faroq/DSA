class Solution:
    def isIsomorphic(self, s: str, t: str):
        """one to one mapping but one elemtn myust match to the same elemtn"""
        s1={}
        s2={}
        j=0
        for i in s:
            if i in s1 and s1[i]!=t[j]:
                return False
            if i not in s1 and t[j] in s1.values():
                return False
            s1[i]=t[j]
            j+=1
        return True
s=Solution().isIsomorphic(s = "aabb",t = "abab")
s1=Solution().isIsomorphic(s = "foo",t = "baa")
s2=Solution().isIsomorphic(s = "badc",t = "baba")
print(s2,s1,s)


        # for i in s:
        #     s1.add(i)
        # for i in t:
        #     s2.add(i)
        # return len(s1)==len(s2)