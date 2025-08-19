def mergeAlternately( word1: str, word2: str) -> str:
    w1 = len(word1)
    w2 = len(word2)
    res = ""
    if w1 > w2:
        for i in range(len(word2)):
            res += word1[i] + word2[i]
        word1 = word1[w2:]
        res += word1
    elif w2> w1:
        for i in range(len(word1)):
            res += word1[i] + word2[i]
        word2 = word2[w1:]
        res += word2
    else:
        for i in range(len(word1)):
            res += word1[i] + word2[i]
    return res
print(mergeAlternately("h","1"))