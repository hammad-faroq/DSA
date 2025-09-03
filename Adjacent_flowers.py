def canPlaceFlowers(flowerbed, n):
    if  n==0:
        return True
    if len(flowerbed)==1 and n>0:
        if flowerbed[0]==0 and n==1:
            return True
        return False
    if len(flowerbed)==2 and n==1:
        if flowerbed[0]==flowerbed[1]==0:
            return True
        return False


    for i in range(1,len(flowerbed)-1):
        # print("yay")
        if i==len(flowerbed)-2 and  flowerbed[i]==flowerbed[i+1]==0:
            print("aduau")
            flowerbed[i+1]=1
            n-=1
        if i==1 and flowerbed[i-1]==0 and flowerbed[i]==0:#first boundry case

            print("I ran")
            flowerbed[i-1]=1
            n-=1
        print(n)
        if n<=0:
            return True
        elif flowerbed[i-1]==flowerbed[i+1]==flowerbed[i]==0:
            flowerbed[i]=1
            n-=1
    return False
    # flowerbed[2]==1
    # print(flowerbed)
# print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
# print(canPlaceFlowers(flowerbed = [1], n = 2))
# print(canPlaceFlowers([1,0,1,0,1,0,1],n=1))
# print(canPlaceFlowers([0,0,1,0,1],n=1))
print(canPlaceFlowers([0,0,0],n=1))
