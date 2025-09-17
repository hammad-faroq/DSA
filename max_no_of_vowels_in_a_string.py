def maxVowels(s, k):
    """"I will have to find a sequence taht is of length k with max number of vowels"""
    """This problemm has a time complexity of 0 (n*k)"""
    vow=["a","e","i","o","u"]
    seq=""
    l=0
    max_vow=0
    no=0
    ind=0
    for i in range(len(s)):
        seq+=s[i]
        l+=1
        if l == k:
            for j in range(len(seq)):
                if seq[j] in vow:
                    no+=1
                # print(no)
            if no> max_vow:
                max_vow=no
            no=0
            seq=seq.replace(s[ind],"",1)
            l-=1
            ind+=1
    print(max_vow)
# maxVowels(s = "abciiidef", k = 3)
def maxVowels1(s, k):
    """"I will have to find a sequence taht is of length k with max number of vowels"""
    """This problemm has a time complexity of 0 (n*k)"""
    vow=["a","e","i","o","u"]
    l=0
    max_vow=0
    no=0
    ind=0
    for i in range(len(s)):
        l+=1
        if s[i] in vow:
            no+=1
        if l == k:
            if no> max_vow:
                max_vow=no
            if s[ind] in vow:
                no-=1
            l-=1
            ind+=1
    print(max_vow)
maxVowels1(s = "", k = 1)
