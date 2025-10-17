def dailyTemperatures(temperatures):
    stack=[]
    for i in range(len(temperatures)):
        count=1
        is_break=False
        # stack.append([temperatures[i]])
        # while stack!=[]:

        for j in range(i+1,len(temperatures)):
        #     if stack[-1]>temperatures[j]:
        #         stack.append(temperatures[j])
        #     else:
        #         break
            if temperatures[i]<temperatures[j]:
                is_break=True
                break
            else:
                count+=1
        if not is_break:
            stack.append(0)
        else:
            stack.append(count)
    print(stack)
dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
# dailyTemperatures(temperatures = [30,40,50,60])
# dailyTemperatures(temperatures = [30,60,90])

def dailyTemperatures1(temperatures):
    monotonic_stack=[0]
    result = [0] * len(temperatures)
    # br=False
    for i in range(1,len(temperatures)):
        br = False
        if not monotonic_stack or temperatures[monotonic_stack[-1]]>=temperatures[i]:
            monotonic_stack.append(i)
        else:
            while monotonic_stack!=[]:
                ind=monotonic_stack.pop()
                if temperatures[ind] >= temperatures[i]:
                    monotonic_stack.append(ind)
                    monotonic_stack.append(i)
                    br=True
                    break#jab break ho jya to bahit a kar na lagaya
                result[ind] = i-ind

            if not br:
                monotonic_stack.append(i)
                br=False
    print(result)
dailyTemperatures1(temperatures=[55,38,53,81,61,93,97,32,43,78])
            # if monotonic_stack==[]:
            #     count = 0







        # while monotonic_stack:
        #     if temperatures[monotonic_stack[-1]]>=temperatures[i]:
        #         monotonic_stack.append(i)
        #     else:


