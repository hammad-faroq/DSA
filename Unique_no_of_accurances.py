def uniqueOccurrences(arr):
    s=set()
    d={}
    l=[]
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]]=1
        else:
            now=d[arr[i]]
            now+=1
            d[arr[i]]=now
    for i in d:
        s.add(d[i])
        l.append(d[i])
    if len(s)!=len(l):
        return False
        # print("false")
    else:
        return True
        # print("True")
uniqueOccurrences([1,2,1,2,3,4])