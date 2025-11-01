def main(s):
    """updaed version of the one whcih i ahve done In the DSA lab some time ago"""
    s2=[]
    l=len(s)
    d=["{","[","("]
    d1=["}",')',']']
    for i in range(l):
        if s[i] in d:
            s2.append(s[i])
        elif s[i] in d1:  # THis is the boundery check
            if not s2:
                return False
            top = s2[-1]
            if (top == "(" and s[i] == ")") or \
                    (top == "[" and s[i] == "]") or \
                    (top == "{" and s[i] == "}"):
                s2.pop()
            else:
                return False
    if s2 == []:
        return True
    return False
# main("{(123)+(123)+[1223](1)2}")
# main("")
# print(main("()()"))
print(main("()"))
