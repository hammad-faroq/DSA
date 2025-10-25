def isPalindrome( s: str) -> bool:
    """another approch can be reverse the string ond chek if it is equal to the original string or not"""
    valid=""
    for i in s:
        if i.isalpha() or i.isdecimal():
            valid+=i.lower()
    mid=len(valid)//2
    if len(valid)%2==0:
        f=valid[:mid]
        s1=valid[mid:]
    else:
        f = valid[:mid]
        s1 =valid[mid+1:]
    # print(f,s)
    for i in range(len(f)):
        j=i+1
        if f[i]!=s1[-j]:
            return False
    return True

# print(isPalindrome( s = "A man, a plan, a canal: Panama"))
print(isPalindrome("0P"))