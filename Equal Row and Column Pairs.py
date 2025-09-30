def equalPairs(grid):
    d={}
    start=True
    for i in range(len(grid)):
        print(grid[i])
        col=grid[i]
        k=0
        for j in range(len(col)):
            if start:
                d[k]=[col[j]]
                k+=1
            else:
                l=d[k]
                l.append(col[j])
                d[k]=l
                k+=1
        start=False
    count=0
    for i in range(len(grid)):
        curr=grid[i]
        for i in d:
            if d[i]==curr:
                count+=1
    print(count)
    print(d)
    return count



equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]])