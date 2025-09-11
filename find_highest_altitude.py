def largestAltitude(gain):
    new_list=[0]
    sum=0
    for i in range(len(gain)):
        sum+=gain[i]
        new_list.append(sum)
    max=new_list[0]
    for i in range(1,len(new_list)):
        if max<new_list[i]:
            max=new_list[i]
    return max
    # print(max)
    # print(new_list)
# largestAltitude(gain = [-4,-3,-2,-1,4,3,2])
print(largestAltitude(gain = [-5,1,5,0,-7]))
