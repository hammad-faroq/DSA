def closeStrings(word1, word2):
    """attain word 2 from word1"""
    dict={}
    dict1={}
    if len(word2)!= len(word1):
        print(False)
        return False
    for i in range(len(word2)):
        if i==0:
            key=word2[i]
            key2=word1[i]
            dict[key]=1
            dict1[key2]=1
        else:
            if word1[i] in dict1:
                value = dict1[word1[i]]
                value += 1
                dict1[word1[i]] = value
            else:
                key1 = word1[i]
                dict1[key1] = 1

            if word2[i] in dict:
                value=dict[word2[i]]
                value+=1
                dict[word2[i]]=value
            else:
                key=word2[i]
                dict[key]=1
    if len(dict1)!= len(dict):
        print(False)
        return False
    sorted_values = sorted(dict.values())
    sorted_values1=sorted(dict1.values())
    if set(word1) != set(word2):
        return False#UA and SSX

    if sorted_values1==sorted_values:
        print(True)
        return
    else:
        return False
# closeStrings(word1 = "abc", word2 = "bca")
# closeStrings(word1 = "a", word2 = "aa")
# closeStrings(word1 = "cabbbab", word2 = "abbcccc")
# closeStrings("cabbba","aabbss")
closeStrings("uau","ssx")