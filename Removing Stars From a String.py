def removeStars(s):
    """If i tried to solve with core logic, it would be very difficult to sove this, using s imple data stucture like stack make things easy for me (:"""
    """one approch would be jo stack me reah gya wo ans, rahter tahtnremove start ane ele from the original string"""
    stack=[]
    i=0
    while i < len(s):
        if s[i] != "*":
            stack.append(i)
            i+=1
        elif s[i]== "*":
            s = s[:i] + s[i + 1:]
            j=stack.pop()
            s=s[:j] + s[j+1:]
            i-=1
    return s
print(removeStars(s = "leet**cod*e"))
removeStars(s = "erase*****")