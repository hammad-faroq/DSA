def pascal(r):
    """This is the iterative way of forming the pascal traingle"""
    l=[]
    for i in range(1,r+1):
        if i == 1:
            l.append([1])
        elif i == 2:
            l.append([1, 1])
        else:
            l1 = l[(i-1) - 1]
            l3 = [1, 1]
            for i1 in range(2,i):
                value=i1-1
                l3.insert(value,l1[value]+l1[value-1])
            l.append(l3)
    print(l)