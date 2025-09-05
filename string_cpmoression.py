def compress(chars):
    count=1
    char=""
    j=0
    if len(chars)==1:
        return len(chars)
    for i in range(len(chars)):
        if i ==0:
            char=chars[i]
        elif char==chars[i]:
            count+=1
        else:
            if count==1:
                chars[j]=char
                char=chars[i]
                j+=1
            else:
                if count>9:
                    count=str(count)
                    chars[j] = char
                    j+=1
                    for k in count:
                        chars[j]=k
                        j+=1
                    char = chars[i]
                    count=int(count)
                    count=1
                else:
                    chars[j]=char
                    chars[j+1]=str(count)
                    j+=2
                    count=1
                    char=chars[i]
        if i==len(chars)-1:
            print(count)
            if count==1:
                chars[j]=char
                j+=1
            if count > 9:
                print("uaua")
                count = str(count)
                chars[j] = char
                j += 1
                for k in count:
                    chars[j] = k
                    j += 1
            # print("uauau")
            if count<=9 and count!=1:
                print("yaay")
                print(j)
            # if int(count)<9:
                chars[j] = char
                chars[j + 1] = str(count)
            # print(j)
                j+=2
            for i in range(j,len(chars)):
                chars.pop()
    print(chars)
    return len(chars)
    # print(chars)
# compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","b","b"])
# compress(["a","a","a"])
# compress(["a","b","b"])

# print(compress(["a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","d"]))
# print(compress(["a","a","b","b","c","c","c"]))
# print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
# print(chars)
# print(compress(["a","b","c"]))
print(compress(["v","r","r","r","r","r","r","r","r","r"]))