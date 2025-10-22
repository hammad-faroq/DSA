def countBits(n):
    l=[0]
    for i in range(1,n+1):
        c = 0
        while i!=0:
            if i & 1 == 1:
                c += 1
            i = i >> 1
        l.append(c)
    return l
countBits(2)

    # while n!=0:
    #     if n &1 == 1:
    #         c+=1
    #     n=n >> 1
    # print(c)
countBits(5)

