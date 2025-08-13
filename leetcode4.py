
def strStr(haystack, needle):
    j=0
    upto=len(needle)
    index=-2
    i=0
    ho_rha=0
    # for i in range(len(haystack)):
    while i <len(haystack):
        if  haystack[i]== needle[j]:
            ho_rha+=1
            if index==-2:
                index=i

            print(i,j)
            print("fursttime")
            print(haystack[i],needle[j])
            j += 1
        else:
            if ho_rha>=1:
                print(i)
                print(index)
                i=index
                ho_rha=0
                print(i)

            index=-2
            j=0
            print()
            print(i, j)
        if upto==j:
            print(j,index)
            break
        i+=1
    # print(-1)

strStr("sadbutsad","sad")
# strStr("leetcode","leeto")
# strStr("mississippi","issip")
# strStr("mississippi","pi")