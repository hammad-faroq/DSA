def minFlips(a, b, c):
    min=0
    while a>0 or b>0 or c>0:
        # print("yes")
        bit_a = a % 2
        bit_b = b % 2
        bit_c= c % 2
        if bit_c==0:
            if bit_a==1:
                min+=1
            if bit_b==1:
                min+=1
        if bit_c==1:
            if bit_a==0 and bit_b==0:
                min+=1
        a //= 2
        b //= 2
        c //=2
    return min
minFlips(a = 2, b = 6, c = 5)
# 0001,0111