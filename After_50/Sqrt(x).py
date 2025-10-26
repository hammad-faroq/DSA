def mySqrt( x: int):

    for i in range(x):
        if i*i<=x and (i+1)*(i+1)>x:
            return i
print(mySqrt(8))