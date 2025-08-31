
def reverseWords(s):
    stack=[]
    s=s.strip()
    one_spcae=False
    for i in s:
        stack.insert(0,i)
    out=""
    s=""
    for i in range(len(stack)):
        if stack[i]!=" ":
            s+=stack[i]
            one_spcae=False
        elif one_spcae:
            continue
        else:
            one_spcae=True
            s=s[::-1]
            s+=" "
            # print(s)
            out+=s
            s=""
    s = s[::-1]
    # print(s)
    out += s

    print(out)
    print(stack)
reverseWords(s = "  hello world  ")
reverseWords(s = " the ")
reverseWords("a good   example")