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
# pascal(10)
def pascel(r,l=None):
    if l==None:
        l=[]
    if r==1:
        l.append([1])
    elif r==2:
        l.append([1,1])
    else:
        l2=[1,1]
        l3=l[r-2]
        l4=inserrt(l2,l3)
def pasacel(r,l=None):
    if l==None:
        l=[[1]]
        r=r-1
        pasacel(r)
    if r>2:
        l1=pascel(r-1)
        l2=l1[r-2]
    elif r==2:
        l.append([1])
        l.append([1,1])
        return l
def inserrt(l3):
    l2=[1,1]
    for i in range(len(l3)-1):
        value=i+1
        l2.insert(value,l3[value]+l3[i])
    return l2
def p(r,l=[]):
    """This is the recursive functiton of the pascal traingle with one iterative function named inserrt to insert values into the list according to the row number :)"""
    if r==0:
        print(l)
    if l==[]:
        if r==1:##This if is to the first row so taht [[1],[1,1]] will ot be printed when row 1 is entered
            l.append([1])
            p(r=0,l=l)
        l1=[[1],[1,1]]
        r=r-2
        p(r,l1)
    elif r>=1:
        value=len(l)##How many values we need to insert in the list
        l3=l[value-1]
        l2=inserrt(l3)#The insertion is done usign the iterable fuction user defined
        l.append(l2)
        p(r-1,l)
p(r=996)



