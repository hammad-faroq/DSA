def longestCommonPrefix(strs):
    fir=strs[0]
    common=""
    not_prefix=False
    min_len=10000000000
    for i in range(len(strs)):
        if len(strs[i])<min_len:
            min_len=len(strs[i])
    for i in range(len(fir)):
        for j in range(1,len(strs)):
            if i<len(strs[j]):
                if fir[i]!=strs[j][i]:
                    not_prefix=True
        if not_prefix:
            return common[:min_len]
        common+=fir[i]
    return common[:min_len]
print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ["dog","racecar","car"]))
print(longestCommonPrefix(["ab", "a"]))


