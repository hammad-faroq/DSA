def isPowerOfThree( n: int):
    no=n
    i=1
    while no//3>=3:
        no=(no//3)
        i+=1
    print(i)
    if n%3==0 and not n==0 and 3**i==n or n==1:#Divide kar ka poser sa wo phir ban bi jata ka nai
        return True
    return False
print(isPowerOfThree(45))
print(isPowerOfThree(27))
print(isPowerOfThree(1))