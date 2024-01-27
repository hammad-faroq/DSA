def number_occurance(n):
    list=[]
    for i in n:
        count = 0
        if i in list:
            continue
        else:
            for j in n:
                if i==j:
                    count+=1
            list.append(i)
            print(f"The number{i} exist {count} times!")
number_occurance([1,2,3,4,1,2,3,4,1,2,3,4,0])