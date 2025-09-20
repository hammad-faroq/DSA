# def decodeString(s):
#     """it gonna work on single approch but not nested approch"""
#     stack=[]
#     how_muc=""
#     what=""
#     seq=""
#     k=0
#     l=0
#     ya_hoa=False
#     for i in range(len(s)):
#         # print(stack)
#         # print(l)
#         if s[i]!="]":
#             if s[i]=="[":
#                 l+=1
#             stack.append(s[i])
#         elif s[i]=="]":
#             # print()
#             # print(stack)
#             # print()
#             for j in range(len(stack)):
#                 print(stack)
#                 if stack !=[]:
#                     # print("yes")
#                     d=stack.pop()
#                 if d=="[":
#                     print()
#                     print(stack)
#                     if l>1:
#                         if stack is not []:
#                             ya_hoa=True
#                             d=stack.pop()
#                             for m in range(len(stack)):
#                                 o = stack.pop()
#                                 if not 'a' <= o <= 'z':
#                                     d+=o
#                                 else:
#                                     break
#                                 d=d[::-1]
#                             what=what[::-1]
#                             seq+=int(d)*what
#                             stack.append(seq)
#                             if k ==0:
#                                 seq=""
#                             k+=1
#                         what=""
#                     else:
#                         l-=1
#                         continue
#                 elif 'a' <= d <= 'z':
#                     what+=d
#                 else:
#                     how_muc+=d
#                 # print(stack)
#             if not ya_hoa:
#                 what=what[::-1]
#                 how_muc=how_muc[::-1]
#                 # print()
#                 # print(what)
#                 # print(how_muc)
#                 how_muc=int(how_muc)
#                 for i in range(how_muc):
#                     seq+=what
#             how_muc=""
#             what=""
#     print(seq)
# # decodeString(s = "3[a2[c]3[b]4[ac]]")
# # decodeString(s = "3[a2[c]]")
# # decodeString(s = "3[a]4[bc]")
















def decodeString1(s):
    """This gonna insahllah work for the nested approch"""
    stack=[]
    # u=0
    for i in range(len(s)):
        if s[i]!="]":
            # if s[i]=="[":
            #     u+=1
            # else:
            stack.append(s[i])
        else:
            what = ""
            while stack and stack[-1] != "[":
                what = stack.pop() + what
            stack.pop()  # remove "["

            # step 2: collect number (could be multiple digits)
            how_muc = ""
            while stack and stack[-1].isdigit():
                how_muc = stack.pop() + how_muc
            how_muc = int(how_muc)

            # step 3: expand substring and push back
            seq = what * how_muc
            stack.append(seq)

            # final decoded string
        return "".join(stack)
    # d=stack.pop()
    # while stack is not []:

# print(decodeString1(s = "3[a2[c]]"))

def decodeString(s):
    """Updated to handle nested approach using stack"""
    stack = []
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            print(stack)
            print("Uauda")
            # step 1: collect substring inside [...]
            what = ""
            while stack and stack[-1] != "[":
                what = stack.pop() + what
            stack.pop()  # remove "["

            # step 2: collect number (could be multiple digits)
            how_muc = ""
            while stack and stack[-1].isdigit():
                how_muc = stack.pop() + how_muc
            how_muc = int(how_muc)

            # step 3: expand substring and push back
            seq = what * how_muc
            stack.append(seq)
            print(stack)

    # final decoded string
    return "".join(stack)


# 🔍 Tests
# print(decodeString("3[a]2[bc]"))  # aaabcbc
print(decodeString("3[a2[c]3[b]]"))  # accaccacc
# print(decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
# print(decodeString("10[a]"))  # aaaaaaaaaa

#How i gonna solve tis problem into when nested


