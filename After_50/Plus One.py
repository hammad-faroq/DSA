def plusOne(digits):
    if digits==[]:
        return digits
    c=""
    l=[]
    for i in range(len(digits)):
        c+=str(digits[i])
    c=int(c)+1
    c=str(c)
    for i in c:
        l.append(int(i))
    return l

    # return c.split()
print(plusOne([1,2,3]))
# print(plusOne([9,9]))