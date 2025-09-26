
def predictPartyVictory(senate):
    queue=[]
    i=0
    selected=False
    d_selected=False
    while i < len(senate):
        print(i)
        if senate[i]=="D" and selected:
            senate = senate[:i] + senate[i + 1:]
            print("yes")
            print(senate)
            i=j
            selected=False
        elif d_selected and senate[i]=="R":
            senate = senate[:i] + senate[i + 1:]
            i=j
            d_selected=False
        elif senate[i]=="R":
            if selected:
                i+=1
                continue
            else:
                j=i
                selected=True
                queue.append("R")
        elif senate[i]=="D":
            if d_selected:
                i+=1
                continue
            else:
                j=i
                d_selected=True
                queue.append("D")
        i+=1
    # print(senate)
    i=0
    # while queue!=[]:
    #     curr=queue[i]

    print(queue)

# predictPartyVictory("RDDR")
# predictPartyVictory("RDRDRDRDRDDDDDD")
def predictPartyVictory1(senate):
    """who ever comes first, ban the other and goes back to the queue"""
    r_q=[]
    d_q=[]
    for i in range(len(senate)):
        if senate[i]=="R":
            r_q.append(i)
        else:
            d_q.append(i)
    print(r_q,d_q)
    while r_q!=[] and d_q!=[]:
        top=r_q.pop(0)
        top1=d_q.pop(0)
        if top<top1:
            r_q.append(top+len(senate))
        elif top>top1:
            d_q.append(top1+len(senate))
    if r_q==[]:
        return "Dire"
    else:
        return "Radiant"
print(predictPartyVictory1("RDD"))
# print(predictPartyVictory1("DDDDRRRRRD"))



