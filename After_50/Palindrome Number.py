def isPalindrome( x: int):
    new=str(x)
    new=new[::-1]
    if new==str(x):
        return True
    return False
    # print(new)
print(isPalindrome(-123))