def gcdOfStrings( str1: str, str2: str):
    not_found=True
    prefix=""
    i=0
    stack=[]
    while not_found and i<len(str2):
        if i==0:
            prefix=str2[i]
        else:
            for j in range(i+1):
                prefix+=str2[j]
        new=prefix
        st2=prefix
        l=len(prefix)
        while l<len(str2):
            st2+=prefix
            l=len(st2)
        k=len(prefix)
        while k<len(str1):
            new+=prefix
            k=len(new)
        if new==str1 and st2==str2:
            stack.append(prefix)
            i+=1
        else:
            prefix=""
            i+=1
    if stack!=[]:
        return stack[-1]
    return ""
# gcdOfStrings(str1 = "ABCABC", str2 = "ABC")
# print(gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
# print(gcdOfStrings("ABABABAB","ABAB"))
print(gcdOfStrings("AA","A"))