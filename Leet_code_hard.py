import random


def isMatch(s, p):
    if p == ".*":
        return True
    i = 0
    random_remove = 0
    chal_gi=False
    while i < len(p):
        print(s,p)
        # print(p)
        if i != len(p) - 1:
            # print("yayay")
            # print(p[i],p[i+1])
            if p[i].isalpha() and p[i + 1] == "*":
                # print("yes")
                if len(p)>2:#For case a*a
                    if p[i]==p[i+2] or p[i] in s:
                        # print("OOOO")
                        j=i+2
                        while j<len(p):
                            # print("removing after")
                            if j+1< len(p):
                                if p[j]==p[i] and p[j+1]=="*":
                                    print("uauauau")
                                    p = p[:j] + "" + p[j + 2:]
                                    # continue
                                    # # print("oooo")
                                    # # print(p[j])
                                    # # print(p[j+1])
                                    # # print(p[j],p[j+1])
                                    # no = p[j]
                                    # no1 = p[j + 1]
                                    # p = p.replace(no, "", 1)
                                    # p = p.replace(no1, "", 1)
                                    # # print(p[j], p[j + 1])
                                    # # print(p)

                            if p[j] == p[i]:
                                p = p[:j] + "" + p[j + 1:]                  #removing taht from p
                            else:
                                j+=1
                # print(p[i],p[i+1])
                s = s.replace(p[i], "")
                no=p[i]
                no1=p[i+1]
                p=p.replace(no,"",1)
                p = p.replace(no1, "", 1)
                # print("removing two",len(p)-1)
                print(p)
                chal_gi=True

            elif p[i] == "." and p[i + 1] == "*":
                p=p[i+2:]
                if len(p)==1:#1 lenght case
                    if p[-1] in s:
                        p=p.replace(p[i], "", 1)

                for i in range(len(p)-1,-1,-1):
                    if p[i] in s:
                        p=p.replace(p[i],"",1)
                # print(p)
                if p=="":
                    print(True)
                    return True
                else:
                    print(False)
                    return False
        if chal_gi:
            chal_gi=False
            continue
        if i<len(p):
            if p[i] == ".":
                p=p.replace(".","",1)
                print("removing one", len(p)-1)
                random_remove += 1
            elif p[i] not in s:
                # print(p[i],s)
                i += 1
            elif p[i] in s:
                print("removing one last if", p[i])
                s = s.replace(p[i], "", 1)
                no=p[i]
                p=p.replace(no,"",1)
    # print(random_remove)
    print(random_remove)
    while random_remove >= 1 and len(s)>=1:
        print("why")
        s = s.replace(s[0], "", 1)
        random_remove -= 1
    print(s)

    print("the p is",p)
    print(random_remove)
    if s == "" and p=="":
        print(True)
        return
    if s != "" or p!="":
        print(False)


# isMatch("mississippi", "mis*is*p*.")
isMatch("aaba", "ab*a*c*a")

